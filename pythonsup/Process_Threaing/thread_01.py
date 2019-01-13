import threading,time

def Func1(m1,m2):
    if m1.acquire():
        time.sleep(1)
        print(0)
        m2.release()
def Func2(m1,m2):
    if m1.acquire():
        time.sleep(1)
        print(0)
        m2.release()

def Func3(m1,m2):
    if m1.acquire():
        time.sleep(1)
        print(0)
        m2.release()
def Func4(m1,m2):
    num=0
    while True:
        time.sleep(2)
        num+=1
        if E:
            break
    print(num)

Munex1=threading.Lock()
Munex2=threading.Lock()
Munex2.acquire()
Munex3=threading.Lock()
Munex3.acquire()
Munex4=threading.Lock()
Munex4.acquire()
t1=threading.Thread(target=Func1,args=(Munex1,Munex2))
t2=threading.Thread(target=Func2,args=(Munex2,Munex3))
t3=threading.Thread(target=Func3,args=(Munex3,Munex4))
t1.start()
t2.start()
t3.start()






