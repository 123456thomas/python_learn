# 2，查找10个内建函数，

#complex创建一个复数，a.conjugate()将复数转为共轭复数
a=complex(2,6)
# print(a,a.conjugate(),a.__class__)

#all，any
# result=all([1,"s",3,4])#若可迭代对象每一个都不是空元素也不为0，且为真则返回True
# print(result)
# print(all({}))#迭代对象为空也返回真
# print(any({}))#迭代对象为空返回真假
# result11=all([1,"s","",4])
# result12=any([1,"s","",4])#有一个为真即为真
# print(result11,result12)


# compile得到一个匹配模型，然后用匹配模型去匹配
import re
from collections.abc import Iterator
partch=re.compile("rel")
result=partch.search("wertyrel")#得到一个对象
print(result,isinstance(result,Iterator))

#filter筛选器
def Func1(x):
    if x%3==0:
        return True
ret1=filter(Func1,[2,3,5,6,8,9,12,42,44])#可迭代对象里的元素是3的倍数则返回True,则加到迭代器里，最后返回一个迭代器
# for i in ret1:
#     print(i)
# print(ret1,isinstance(ret1,Iterator))

#map()投影函数,得到一个处理过的迭代器
ret2=map(lambda x:x*2+x**2,[1,2,3,4,5,6,7])
print(ret2,ret2.__class__,isinstance(ret2,Iterator))

while True:
    try:
        print(next(ret2))
    except StopIteration as e:
        print(e)
        break

#sorted()排序
ret3=[6.2,2,6.78,54,7.7,45]
ret31=sorted(ret3,reverse=1)#降序
ret32=sorted(ret3)          #升序
print(ret31,ret32)


#dir()#可以查看对象、类的属性
print(dir(ret3))

#reduce(),对序列处理后累加
from _functools import reduce
def Func2(x,y):
    return x+y
ret4=reduce(Func2,["a","b","c"])
print(ret4)
