
# from collections.abc import Iterable,Iterator
#
# # tup=(2,4,6)
# # str1="adffg"
# # list1=["df","sr",2,34]
# # dic1={"df":23,"aw":43}
# # def FH(m):
# #     a=1
# #     count=1
# #     while count<=m:
# #         m+=a
# #         yield m
# # g1=FH(10)
#
# # print(isinstance(tup,Iterable),next(tup))
# # print(isinstance(str1,Iterable))
# # print(isinstance(list1,Iterable))
# # print(isinstance(dic1,Iterable))
# # print(isinstance(g1,Iterable),next(g1))
# # print("===")
# # print(isinstance(tup,Iterator))
# # print(isinstance(str1,Iterator))
# # str2=iter(str1)
# # print(isinstance(str2,Iterator))
# # print(next(str2))
# # print(next(str2))
# # print(next(str2))
# # for i in str2:
# #     print(i)
# # for i in str2:#迭代器似乎会记录迭代的位置
# #     print(i)
# # try:
# #     print(next(str2))
# #     print(next(str2))
# #     print(next(str2))
# #     print(next(str2))
# #     print(next(str2))
# #     print(next(str2))
# #     for i in str2:
# #         print(i)
# # except StopIteration as e:
# #     print(e)
# # print(isinstance(list1,Iterator))
# # print(isinstance(dic1,Iterator))
# # print(isinstance(g1,Iterator))
#
#
# #闭包
# # temp=12
# # def fun1(a):
# #     def fun2(b):
# #         return (a+b)
# #     return fun2
# # r1=fun1(3)
# # r2=r1(4)
# # print(r1)
# # print(r2)
#
#
# #装饰器
# def check(f):#装饰器
#     def func():
#         name=input()
#         if name=="zzt":
#             f()#调用被装饰的函数
#         else:
#             print("无权限")
#     return func
#
# @check
# def Selectgo():#被装饰的函数
#     print("++++")
#
# @check
# def Selprice():
#     temp = [1,2,3,4,5]
#     print(temp)

# Selectgo()
# Selprice()

import time
def check(f):
    def func():
        sta=time.time()
        f()
        end=time.time()
        print(end-sta)
    return func
@check
def Sun():
    for i in range(0, 1001):
        for j in range(0, 1001):
            if i ** 2 + j ** 2 == (1000 - j - i) ** 2:
                print(i, j, 1000 - i - j)
            if i>500 and j>500:
                break

# Sun()

#复制、浅拷贝、深拷贝
# list1=[1,2,3,[3,4],5]
# # list11=list1[:]#相当于浅拷贝
# # list2=list1
# # print(id(list11),id(list1))
# # print(id(list11[3]),id(list1[3]))
# # # print(id(list2),id(list1))
# # # print(id(list2[3]),id(list1[3]))
# # print("++++++++++++++++++++++++++++++++++")
# # import copy
# # list3=copy.copy(list1)
# # print(id(list3),id(list1))
# # print(id(list3[3]),id(list1[3]))
# # list4=copy.deepcopy(list1)
# # print(id(list4),id(list1))
# # print(id(list4[3]),id(list1[3]))

#进制转换
# print(bin(100))
# print(hex(0b100))
# print(bin(0o700))
# print(int(0x3))

#元类创建类
def Num(self):
    print("++++")
def Num2(self,a,b):
    self.name=a
    self.color=b
@classmethod
def Num3(cls):
    """这是个剑法"""
    print("-----")
    return cls.__doc__
@staticmethod
def Num4():
    print("吃过了")

Human1=type("Human",(object,),{"heigh":179,"weight":70,"nmumfun":Num,"numf1":Num2})#第二个参数为元组末尾跟逗号
print(Human1,type(Human1),Human1.__class__)
h1=Human1()
print(h1,type(h1),h1.__class__.__class__)
h1.numf1(2,5)#对象属性
People1=type("People",(Human1,),{"Age":17,"name":"tt"})
print(People1,type(People1),People1.__class__)
p1=People1()
print(p1,type(p1),p1.__class__)

print(h1.heigh,h1.name)
print(Human1)

