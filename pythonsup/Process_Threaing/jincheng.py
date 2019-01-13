import os,time
from multiprocessing import Process

def Fun1(*args,**kwargs1):
    """
    子进程的主函数
    :param args:
    :param kwargs1:
    :return:
    """
    print(args[0],args[1],kwargs1)
    # time.sleep(4)
    print(args[0],args[1], kwargs1)
    print("/////")
def main():
    # 查看主进程pid
    print("parent pid %d" % os.getpid())
    # 创建一个子进程
    p1=Process(
        name="child",
        target=Fun1,
        args=("ztp",24),
        kwargs={"alive":False})

    print(p1.is_alive())
    t1 = time.time()
    # 开启子进程
    p1.start()
    print("p1 name %s pid %d" % (p1.name, int(p1.pid)))  # 查看子进程名字和进程号
    # 主进程暂停2秒，若子进程还没完成，就终止子进程，继续运行主进程
    print(p1.is_alive())
    p1.terminate()  # 终止可能需要等待极端的时间,is_alive()才会转为false
    print("终止耗时：",time.time()-t1)
    time.sleep(0.003)
    print(p1.is_alive())
    # 等待子进程完成p1.is_alive变为false，再执行以下主进程
    p1.join()
    print("child finish")
    print("++++")

# 当__name__为__min__代表该文件为程序主入口,而非导入进来的文件模块
if __name__ == '__main__':
    main()



# def Func(name,i):
#     # print(args)
#     li.append(i)
#     print(name,li)
#     print(os.getpid(), os.getppid())
#
# li=[]
# if __name__ == '__main__':
#     # 利用循环语句创建多子个进程
#     for i in range(10):
#         p=Process(name="a%s"%(i),args=("a%s"%(i),i),target=Func)
#         p.start()
#         p.join(2)
#     print("end")

