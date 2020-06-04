import asyncio
import json
import ssl
from cfgloader import loadcfg
import websockets

CONFIG = loadcfg()
PASSWORD = CONFIG["server_password"]
USERS = {}
SERVERNAME = "TestServer"
host = CONFIG["server_ip"]
port = CONFIG["server_port"]

def onlineUsers_event():
    str_list = list(USERS.values())
    return json.dumps({"msgType":"OnlineUsers","Users": str_list})

def ServerInfo_event():
    return json.dumps({"ServerName": SERVERNAME})

async def notify_onlineUsers():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = onlineUsers_event()
        await Broadcast(message)


async def notify_serverinfo():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = ServerInfo_event()
        await Broadcast(message)


async def Broadcast(message):
    if USERS:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(message) for user in USERS])

async def PrivateMessage(websocket,message):
    await websocket.send(message)

async def distribution(websocket, message):
    dict = json.loads(message)

    if dict["msgType"] == "Broadcast":
        dict["SrcUser"] = USERS[websocket]
        msg = json.dumps(dict)
        await Broadcast(msg)

    if dict["msgType"] == "PrivateMessage":
        dict["SrcUser"] = USERS[websocket]
        for ws,user in USERS.items():
            if user ==dict["TgtUser"]:
                del dict["TgtUser"]
                msg = json.dumps(dict)
                await PrivateMessage(ws, msg)


async def passauth(websocket):
    password = await websocket.recv()
    return True if ((password == PASSWORD) or (PASSWORD=="")) else False


async def register(websocket):
    if await passauth(websocket) == True:
        name = await websocket.recv()
        print(f"< {name}")
        if name not in USERS.keys():
            USERS[websocket] = name
            return True
        else:
            return False
    else:
        return False


async def unregister(websocket):
    try:
        await websocket.close()
        del USERS[websocket]
        await notify_onlineUsers()
    except Exception as inst:
        print(inst)


async def establish(websocket, path):
    # register(websocket) sends user_event() to websocket
    try:
        if await register(websocket):
            await notify_serverinfo()
            await notify_onlineUsers()
            while True:
                msg = await websocket.recv()
                await distribution(websocket, msg)

    finally:
        await unregister(websocket)



if CONFIG["SSL"]:
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ssl_context.load_cert_chain('self-signed.crt', 'self-signed.pem', password=None)
    start_server = websockets.serve(establish, host, port, ssl=ssl_context)
else:
    start_server = websockets.serve(establish, host, port)
print(f"Listen on %s:%d"%(host,port))
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
