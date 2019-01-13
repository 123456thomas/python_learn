import random as r
import os
class Ai:
    def __init__(self,name,Hp=200,Hurt=5):
        self.name=name
        self.__Hp=Hp
        self.__Hurt=Hurt
    def AiCai(self,value):
        self.__Cai=value
        return self.__Cai
    def HP(self,obj):
        self.__Hp-=obj.__Hurt
        return self.__Hp
    def GetHp(self):
        return self.__Hp
    def __str__(self):
        return "%s,%s,%s" % (self.name, self.__Hp, self.__Cai)
class Player(Ai):
    def __init__(self,name,Hp=600,Hurt=15):
        super().__init__(name,Hp,Hurt)
#创建对象
# Ai1=Ai("小米")
# Ai2=Ai("小鹿")
# Ai3=Ai("小丁")
# Hero=Player("大力")
# # print(Ai1,Hero)
# #流程设计
# isGo=True
# while isGo:
#     t=r.randint(1,6)
#     WanC=int(input("请猜大小:\n(大:请输2；小:请输1)"))
#     while WanC not in [1,2]:
#         WanC = int(input("输入错误，请重新输入:\n(大:请输2；小:请输1)"))
#     Hero.AiCai(WanC)
#     s = 0
#     #1.猜大小，猜对的，有攻击权，若玩家猜对，则玩家有先手权（先执行）
#     if (Hero.AiCai(WanC)==1 and t<4) or (Hero.AiCai(WanC)==2 and t>3):
#         for i in [Ai1,Ai2,Ai3]:
#             if i.GetHp()>0:
#                 i.HP(Hero)
#             else:
#                 s+= 1
#                 if s == 3:
#                     isGo = False
#     for j in [Ai1,Ai2,Ai3]:
#         temp=j.AiCai(r.randint(1, 2))
#         if (temp==1 and t<4) or (temp==2 and t>3):
#             if Hero.GetHp()>0:
#                 Hero.HP(j)
#             else:
#                 isGo=False
#         print(j)
#     print(Hero)
#     print(t)





