# Project-Ragnarok

一个基于websocket的聊天室


&nbsp;
## 运行环境
Python 3

&nbsp;
## 特性
*  全双工 websocket，随时向客户端推送消息
*  运用非阻塞异步架构
*  消息广播 
*  客户端指定对另一客户端的定向信息(开发中)
*  

&nbsp;
## 初始化
#### 1. 安装 websockets 库
```shell 
pip3 install websockets
```

&nbsp;
#### 2. 生成 SSL certificate (按需)
```shell
$ openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.crt
```

&nbsp;
#### 3. 客制化 Config.json
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

* SSL: 是否使用ssl加密通信
* SSL_Cert: cert文件目录
* SSL_Key : key文件目录
* server_ip : vps的公网ip或者localhost
* server_port: 监听端口
* server_name: 聊天室的标题
* server_password :  不填写会让服务器对公共开放

&nbsp;
#### 4. 启动服务器
``` shell
$ python3 server.py
```

&nbsp;
## 信息结构
这部分描述可以用作第三方客户端开发的参考

``` json
{
	"msgType":"type",
  "SrcUser": "username1",
  "TgtUser": "username2",
  "text" : "msg",
  "Users" : ["一个由在线用户组成的list"]
}
```

&nbsp;
#### 广播信息
msgType = "Broadcast"  时，此条信息会向所有建立连接的客户端发送

客户端不发送 "SrcUser" ，服务器在处理信息的时候会通过连接添加这个属性防止冒用身份

"TgtUser" 留空
"text" 是正文

"Users" 在这个种类的信息中为空

&nbsp;
#### 在线用户通知
"msgType" = "OnlineUsers" 

"Users" 长得比较像 ["john","smith"...]

客户端通过解包json，刷新在线客户端

&nbsp;
#### 私聊信息 (开发中)
"msgType" = "PrivateMessage" 

客户端将 "TgtUser" 发送到服务器

然后 "SrcUser" 会被服务器添加

"text" 也许会是16进制的字符串 (使用RSA 加密),需要公钥交换(未完成)

所以服务器无法解密信息内容，仅将信息转发到 "TgtUser"

##
## License
[The MIT License (MIT)](https://raw.githubusercontent.com/v2ray/v2ray-core/master/LICENSE)
