
# 在linux中使用fork模块完成多进程，在windows用multiprocessing完成多进程


from  multiprocessing import Pool
import os,time
import requests
def fun(name, age, **kwargs):
    print("pid %d" % os.getpid(),os.getppid())
    print(name, age, kwargs)
    time.sleep(1)
def Imgload():
    with open(r"D:\Python_sup\20181123\zuoye11.23\kingworld_imgsrc.txt") as f:
        reader=f.read()
    lis=reader.split("\n")
    lis.pop()
    for t in lis:
        result=requests.get(t).content
        tm=t.rpartition("/")[-1]
        with open(r"D:\Python_sup\20181123\zuoye11.23\gsrc\%s"%(tm),"wb") as f1:
            f1.write(result)

def proload(t):
    result = requests.get(t).content
    tm = t.rpartition("/")[-1]
    with open(r"D:\Python_sup\20181123\zuoye11.23\gsrcl\%s" % (tm), "wb") as f2:
        f2.write(result)

import threading
# 多线程加载图片
class Threadmul(threading.Thread):
    def __init__(self,_url):
        super(Threadmul, self).__init__()
        self.url=_url
    def run(self):
        result = requests.get(self.url).content
        tm =self.url.rpartition("/")[-1]
        with open(r"D:\Python_sup\20181123\zuoye11.23\gsrcl\%s" % (tm), "wb") as f2:
            f2.write(result)

def main4():
    st1=time.time()
    with open(r"D:\Python_sup\20181123\zuoye11.23\kingworld_imgsrc.txt") as f4:
        reader=f4.read()
    lis=reader.split("\n")
    lis.pop()
    for k in lis:
        # 非阻塞式进程
        t=Threadmul(k)
        t.start()
    while True:
        if t.is_alive()==False:
            print("多线程费时%s"%(time.time()-st1))
            break

def main3():
    with open(r"D:\Python_sup\20181123\zuoye11.23\kingworld_imgsrc.txt") as f3:
        reader=f3.read()
    lis=reader.split("\n")
    lis.pop()
    pool = Pool(10)
    for k in lis:
        # 非阻塞式进程
        pool.apply_async(proload, (k,))
    # 停止池子的使用
    pool.close()
    pool.join()

def main():
    pool = Pool(5)
    for i in range(10):
        # 非阻塞式进程
        pool.apply_async(fun, ("zt", i), {"isalive": False})
    print("++++")
    # 停止池子的使用
    pool.close()
    pool.join()
    print("finish")

def main1():
    pool = Pool(5)
    pool.apply_async(fun, ("zt",1), {"isalive": False})
    for i in range(20):
        # 阻塞式,进程排队一个一个执行
        pool.apply(fun, ("zty", i), {"isalive": False})
    print("++++")
    print("finish")

if __name__ == '__main__':
    t1=time.time()
    # main3()
    # main()
    # Imgload()
    main4()
    print("timeout:%s"%(time.time()-t1))

