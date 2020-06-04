# Project-Ragnarok

A chatroom server based on websocket


##
## System requirements 
Python 3

##
## Feature
*  Websocket full duplex
*  Asnyc structure
*  Message broadcast 
*  Point to point message exchange(under dev)
*  
##
## Initialization
#### 1. Install websockets library
```shell 
pip3 install websockets
```
####
#### 2. Generate SSL certificate (If needed)
```shell
$ openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.crt
```
####
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
####
#### 4. Start server 
``` shell
$ python3 server.py
```

##
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

####
#### Broadcast message 
msgType = "Broadcast"  is a message needs to broadcast to all online user

Client doesn't send "SrcUser" ,it will be assigned by server

"TgtUser" will be empty

"text" is what you want to say

"Users" is empty for this type of message

####
#### Online users notification
"msgType" = "OnlineUsers" 

"Users" looks like ["john","smith"...]

Client Unpack those value to update online user's name

####
#### Privatemessage (under dev)
"msgType" = "PrivateMessage" 

Client send "TgtUser" to server

Then "SrcUser" will be assigned by server

"text" might be a hex string (RSA encrypted),need private key exchange(Uncomplete)

So that server can not decrypt this message, only forward to "TgtUser"

##
## License
[The MIT License (MIT)](https://raw.githubusercontent.com/v2ray/v2ray-core/master/LICENSE)
