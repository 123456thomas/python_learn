import math,random
import numpy as np
#数组的生成方法，和形状属性，重新定义形状
a=np.array([1,math.pi/2,3])
# print(np.sin(a))
# print(a>2)
# print(type(a),a.dtype,a.shape)

#重新定义形状
# b=a.reshape(1,-1)
# print(b,type(b),b.shape)
# b[0,2]=55
# print(a,type(a),a.shape)
# print(b,type(b),b.shape)

#基本矩阵
# c1=np.zeros((3,3))
# c2=np.ones((2,3))
# c3=np.full((4,4),6)
# c4=np.eye(5)
# c5=np.random.random((4,4))
# print(c1,c2,c3,c4,c5)
# e1=np.empty((3,3))

#矩阵的类型与内存、精度的关系，位数越大，越精确，
# 越占空间,其中的参数dtype=np.int64，可以强制转化元素数据类型（存储方式）。
# e2=np.array([[1,3,4,5],
#              [2,3,5,6],
#              [8,6,0,3]],dtype=np.int64)
# print(e2)
# print(type(e2),e2.dtype)

# f1=np.arange(12).reshape((4,3))
# print(f1,f1.dtype)
# #设起点和终点，分几份
# f2=np.linspace(0,10,6).reshape((2,3))
# print(f2,f2.dtype)

#提取矩阵元素
# f3=np.array([[1,4,6,8,9,5],
#              [4,7,9,0,2,1],
#              [5,23,1,5,7,0],
#              [10,1,3,5,12,5]])
# # b1=f3[-2:,3:5]
# # print(b1)
# c1=f3[3,3:5]
# c2=f3[3,4]
# print(c1,c2)

#算数运算，对应位置的加减乘除，开方np.sqrt(a)
# g1=np.array([[1,2],
#              [2,3]])
# g2=np.array([[2,1],
#              [3,4]])
# #矩阵的乘法g1.dot(g2)
# print(g1.dot(g2))

#常用函数
f3=np.array([[1,4,6,8,9,5],
             [4,7,9,0,2,1],
             [5,23,1,5,7,0],
             [10,1,3,5,12,5]])
# print("f3所有元素求和",np.sum(f3))
# print("f3同一列求和",np.sum(f3,axis=0))
# print("f3同一行求和",np.sum(f3,axis=1))

# print("f3所有元素平均值",np.mean(f3))
# print("f3同一列求平均值",np.mean(f3,axis=0))
# print("f3同一行求平均值",np.mean(f3,axis=1))

#uniform产生指定范围内一个随机数
# t=np.random.uniform(4,10)
# print(t)

#tile函数有产生指定范围数值的功能
# g1=np.array([[1,2],
#              [2,3]])
# print("在横向为2增加一个数组g1,纵向为1 不增加",np.tile(g1,(2,1)))
# print("在横向为3增加2个数组g1,纵向为2 增加1",np.tile(g1,(3,2)))

# print(np.random.uniform(4,120,[2,3,5]))

#矩阵的转置
# A=np.array([[2,4,6,1],[2,4,6,1]])
# print(A,A.shape)
# print(A.T,A.T.shape)

#np.clip()。限定元素区间
# sa=[[12,31,56,7,8],
#     [21,41,15,19,8]]
# sz=np.clip(sa,12,32)
# print(sa)
# print(sz)

#分割
sa1=np.arange(12).reshape((3,4))
# sa2=np.split(sa1,4,axis=1)
# print(sa2)

#np.array_split也可以进行不等项分割
# sa0=np.array_split(sa1,3,axis=0)
# print(sa0)

# sa3=np.vsplit(sa1,3)
# print(sa3)

# sa4=np.hsplit(sa1,2)
# print(sa4)