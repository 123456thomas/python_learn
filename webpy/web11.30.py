from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import re
# 引入url解析库，可以在get请求里对端口后的数据进行解析
from urllib import parse
# 提供构建服务器功能
# D:\Py1809Project\Project\webpy\webpart\register.html
class RequestCallBack(BaseHTTPRequestHandler):
    # 处理get请求,关键字GET必须大写
    def do_GET(self):
        # 获得文件的完整路径
        # full_path=os.getcwd()+self.path.replace("/",'\\')

        # path = parse.urlparse(self.path).path
        print(self.path)

        full_path = "webpart" + self.path
        print(full_path)
        # query=parse.urlparse(self.path).query
        # print(query)
        # 需要返回页面
        if self.path=="/favicon.ico":
            return
        #文件路径
        if not os.path.exists(full_path):
            print("haha")
            return
        # 设置状态码
        self.send_response(200)
        # 添加头部数据,发送的响应头部,头部可以有很多
        self.send_header("Content-Type","text/html")  # text里的文本内容可能是html,json，plain或其他，这里指定是html
        # 结束头部数据
        self.end_headers()
        # 写入页面数据
        with open(full_path,"r",encoding="utf8") as f:
            self.wfile.write(f.read().encode("utf8"))
    # 处理Post请求,post大写
    def do_POST(self):
        print("POST请求收到了")
        print(self.rfile.read().encode("utf8"))
        # 需要返回页面
        result=self.rfile.read()
        # 设置状态码
        self.send_response(200)
        # 添加头部数据
        self.send_header("Content-Type", "text/html")
        # 结束头部数据
        self.end_headers()
        # 写入页面数据

    # 设置状态码

    # 设置状态信息

    # 设置请求头部


# 构建http服务器
saddr=("192.168.12.23",8989)
server=HTTPServer(saddr,RequestCallBack)

# 开启服务
server.serve_forever()
