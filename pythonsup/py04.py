# 4，windows下使用跨平台模块 multiprocessing
# 编写多进程应用程序
# 结合getpid getppid（）方法编码验证父子进程id

from multiprocessing import Process
import os

def Fun2(j):
    print("pid21 %s,pid12 %s" % (os.getpid(), os.getppid()))
    print(j)
def Fun1(i,num):
    print("pid12 %s,pid1 %s"%(os.getpid(),os.getppid()))
    num+=2
    print(i,"num %s"%(num))
    # 在产生一个子进程
    p2=Process(target=Fun2,args=(13,))
    # 启动子进程
    p2.start()
    # join方法:子进程结束后，在执行下面的
    p2.join()
    print("KKKKK")


# 此处查看进程号

# 启动进程分裂
if __name__ == '__main__':
    num=0
    pid1 = os.getpid()
    print(pid1, "---")
    # 产生一个子进程
    p = Process(target=Fun1,args=(12,num))
    p.start()
    # 子进程结束后执行后续主进程
    p.join()
    print( "num %s" % (num))
    print("++++")