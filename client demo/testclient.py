import asyncio
import pathlib
import ssl
import websockets
import json
import threading
from threading import Thread

async def rx (websocket):
    while True:
        greeting = await websocket.recv()
        print (greeting)

async def startclient():
    uri = "wss://localhost:8765"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        
        await websocket.send("963")
        await websocket.send("Kings")
        while True:
            greeting = await websocket.recv()
            greeting = greeting.encode('utf-8').decode('unicode_escape')
            print(f"< {greeting}")

            #buffer = json.dumps({"msgType":"PrivateMessage",
            #                     "TgtUser":"Queens",
            #                     "text":input()})
            buffer =  json.dumps({"msgType":"Broadcast","text":input()})
            await websocket.send(buffer)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ssl_context.load_verify_locations("self.crt")
asyncio.get_event_loop().run_until_complete(startclient())

