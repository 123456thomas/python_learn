import socket,threading,time
# 编写线程类
class Threcli(threading.Thread):
    def __init__(self):
        super().__init__()
    def rev(self):
        pass
    def send(self):
        pass
    def run(self):
        pass
IsGo=True

def Send(client,Munex1):
    while True:
        try:
            addr=input("内容")
            if addr=="exit":
                client.close()
                break
            client.send(addr.encode("utf8"))
        except Exception as e:
            print(e)
            break
def Rev(client,Munex1):
    global IsGo
    while True:
        try :
            resul=client.recv(1024)
            print(resul.decode("utf8"))
        except Exception as e:
            print(client)
            print(e)
            client.close()
            break

def main():
    try:
        server=socket.socket()
        server.bind(("192.168.12.23",60000))
        server.listen(50)
        cli=server.accept()
        print(cli)
        # 创建线程
        t1 = threading.Thread(target=Send,args=(cli[0],Munex1))
        t2 = threading.Thread(target=Rev, args=(cli[0],Munex1))
        t1.start()
        t2.start()
    except Exception as e1:
        print("e1%s"%e1)

if __name__ == '__main__':
    main()