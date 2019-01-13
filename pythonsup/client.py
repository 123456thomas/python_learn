import socket,threading
def Sendto(clientsoc):
    global Nump
    while True:
        da = input("内容：\n")
        if da=="exit":
            clientsoc.close()
            return None
        clientsoc.sendto(da.encode("utf8"), ("192.168.12.23", 60000))  # 将发送内容转为字节
        print("已发送")
def Recv(clientsoc):
    clientsoc.sendto("".encode("utf8"), ("192.168.12.23", 60000))
    while True:
        try:
            result=clientsoc.recvfrom(1024)  # 是一个阻塞操作
        except:
            break
        try:
            content=result[0].decode("utf8")
        except Exception as e:
            content = result[0].decode("gbk")
        print(content)
        print("数据来源",result[1])

def main():
    clientsoc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    thr1=threading.Thread(target=Sendto,args=(clientsoc,))
    thr2=threading.Thread(target=Recv,args=(clientsoc,))
    thr1.start()
    thr2.start()


if __name__ == '__main__':
    main()