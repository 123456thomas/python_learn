# 1.创建一个学员类，并设计三个字段用于表示学生的成绩 （语文、数学、英语）；
# 然后定义一个列表list表示一个班 的学生（10人），依次输入每个学生的信息和成绩，
# 输入 的同时将学员的每科成绩划分等级（100-90：A 89-80： B 79-70：C 69-60：D 60以下：E）
# 最后输出所有学员的 信息
# 2.编一个关于求多个某门功课总分和平均分的程序。
# 1.每个学生信息包括姓名和某门功课成绩。
# 2.假设5个学生。  3.类和对象的处理要合理
# 3.设计一个游戏角色类
# 字段:角色名、血量、魔法、状态   方法:释放技能 被伤害   要求:设计要合理
import random,math
#任务1
class StudentScore:
    def __init__(self,name,chinese,math_,english):
        self.name=name
        self.chinese=chinese
        self.math_=math_
        self.english=english
    def CheGrade(self,score):
        if 90<=score<=100:
            return "A"
        elif 80<=score:
            return "B"
        elif 70<=score:
            return "C"
        elif 60<=score:
            return "D"
        elif 0<=score:
            return "E"
        else:
            print("输入错误")
    def AllLevel(self):
        yul=self.CheGrade(self.chinese)
        mal= self.CheGrade(self.math_)
        enl= self.CheGrade(self.english)
        return {"语文":yul,"数学":mal,"英语":mal}
# listA=list("qwrtyuopkj")
# DictA={}
# for i in range(len(listA)):
#     x=i
#     y=random.randint(0,100)
#     z=random.randint(0,100)
#     m=random.randint(0,100)
#     listA[i]=StudentScore(x,y,z,m)
#     DictA[listA[i].name]=listA[i].AllLevel()
# print(DictA)
#任务2
class StuSubs:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def Subs(self,Ard):
        sublist = "科目:"
        for i in Ard.keys():
            sublist+=i
        return sublist
class Subcore:
    def __init__(self,name,Ard):
        self.name=name
        self.Ard=Ard
    def SumAver(self):
        Sum_ = 0
        Aver_ = 0
        for i in self.Ard.keys():
            Sum_ +=self.Ard[i]
        Aver_=Sum_/len(self.Ard)
        return {self.name:{"总分":Sum_,"平均分":"%0.2f"%Aver_} }
dictA={}
listcore=[]
listsub=[]
s=0
while True:
    name=input("请输入姓名")
    age=input("请输入年龄：")
    gender= input("请输入性别：")
    subss1=input("请输入学科（，隔开）")
    subss=subss1.split("，")
    for i in range(len(subss)):
        temp=int(input("请输入%s成绩"%subss[i]))
        dictA[subss[i]]=temp
    print(dictA)
    listcore.append(name)
    listsub.append(name)
    listcore[s]=Subcore(name, dictA)
    print(listcore[s].Ard)
    listsub[s]=StuSubs(name, gender, age)
    t=input("是否继续输入(y/n)")
    if t=="n":
        break
m=input("请选择要查看的科目")
Summ=0
y=0
for k in range(len(listsub)):
    print(listsub[k].Subs(listcore[k].Ard))
    if m in listsub[k].Subs(listcore[k].Ard):
        y+=1
        Summ+=listcore[k].Ard[m]
print("%s的总成绩:%s,平均成绩:%0.2f"%(m,Summ,Summ/y))
# n=input("请选择要查看的学生")
# for l in listsub:
#     if n==l.name:
#         print(name,l.Subs(listcore[listsub.index(l)]),listcore[listsub.index(l)].SumAver())








#         return {"总成绩%":Sum_,"平均成绩":"%0.2f"%Aver_}
# listC=[0,1,2,3,4]
# DictB={}
# for i in range(len(listC)):
#     Name=input("请输入姓名：")
#
#     yuwen=random.randint(0,100)
#     shuxue=random.randint(0,100)
#     wuli =random.randint(0,100)
#     listC[i]=Stucore(Name,yuwen,shuxue,wuli)
#     DictB[listC[i].name]=listC[i].SumAver()
# print(DictB)

#任务3
class Gamecc:
    def __init__(self,Name,Hp=1000,Mp=100,Bf=random.randint(-20,100)/50):
        self.Name=Name
        self.Hp=Hp
        self.Mp=Mp
        self.Bf=Bf
    def Attack(self,obj):
        jigong=100
        Allattack=jigong+self.Bf*self.Mp
        obj.Hp-=Allattack
        print("%s被打掉%s点血，还剩%s"%(obj.Name,Allattack,obj.Hp))
# Wolf=Gamecc("Wolf")
# Hero=Gamecc("Hero")
# while True:
#     if random.randint(0,10)%2==1:
#         Hero.Attack(Wolf)
#     else:
#         Wolf.Attack(Hero)
#     if Wolf.Hp<=0 or Hero.Hp<=0:
#         break
# 1：创建一个圆Circle类，为该类提供两个方法，方法一用 于求圆的面积，方法二用于求圆的周长，同时为该类提供 一个变量r表示半径，一个变量PI表示圆周率。为该类提供 一个魔法方法，用于初始化属性的值
class CircieMath:
    def __init__(self,r,pi=3.14):
        self.r=r
        self.pi=pi
    def CircleArea(self):
        return "面积：%s"%(self.pi*self.r**2)
    def CircleGirth(self):
        return "周长：%s"%(self.pi*self.r*2)
# x=CircieMath(3)
# print(x.CircleArea(),x.CircleGirth())
# 2：（1）创建Rectangle类，添加属性width、height；
# （2）在Rectangle类中添加两种方法计算矩形的周长和面 积；
# （3）编程利用Rectangle输出一个矩形的周长和面积
def Area(width=0,height=0):
    return "面积:%s"%(width*height)
def Girth(width=0,height=0):
    return "面积:%s"%(width+height)*2
class Rectangle:
    pass
# y=Rectangle()
# y.Fun=Area
# y.fin=Girth#不加括号
# y.width=3
# y.height=6
# print(y.Fun(y.width,y.height),y.fin(y.width,y.height))
# DictA={"a":3,"b":6,"c":9}
# for i in DictA.keys():
#     print(i,DictA[i])
# print(DictA.keys())
# DictB={}
# print(DictB.fromkeys("sdfghj"))

