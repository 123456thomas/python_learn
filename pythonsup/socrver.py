import socket,threading
def Sendto(serve):
    while True:
        try:
            da = input("内容：\n")
            if da=="exit":
                serve.close()
                break
            serve.sendto(da.encode("utf8"), Read)  # 将发送内容转为字节
        except Exception as e:
            print(e)
def Recv(serve):
    global Read
    while True:
        try:
            result=serve.recvfrom(1024)  # 是一个阻塞操作
            content=result[0].decode("utf8")
        except Exception as e:
            break
        Read=result[1]
        print(content)
Read=None
def main():
    serve=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serve.bind(("192.168.12.23",60000))
    thr1 = threading.Thread(target=Sendto, args=(serve,))
    thr2 = threading.Thread(target=Recv, args=(serve,))
    thr2.start()
    thr1.start()
if __name__ == '__main__':
    main()


