# class Student:
#     """这是一个学生类"""
#     level=0
#     color="red"
#     def __init__(self,name,Age,exp):
#         self.name=name
#         self.Age=Age
#         self.exp=exp
#         self.level=Student.level
#     def dark(self):
#         print("Hello World",self.Age)
#     @classmethod
#     def St1(cls):
#         print(Student.__doc__)
#     @staticmethod
#     def st2(age):
#         print("well good",age)
#         if age<Student.Age:
#             return  age
#         else:
#             return 0
#
#
# # Student.St1()
# tim=Student('tim',12,2)
#
# tim.dark()
# Student.dark(tim)#类通常不会调用实例方法，调用时，要输入实例
#
#
# import types
# tim.fre=12
# print(tim.fre)
#
# Student.addr='newyork'
# print(Student.addr)
#
# def union(self,num):
#     print(num)
#     return "Earth fall"
#
# @classmethod
# def food(cls):
#     return "apple"
# @staticmethod
# def water():
#     print("waterslip")
#
# tim.unionfun=types.MethodType(union,tim)
# print(tim.unionfun(23))
#
# Student.water=water
# Student.water()
# tim.water()
# Student.food=food
# print(Student.food())
#
# del tim.unionfun
# print(tim.unionfun(23))
# # delattr(Student.food)
# print(Student.food())

#生成器

