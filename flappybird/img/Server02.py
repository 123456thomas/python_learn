"""
用Python编写Web服务器
需要使用Socket模块
"""
# 引入socket通信模块
from socket import *
# 创建服务器对象 TCP Socket
server = socket(AF_INET, SOCK_STREAM)
# 在网络上表名身份  其他电脑想要连接需要使用IP  + Port
server.bind(("127.0.0.1", 8990))
# 开启服务器监听（开始接受连接）
server.listen(100)

while True:
    # 阻塞操作  当有客户端连接时client ， clientaddr被赋值
    client, clientaddr = server.accept()
    # 打印客户端IP 端口
    # print(clientaddr)
#     获取客户端信息
    datacode = client.recv(1024)
    print(datacode.decode("utf-8"))


#     客户端如果想要收到信息服务器必须进行返回
    resonse_start = "HTTP/1.1 200 OK\r\n"
    resonse_body = "<html><head> <meta charset='utf-8' /></head> <body>  Success 注册成功 </body></html>"
    # 构造返回对象
    response = resonse_start + "\r\n" + resonse_body
    # 给与客户端返回内容
    client.send(response.encode("utf-8"))

