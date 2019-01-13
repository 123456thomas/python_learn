import socket,threading
from multiprocessing import Pool

def Read(cli):
    while True:
        result=cli.recv(1024)
        print(result,len(result))
        if len(result)==0:
            break
def Write(cli):
    while True:
        try:
            content=input("内容:")
            result=cli.send(content.encode("utf8"))
            print(result,len(result))
        except Exception as e:
            print(e)
def main():
    server=socket.socket()
    server.bind(("192.168.12.23",56000))
    server.listen(50)
    pool=Pool(50)
    while True:
        cli,adr=server.accept()
        p1 = pool.apply_async(Clien,args=(cli,))

def main1():
    server = socket.socket()
    server.bind(("192.168.12.23", 56000))
    server.listen(50)
    while True:
        cli, adr = server.accept()
        pr = threading.Thread(target=Read, args=(cli,))
        pw = threading.Thread(target=Write, args=(cli,))
        pr.start()
        pw.start()


if __name__ == '__main__':
    main1()