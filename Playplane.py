import os,sys,json,random,math
import pygame
#游戏分解
# 登录界面：登录、注册、退出
# 游戏菜单界面：游戏模式（难易程度，记分制、记时制）、
#     查看历史最高分选项，背景音乐选择，退出界面
# 游戏进行界面：
#     主角：血量、特技
#     敌机：种类、血量
#     奖励：
#     子弹：
# 游戏结束界面：显示得分和最高记录，显示再来一次选项，否则回到游戏开始界面
#1.登录界面
#1.1服务器数据库
Users={"Tim":["666666","0","0"]}

# 数据写入服务器
def CreatUserDates(users,path0="playplaneKK"):
    if not os.path.exists(path0):
        os.mkdir(path0)
    temp=os.path.join(path0,"Playplane.json")
    with open(temp,"w",encoding="utf-8") as f_w:
        json.dump(users,f_w)
if not os.path.exists("playplaneKK"):
    CreatUserDates()
#读取数据
def ReadDates(path0="playplaneKK"):
    temp = os.path.join(path0, "Playplane.json")
    with open(temp,"r",encoding="utf-8") as f_r:
        return json.load(f_r)
#登录界面
def Login():
    s=3
    Reading=ReadDates()
    name=input("用户名：")
    pwd=input("密码（数字）：")
    try:
        while True:
            if name in Reading.keys():
                if int(pwd)==int(Reading[name][0]):
                    print("登录成功")

                    return True
            else:
                print("用户名或密码错误\n还有%s次机会"%(s))
                if s==0:
                    print("登录失败")
                    return False
                name = input("用户名：")
                pwd = input("密码：")
                s -= 1
    except Exception as e:
        print(e)
#注册方法
def Register():
    Reading = ReadDates()
    s=3
    name = input("用户名：")
    pwd = input("密码（6位数字）：")
    while True:
        if name not in Reading.keys():
            if len(pwd) == 6 and pwd.isdigit():
                print("注册成功")
                Reading[name]=[pwd,"0","0"]
                CreatUserDates(Reading, path0="playplaneKK")
                return True
            else:
                print("密码格式错误")
                t = input("是否继续注册（y/n）")
                if t == "n":
                    print("注册失败")
                    return False
                pwd = input("密码：")
        else:
            print("该用户名已存在" )
            t=input("是否继续注册（y/n）")
            if t== "n":
                print("注册失败")
                return False
            name = input("用户名：")
            pwd = input("密码：")
def main():
    while True:
        s=input("欢迎来到Planeplay，请选择\n"
                "1.登录；2.注册；3.退出")
        if s=="1":
            Login()
        elif s=="2":
            Register()

        elif s=="3":
            break
        else:
            print("输入错误")

if __name__ == '__main__':
    main()