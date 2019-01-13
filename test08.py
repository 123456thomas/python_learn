#
# 1、根据一个用户指定的行数打印斐波那契数的图形
# （1,1,2,3,5,8,13,21.......），那么最终在控制台输出如下图形
#
# *
# *
# **
# ***
# *****
# ********
# *************
#
# 2、创建一个长度为10的整型列表，并且用大于等于1且小于等于10的随机数初始化
# 这个整型列表且列表内的数值不可重复。
#
# 3、公鸡一只5元，母鸡一只3元，小鸡三只1元。现在要拿100元买100只鸡，
# 请问公鸡、母鸡、小鸡各几只?
#
# 4、计算一个字符串有几个子串？例如字符串"abc",就包含
# "a","b","c","ab","bc","abc"6个子串。
#
# 5、编写方法，接收一个表示上限的参数n，打印出0到n内能够被3整除的所有偶数。
#
# 6、编程求一个四位自然数ABCD,它乘以A后变成DCBA。
#
# 7、求100以内跨度最大的相邻的一对质数。
#
# 8、实现账号注册和账号登陆，需要使用外置文件存储数据。账号属性为：名字，
# 年龄，性别，邮箱，地址，密码
#
#
# 9、输入一个日期，格式如：2010 10 24 ，打印输出为【2010年10月24日】，
# 并输出这一天是这一年中的第几天，是星期几？。
#
#
# 10、	有n盏灯,放在一排,从1到n依次顺序编号.有m个人也从1到m依次顺序编号.
# 第1个人（1号）将灯全部关闭；第2个人（2号）将凡是2的倍数的灯打开；
# 第3个人（3号）将凡是3的倍数的灯作相反处理（该灯如是打开的,则将它关闭；
# 如是关闭的,则将它打开）.以后的人都和3号一样,将凡是自己编号倍数的灯
# 作相反处理.试计算当第m个人操作后,哪几盏灯是亮的?
#
# 11、
# 编写武器类，
# a)	字段:名称、攻击力、重量。字段皆为私有变量
# b)	为该类编写三个构造函数，用于初始化
# c)	为该类每个字段添加属性，对字段进行封装
# d)	为该类添加方法WeaponInfo,显示武器的所有信息，格式如下：
# 1.	宝剑的攻击力为 100，重量为1000 g
# 2.	手枪的攻击力为 500，重量为600 g
# e)	实例化5个武器，并依次执行WeaponInfo方法
#
# 12、
# 编写健身器类
# a)	字段：名称、价格、是否是电力驱动。皆为受保护类型
# b)	方法:
# i.	Use()无参无返回值，负责打印“被使用中”
# ii.	Info()无参无返回值，负责打印设备的所有信息
# c)	编写跑步机类，在构造函数中修改默认为电力驱动
# i.	Use方法，打印“跑步机被使用中”
# ii.	添加字段：品牌
# d)	编写哑铃，编写Use方法，打印“哑铃被使用中”
#
# 13、
# 写一个Ticket类,有一个距离属性(本属性只读,在构造方法中赋值),不能为负数,
# 有一个价格属性,价格属性只读,并且根据距离计算价格(1元/公里):
# 0-100公里        票价不打折
# 101-200公里    总额打9.5折
# 201-300公里    总额打9折
# 300公里以上    总额打8折
# 有一个方法,可以显示这张票的信息.
# 测试上面的类.
#
# 14、
# 创建一个玩家类，玩家有名称、生命值、魔法值、攻击力、生存状态5个属性；
# 生命值、魔法值、攻击力、生存状态属性都是只读的；生命值、魔法值、攻击力
# 的初值分别为800、100、50；玩家类有一个攻击方法：Attack(Player player)。
# 玩家类有两个子类：野蛮人和魔法师。野蛮人每次攻击造成的伤害在[攻击力-10]
# 到[攻击力+10]之间（这个伤害值是一个随机值），另外野蛮人有一个被动技能
# （不消耗魔法），有25%的几率产生1次暴击（每4次攻击随机产生1次暴击），
# 每次暴击产生的伤害是原来的3倍；魔法师每次攻击造成的伤害在攻击力的80%~100%
# 之间（也是一个随机数），魔法师每次攻击消耗18点魔法，它会额外减少对方12%的
# 生命值。现在分别创建一个野蛮人、魔法师对象，让他们进行PK，就是你打我一下，
# 我打你一下，直到有一方死亡为止；野蛮人先攻击。
import random,time,os,json,math
########################第 1 题#############################
class Tuxing:
    def __init__(self,num) -> None:
        self.num=num
    def Fibo(self):
        list1=[]
        a=b=1
        if self.num>2:
            for i in range(0,self.num):
                if i in [0,1]:
                    temp=1
                    list1.append(temp)
                else:
                    temp=list1[i-1]+list1[i-2]
                    list1.append(temp)
        return list1
# a=Tuxing(7)
# t=a.Fibo()
# for i in t:
#     print("*"*i)
##############################第 2 题###########################

# import random
# list1=list(range(1,11))
# for i in range(len(list1)):
#     t=random.randint(1,10)
#     if i==0:
#         list1[0]=t
#     elif t not in list1[0:i]:
#         list1[i] = t
# print(list1)
###########################第 3 题######################3

# for i in range(0,20):#求公鸡
#     for j in range(0,33):#求母鸡
#         for z in range(0,300):#求小鸡
#             if i+j+z==100 and 5*i+3*j+z/3==100:
#                 print("买%s只公鸡，%s只母鸡，%s只小鸡"%(i,j,z))
#########################第 4 题##########################

# def GetsubNum(strA):
#     sum=0
#     for i in range(1,len(strA)+1):
#         sum+=i
#     return sum
# print(GetsubNum("abdfhj"))

#########################第 5 题##########################
# def Get32(n):
#     list2=[]
#     for i in range(n+1):
#         if i%3==0 and i%2==0:
#             list2.append(i)
#     return list2
# a=Get32(100)
# print(a)

#########################第 6 题##########################
# for a in range(1,10):
#     for b in range(0, 10):
#         for c in range(0, 10):
#             for d in range(0, 10):
#                 if (a*1000+b*100+c*10+d)*a==d*1000+c*100+b*10+a:
#                     print(a*1000+b*100+c*10+d)

#########################第 7 题##########################

# def GetPrime(Num):#得到一个素数列表
#     listA=[2]
#     for i in range(3,Num+1):
#         p=len(listA)
#         for j in range(0,p):
#             if i%listA[j]==0:
#                 break
#             if j==p-1:
#                 listA.append(i)
#     return listA
# x=GetPrime(100)
# temp=0
# for i in range(len(x)-1):
#     if x[i+1]-x[i]>temp:
#         a=[x[i],x[i+1]]
# print(a)

#########################第 8 题##########################
# class Account:
#     def __init__(self,name,dwg,age=18,gender="男",email="",adress=""):
#         self.Name=name
#         self.Age=age
#         self.Dwg=dwg
#         self.gender=gender
#         self.email=email
#         self.adress=adress
#     @property
#     def Name(self):
#         return self.__name
#     @Name.setter
#     def Name(self,value):
#         self.__name=value
#     @property
#     def Age(self):
#         return self.__age
#     @Age.setter
#     def Age(self, value):
#         self.__age=value
#     @property
#     def Dwg(self):
#         return self.__dwg
#     @Dwg.setter
#     def Dwg(self, value):
#         self.__dwg = value
#     pass
# a=Account("张三","123456",22)
# account={a.Name:[a.Dwg,a.Age,a.gender,a.email,a.adress]}
# def CreDefauluser(path="Account.json"):
#     global account
#     if not os.path.exists(path):
#         temp=account
#         with open(path,"w",encoding="utf-8") as f_w:
#             json.dump(temp,f_w)
# CreDefauluser()
# def Readuser(path="Account.json"):
#     if os.path.exists(path):
#         with open(path,"r",encoding="utf-8") as f_r:
#             return json.load(f_r)
# x=Readuser(path="Account.json")
# # print(x)
# def Updateuser(name,dwg,age=18,gender="男",email="",adress="",path="Account.json"):
#     if os.path.exists(path):
#         temp=Readuser(path)
#         tem=Account(name,dwg,age,gender,email,adress)
#         temp[tem.Name]=[a.Dwg,a.Age,a.gender,a.email,a.adress]
#         with open(path,"w",encoding="utf-8") as f_w:
#             json.dump(temp,f_w)
#
# def Login(path="Account.json"):
#     s=0
#     while True:
#         user = input("请输入用户名：")
#         userpwd = input("请输入密码：")
#         temp=Readuser(path)
#         if user in temp :
#             if temp[user][0]==userpwd:
#                 print("登陆成功")
#                 return True
#         s+=1
#         if s==3:
#             print("多次登录失败,请重新注册")
#             return False
#         print("登录失败,请重新登录")
# def Regeister(path="Account.json"):
#     temp= Readuser(path)
#     while True:
#         isGo=True
#         user= input("请输入用户名：")
#         dwg= input("请输入6-12位密码：")
#         age= input("请输入年龄：")
#         gender = input("请输入性别：")
#         emil = input("请输入邮箱：")
#         adress = input("请输入地址：")
#         if user in temp:
#             print("该用户已存在，请重新注册")
#             isGo = False
#             continue
#         if isGo and len(dwg) in range(6,13):
#             print("注册成功")
#             username=user
#             userPwd=dwg
#             Updateuser(username, userPwd,age,gender,emil,adress,path="Account.json")
#             return True
# def main():
#     while True:
#         x=int(input("欢迎来到BoBocc,请选择\n 1.登录；2.注册，3.退出"))
#         if x==1:
#             Isgo=Login()
#             if Isgo:
#                 print("登录成功")
#         elif x == 2:
#             Regeister(path="Account.json")  # 注册
#         elif x == 3:
#             break
#         else:
#             print("输入错误，请重新输入")
#     main()
# main()

#########################第 9 题##########################
# t=input("请输入一个日期如:2010 10 24")
# import calendar,datetime,time
# a=t.split(" ")
# x=time.strptime(t,"%Y %m %d")
# m=time.strftime("%Y{0}%m{1}%d{2}",x).format("年","月","日")
# t=calendar.monthrange(int(a[0]),int(a[1]))
# print(m)
# print(x)
# print("这天是一年中第%s天，今天是周%s"%(x[-2],int(x[-3])+1))

#########################第 10 题##########################

#########################第 11 题##########################
# class Guns:
#     def __init__(self,name,hurt,g) -> None:
#         self.Name=name
#         self.Hurt=hurt
#         self.Kmg=g
#     @property
#     def Name(self):
#         return self.__name
#     @Name.setter
#     def Name(self,value):
#         self.__name=value
#     @property
#     def Hurt(self):
#         return self.__hurt
#     @Hurt.setter
#     def Hurt(self, value):
#         self.__hurt = value
#
#     @property
#     def Kmg(self):
#         return self.__kmg
#     @Kmg.setter
#     def Kmg(self, value):
#         self.__kmg = value
#     def WeaponInfo(self):
#         print("名字：%s，攻击力：%s，重量%s"%(self.__name,self.__hurt,self.__kmg))
# a=Guns("手枪",500,600)
# b=Guns("宝剑",100,1000)
# a.WeaponInfo()
# b.WeaponInfo()
# b1=Guns("宝剑1",100,1000)
# b2=Guns("宝剑2",120,1000)
# b3=Guns("宝剑3",130,1000)
# b4=Guns("宝剑4",140,1000)
# b5=Guns("宝剑5",150,1000)
# for i in [b1,b2,b3,b4,b5]:
#     i.WeaponInfo()

#########################第 12 题##########################
# class JianQi:
#     def __init__(self,name,price,t=True):
#         self._name=name
#         self._price=price
#         self._t=t
#     def Use(self):
#         print("%s被使用中"%self._name)
#     def Info(self):
#         print(self._name,self._price,self._t)
# class Runman(JianQi):
#     def __init__(self, name, price,Gend,t=True):
#         super().__init__(name, price, t)
#         self.Gend=Gend  #品牌
#     def Use(self):
#             print("跑步机被使用中")
# z=JianQi("哑铃",100)
# z.Use()

#########################第 13题##########################
class Ticket:
    def __init__(self,distance):
        self.__SetDistance(distance)
        self.__SetPrice(distance)
    def __SetDistance(self,value):
        if type(value) in (int,float) and value>=0:
            self.__distance=value
        else:
            print("距离输入错误")
    def GetDistance(self):
        return self.__distance
    def __SetPrice(self,value):
        if value<=100:
            self.__price=value*1
        elif value<=200:
            self.__price=value*1*9.5
        elif value<=300:
            self.__price=value*1*9.0
        elif value>300:
            self.__price=value*1* 8.0
        else:
            print("距离输入错误")
    def GetPrice(self):
        return self.__price
    def __str__(self):
            return "距离：%s,票价:%s"%(self.__distance,self.__price)
# a=Ticket(50)
# b=Ticket(150)
# c=Ticket(250)
# d=Ticket(350)
# e=Ticket(-50)
# print(a,b,c,d,e)

#########################第 14题##########################
class Player:
    def __init__(self,name,state="live",hp=800,mp=100,hurt=50):
        self.Name=name
        self.__hp=hp
        self.__mp=mp
        self.__hurt=hurt
        self.__state=state
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name = value
    def Gethp(self):
        return self.__hp
    def Getmp(self):
        return self.__mp
    def Gethurt(self):
        return self.__hurt
    def Getstate(self):
        return self.__state
    def Attack(self,obj):
        if type(obj)==Magician:
            temp = self.__hp
            if obj.__mp>=18:
                obj.__mp-=18
                self.__hp=self.__hp*(1-0.12)-obj.Gethurt()*random.randint(80, 100)/100
                lip=temp-self.__hp
                print("%s对%s造成%s点伤害"%(obj.Name,self.Name,lip))
            else:
                lip=obj.Gethurt()*random.randint(80, 100) / 100
                self.__hp-=lip
                print("%s对%s造成%s点伤害" % (obj.Name, self.Name, lip))
                print("魔法不足，普通攻击")
        else:
            if random.randint(1, 4)==2:
                lip=(obj.Gethurt()-10+random.randint(0, 20))*3
            else:
                lip=obj.Gethurt()-10+random.randint(0, 20)
            self.__hp-=lip
            print("%s对%s造成%s点伤害" % (obj.Name,self.Name,lip))
    def State(self):
        if self.__hp<=0:
            self.__state=="Die"
    def __str__(self):
        return "%s的剩余血量：%s,魔法值：%s"%(self.__name,self.__hp,self.__mp)
class Barbarian(Player):
    def __init__(self, name, state="live", hp=800, mp=100, hurt=50):
        super().__init__(name, state, hp,mp,hurt)

class Magician(Player):
    def __init__(self, name, state="live", hp=800, mp=100, hurt=50):
        super().__init__(name, state, hp,mp,hurt)

#############################################################################
# Mag=Magician("Hero")
# Bar=Barbarian("小恶魔")
# Mag.Attack(Bar)
# Bar.Attack(Mag)
# t=Bar.Sethurt
# print(Bar.Gethurt(),Bar.Gethp())
# print(Mag.Getmp(),Mag.Gethurt(),Mag.Gethp())
# while True:
#     if Mag.Gethp()>0 and Bar.Gethp()>0:
#         Mag.Attack(Bar)
#         print(Mag)
#         print(Bar)
#     else:
#         break
#     if Mag.Gethp()>0 and Bar.Gethp()>0:
#         Bar.Attack(Mag)
#         print(Mag)
#         print(Bar)
#     else:
#         break


# import datetime,time
# t1 = datetime.datetime.now()
# time.sleep(5)
# t3 = datetime.datetime.now()
# time.sleep(5)
# t4 = datetime.datetime.now()
# time.sleep(5)
# t2 = datetime.datetime.now()
# list2 = [t1, t2, t3, t4]
# list3 = list2.sort(reverse=True)
# # dt = 24*60*60.0
# # t4 = t1 + datetime.timedelta(days=-3)  # 时间运算
# # print(t2 -t1)
# print(list2)
# print(list3)

# 列表是可变的数据类型
# class Auto:
#     name=[]
# a1 = Auto()
# a2 = Auto()
# a1.name.append(1)
# print(a1.name)
# print(a2.name)
# print(Auto.name)

# 元类
# class ObjectCreator(metaclass=Fate):
#     __metaclass__=Fate


# 列表推导式
# sli1=[[i,9] for i in "asdwewefuia"]
# dic1 = {x: y for (x,y) in sli1}
# print(dic1)
num=4

# print(str(num).zfill(4))

# 时间字符串
# import time
# t1= time.localtime()
# print(t1)
# times = time.strftime("%Y-%m-%d %H:%M:%S", t1)
# print(times)



# 字符串的插入：
# tes1 = [1,4,6,7,9,"r"]
# tes2 = tes1[:3]+[2,4,5,2]+tes1[3:]
# print(len("12你好  ".strip()))
def gento(ret):
    for i in range(10):
        ret+=1
        yield ret
        time.sleep(1)
f2 = gento(12)

lis = ["wrr.jpg","wet1.jpg",'er45.jpg']

# def fun2(x):
#     y = x.split(".jpg")[0]
#     return y
# lis2 = map(fun2,lis)
# print(lis2)
# for i in lis2:
#     print(i)



















































































































































































































































































































































































































