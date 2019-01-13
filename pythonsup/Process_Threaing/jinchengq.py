from multiprocessing import Queue,Process,ProcessError
# 线程池中导入队列要从Manage中导入
q = Queue(5)
# q.get()  # 默认阻塞操作,获取一个数据,若为空,则一直等
# q.get_nowait()  # 非阻塞操作
q.put(0)
print(q.qsize())
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.get()  # 取出一个
print(q.qsize())
# q.put(4,True,2) # 第一个参数为传入的值,第二个默认阻塞此时为True,第三个为等待时间,到时间直接放,过已满则报错
print(q.qsize())
q.put_nowait(7) # 非阻塞,直接放

# 多线程
import time
def prt(t):
    print("hello",t)
    time.sleep(1)
# start = time.time()
# for r in range(5):
#     prt()
#     end = time.time()
# print(end-start)

import threading
start1 = time.time()
for i in range(5):
    t=threading.Thread(target=prt,args=(i,))
    t.start()
# while True:
#     if t.is_alive()==False:
#         end1=time.time()
#         print("运行时间:",end1-start1)
#         break
# end1=time.time()
# print(end1-start1)