import socket,threading
from multiprocessing import Pool
# 构建服务端，用于多个客户端间的通信，发信息的格式为：首发为端口，之后与其建立连接，输入su?端口号 切换连接对象
users=[]
# 读取信息
def Read(cli,adr):
    try:
        resu = cli.recv(1024)
        tem = resu.decode("utf8")   # 端口号解码
        por=int(tem)                 # 初始聊天对象端口
        while True:
            try:
                result = cli.recv(1024)
                temp = result.decode("utf8")
                # 如果输入exit或关闭连接，则退出
                if len(result)==0 or temp=="exit":
                    for u in users:
                        if u["Port"][1]== adr[1]:
                            users.remove(u)
                            print(users)
                    break
                # 切换聊天对象
                elif temp[:3]=="su?":
                    por=int(temp[3:])
                # 执行发送信息的方法
                else:
                    Send(por,temp)
            except Exception as e2:
                print("e2",e2)
    except Exception as e4:
        print(e4)

def Send(port,content):
        try:
            for i in users:
                if i["Port"][1] == port:
                    i["Sort"].send(content.encode("utf8"))
        except Exception as e:
            print(e)

def main():
    server=socket.socket()
    server.bind(("192.168.12.23",56000))
    server.listen(50)
    while True:
        try:
            cli,adr=server.accept()
            users.append({"Port":adr,"Sort":cli})
            print(users)
            print(cli)
            th1 = threading.Thread(target=Read,args=(cli,adr))
            th1.start()
            over=input("end(y):")
            if over=="y":
                break
        except Exception as e1:
            print("e1:",e1)

if __name__ == '__main__':
    main()