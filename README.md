# Project-Ragnarok

A chatroom server based on websocket

**[README-CN.md](https://github.com/kingsznhone/Project-Ragnarok/blob/master/README-CN.md)**.

 

## Ideology

This project is based on my victimized delusion.

Like what ***1984*** says "Big Brother is watching you."

We are going to cyberpunk era.

Whatever in Eastern or Western, We all the same

We live in a world that Gov has in charge of every corner.

Telegram can do the same thing, that's right. 

But our privacy. 

Shouldn't be in any company or someone else's hand.

Maybe I can call this Project : Everyone TG.

Cuz I want Everyone in Internet , have their own chatroom server, a safe house

This project is ugly but it works.

Share Your opinion in this tiny chatroom

**click on Star if you're interested**

&nbsp;
## System requirements 
Python 3

&nbsp;
## Feature
*  Websocket full duplex
*  Asnyc structure
*  Message broadcast 
*  Point to point message exchange(under dev)
*  

&nbsp;
## Initialization
#### 1. Install websockets library
```shell 
pip3 install websockets
```

&nbsp;
#### 2. Generate SSL certificate (If needed)
```shell
$ openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.crt
```

&nbsp;
#### 3. Mod Config.json
``` json
{
	"SSL": true,                    
	"SSL_Cert": "self-signed.crt",  
	"SSL_Key": "self-signed.pem",   
	"server_ip": "127.0.0.1",      
	"server_port": 12345,           
	"server_name":"Ks",             
	"server_password":"963"         
}
```

* SSL: Using ssl encryption or not 
* SSL_Cert: path to cert file
* SSL_Key : path to key file 
* server_ip : public ip address if running on VPS
* server_port: port to listen
* server_name:A.K.A chatroom title
* server_password#  Empty for public chatroom

&nbsp;
#### 4. Start server 
``` shell
$ python3 server.py
```

&nbsp;
## Message Structure
This part of discription is for third-party client design

``` json
{
	"msgType":"type",
  "SrcUser": "username1",
  "TgtUser": "username2",
  "text" : "msg",
  "Users" : ["list of onlineusers"]
}
```

&nbsp;
#### Broadcast message 
msgType = "Broadcast"  is a message needs to broadcast to all online user

Client doesn't send "SrcUser" ,it will be assigned by server

"TgtUser" will be empty

"text" is what you want to say

"Users" is empty for this type of message

&nbsp;
#### Online users notification
"msgType" = "OnlineUsers" 

"Users" looks like ["john","smith"...]

Client Unpack those value to update online user's name

&nbsp;
#### Privatemessage (under dev)
"msgType" = "PrivateMessage" 

Client send "TgtUser" to server

Then "SrcUser" will be assigned by server

"text" might be a hex string (RSA encrypted),need private key exchange(Uncomplete)

So that server can not decrypt this message, only forward to "TgtUser"

##
## License
[The MIT License (MIT)](https://github.com/kingsznhone/Project-Ragnarok/blob/master/LICENSE)
