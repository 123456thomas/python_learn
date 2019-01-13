# def Get(classname,partentclass,oriattrdict):
#     print(classname)
#     print(partentclass)
#     print(oriattrdict)
#     newattr={}
#     for k,v in oriattrdict.items():
#         if not k.startswith("__"):
#             key=classname.capitalize() + k
#             newattr[key]=v
#     return type(classname.capitalize(),partentclass,newattr)
#
# class humen(object,metaclass=Get):
#     name="zza"
#     Age=18
#     sex="man"
# h1=humen()
# print(getattr(humen,"Humenname"),h1.__class__)

import  sys
# a=10021
# print(sys.getrefcount(10021))
# b=a
# print(sys.getrefcount(10021))
# del a,b
# print(sys.getrefcount(10021))
# lis1=[1,2,3]
# lis2=["a","b"]
# print(sys.getrefcount([1,2,3]))
# print(sys.getrefcount(["a","b"]))
# print(sys.getrefcount("a"))
# lis1.extend(lis2)
# lis2.extend(lis1)
# print(sys.getrefcount([1,2,3]))
# print(sys.getrefcount(["a","b"]))
# print(sys.getrefcount("a"))
# lis11=lis1
# lis22=lis2
# print(sys.getrefcount([1,2,3]))
# print(sys.getrefcount(["a","b"]))
# print(sys.getrefcount("a"))
# del lis1
t1=complex(2, 4)
# print(t1,t1.__class__,t1.conjugate())
# print(dir(__builtins__))

#内置函数
def fun1(x):
    if x>40:
        return True
    else:
        return False
lisa=[23,56,31,82,24]
conno=filter(fun1,lisa)#得到一个迭代器,返回结果为True的相应值
# for i in conno:
#     print(i)


def Func1(x):
    return (bin(x),hex(x))
# for i in map(Func1,lisa):
#     print(i)
from _functools import reduce
def Func2(x,y):
    return x + y
tts=reduce(Func2,lisa)
print(tts,tts.__class__)
for i in sorted(lisa,reverse=0):
    print(i)