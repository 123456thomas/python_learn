import threading
import time
num=0
def Func():
    global num
    for i in range(100):
        num+=1
        time.sleep(0.05)

# 创建线程
def main():
    global num
    for i in range(100):
        num+=1
        time.sleep(0.1)
    Thre=threading.Thread(target=Func)

    sta=time.time()
    Thre.start()
    # time.sleep(3)
    # print(num)
    while True:
        if Thre.is_alive()==False:
            # print(num)
            print("+++",time.time()-sta)
            break

# 死锁
def Func1b(mutex1,mutex2):
    global num
    while True:
        if mutex1.acquire():
            num+=2
            time.sleep(1)
            print("+")
            if mutex2.acquire():
                print("++")
def Func2b(mutex2,mutex1):
    global num
    while True:
        if mutex2.acquire():
            num += 2
            time.sleep(1)
            print("-")
            if mutex1.acquire():
                print("--")

def main2():
    global num
    num=1
    # 创建锁,并初始化所
    mutex1=threading.Lock()
    mutex2 = threading.Lock()

    # 主线程
    t1 =threading.Thread(target=Func1b,args=(mutex1,mutex2))
    t2 = threading.Thread(target=Func2b,args=(mutex2,mutex1))
    print(num)
    #开启线程
    t1.start()
    t2.start()
# 互斥锁的实现线程同步
def Func1(mutex1,mutex2):
    global num
    while True:
        if mutex1.acquire():
            num+=2
            time.sleep(1)
            mutex2.release()
def Func2(mutex2,mutex3):
    global num
    while True:
        if mutex2.acquire():
            num += 2
            time.sleep(1)
            mutex3.release()
def Func3(mutex3,mutex):
    global num
    while True:
        if mutex3.acquire():
            num += 2
            time.sleep(1)
            mutex.release()

def main1():
    global num
    num=1
    # 创建锁,并初始化所
    mutex=threading.Lock()
    mutex.acquire()  # 加锁
    mutex1=threading.Lock()
    mutex2 = threading.Lock()
    mutex2.acquire()  # 加锁
    mutex3 = threading.Lock()
    mutex3.acquire()  # 加锁

    # 主线程
    t1 =threading.Thread(target=Func1,args=(mutex1,mutex2))
    t2 = threading.Thread(target=Func2,args=(mutex2,mutex3))
    t3 = threading.Thread(target=Func3,args=(mutex3,mutex))
    print(num)
    #开启线程
    t1.start()
    t2.start()
    t3.start()
    if mutex.acquire():
        print(num)

# ThreadLocal线程内全局变量
def Func1c(tm):
    tm.num=3
    print(tm.num)
def Func2c(tm):
    tm.num =10
    print(tm.num)
def main3():
    Threalocal=threading.local()
    print(type(Threalocal),Threalocal)
    Threalocal.num=1  # 只在主线程赋值，不影响其他线程
    # 创建锁,并初始化所
    mutex=threading.Lock()
    mutex.acquire()  # 加锁
    mutex1=threading.Lock()
    mutex2 = threading.Lock()
    mutex2.acquire()  # 加锁

    # 主线程
    t1 =threading.Thread(target=Func1c,args=(Threalocal,))
    t2 = threading.Thread(target=Func2c,args=(Threalocal,))

    #开启线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(Threalocal.num)

if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    main3()
