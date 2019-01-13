
from socket import *

server=socket(AF_INET,SOCK_STREAM)
#在网络上表明身份，其他电脑访问要使用ip+port
server.bind(("127.0.0.1",8848))

#开启服务器监听
server.listen(100)

while True:
    client,clientaddr=server.accept()
    print(clientaddr)
    datacode = client.recv(1024)
    print(datacode.decode("utf-8"))

    #     客户端如果想要收到信息服务器必须进行返回
    resonse_start = "HTTP/1.1 200 OK\r\n"
    resonse_body = "<html><head> <meta charset='utf-8' /></head> <body>  Success 注册成功 </body></html>"
    # 构造返回对象
    response = resonse_start + "\r\n" + resonse_body
    # 给与客户端返回内容
    client.send(response.encode("utf-8"))