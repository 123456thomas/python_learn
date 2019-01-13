import socket,threading



def Send(client):
    while True:
        addr=input("内容")
        if addr=="exit":
            client.close()
            break
        client.send(addr.encode("utf8"))
def Rev(client):
    while True:
        try:
            resul=client.recv(1024)
            print(resul.decode("utf8"))
        except Exception as e:
            print(e)
            break

def main():
    client = socket.socket()
    client.connect(("192.168.12.23", 60000))
    t1 = threading.Thread(target=Send,args=(client,))
    t2 = threading.Thread(target=Rev, args=(client,))
    t1.start()
    t2.start()

# if __name__ == '__main__':
#     main()


list1=[1,3,5,7,8,9,6,4,3,"end"]

for i in list1:
    print(i)

for u in list1:
    print(u)