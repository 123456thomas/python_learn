import sys,json,os,random,time
from datetime import datetime
#老数据库
UserKu={"User":[{"username":"admin","userPwd":"666666"}]}
# #创建文章库
def CreArticle(username,path="Article"):
    if not os.path.exists(path):
        tempArticle={"Article":[
            {"title":"Today",
             "author":"admin",
             "time":datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"),
             "content":"It's time,son"}
        ]}
        os.mkdir(path)
        tempPath=os.path.join(path,"admin.json")
        with open(tempPath,"w",encoding="utf-8") as f_w:
            json.dump(tempArticle,f_w)
    else:
        tempArticle = {"Article": [
            {"title": "Today",
             "author": username,
             "time": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
             "content": "It's time,son"}
        ]}
        tempPath = os.path.join(path, username+".json")
        with open(tempPath, "w", encoding="utf-8") as f_w:
            json.dump(tempArticle, f_w)
#创建Js数据库
def CreDefauluser(path="BokeJJ.json"):
    CreArticle(username="admin")
    if not os.path.exists(path):
        temp={"User":[{"username":"admin","userPwd":"666666"}]}
        with open(path,"w",encoding="utf-8") as f_w:
            json.dump(temp,f_w)
# CreDefauluser()
def Readuser(path="BokeJJ.json"):
    if os.path.exists(path):
        with open(path,"r",encoding="utf-8") as f_r:
            return json.load(f_r)
# print(Readuser())
#更新
def Updateuser(username,userPwd,path="BokeJJ.json"):
    if os.path.exists(path):
        temp=Readuser(path)
        temp["User"].append({"username":username,"userPwd":userPwd})
        with open(path,"w",encoding="utf-8") as f_w:
            json.dump(temp,f_w)
# Updateuser("张三","123456")
#登录系统
def Login(path="BokeJJ.json"):
    global u_name
    s=0
    while True:
        user = input("请输入用户名：")
        userpwd = input("请输入密码：")
        temp=Readuser(path)
        for i in temp["User"]:
            if i["username"]==user and i["userPwd"]==userpwd:
                print("登陆成功")
                u_name=user
                return True
        s+=1
        if s==3:
            print("多次登录失败,请重新注册")
            return False
        print("登录失败,请重新登录")
# Login()

#注册系统
def Regeister(path="BokeJJ.json"):
    temp = Readuser(path)
    while True:
        isGo=True
        user= input("请输入用户名：")
        userpwd= input("请输入6-12位密码：")
        for i in temp["User"]:
            if i["username"]==user:
                print("该用户已存在，请重新注册")
                isGo = False
                break
        if isGo and len(userpwd) in range(6,13):
            print("注册成功")
            username=user
            userPwd=userpwd
            Updateuser(username, userPwd, path="BokeJJ.json")
            CreArticle(username)
            return True
# Regeister()
def ReadArticle(username,path="Article"):
    tempPath=os.path.join(path,username+".json")
    if  os.path.exists(tempPath):
        with open(tempPath,"r",encoding="utf-8") as f_r:
           return json.load(f_r)
# print(ReadArticle("小修"))
def WriteArtile(username,path="Article"):
    tempPath=os.path.join(path, username+".json")
    if os.path.exists(tempPath):
        tempArticle=ReadArticle(username)
        title=input("请输入标题？")
        content=input("请输入内容？")
        dictA={'title': title,
               'author': username,
               'time':datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"),
               'content': content
               }
        tempArticle["Article"].append(dictA)
        with open(tempPath,"w",encoding="utf-8") as f_w:
            json.dump(tempArticle,f_w)
            print("发表文章成功！")
# WriteArtile("小修")
def IndexAll(username,path="Article"):
    ReadAll=ReadArticle(username)
    print("以下为所有文章：（%s篇）" % (len(ReadAll["Article"])))
    for i in ReadAll["Article"]:
        print("\t标题\t：%s,\t时间\t：%s"%(i["title"],i["time"]))
    print("*"*50)
# IndexAll("张三")
def IndexOneArticle(username,path="Article"):
    ReadAll=ReadArticle(username)
    x=input("请输入要查询的文章序号,（如:1)")
    while 0>int(x) or int(x)>=len(ReadAll["Article"]):
        x = input("请输入要查询的文章序号：")
    print("\t标题:\t%s,\t作者:\t%s,\t时间:\t%s"%(ReadAll["Article"][int(x)]["title"],ReadAll["Article"][int(x)]["author"],ReadAll["Article"][int(x)]["time"]))
    print("\t内容:\t:",ReadAll["Article"][int(x)]["content"])
    print("*"*50)
# IndexOneArticle("小修")
def DeloneArticle(username,path="Article"):
    ReadA=ReadArticle(username,path="Article")
    print("以下为%s的所有文章"%username)
    for i in ReadA["Article"]:
        print("\t序号\t：%s,\t标题\t：%s,\t时间\t：%s" % (ReadA["Article"].index(i),i["title"], i["time"]))
    x=input("请输入要删的文章序号：")
    ReadA["Article"].pop(int(x))
    temp=os.path.join(path,username+".json")
    with open(temp,"w",encoding="utf-8") as f_w:
        json.dump(ReadA,f_w)
        print("删除成功！")
# DeloneArticle("张三")
def MotifyArticle(username,path="Article"):
    ReadA=ReadArticle(username,path)
    print("以下为%s的所有文章"%username)
    print(ReadA["Article"])
    for i in ReadA["Article"]:
        print("\t序号\t：%s,\t标题\t：%s,\t时间\t：%s" % (ReadA["Article"].index(i),i["title"], i["time"]))
    x=input("要修改的文章序号：")
    ReadA["Article"][int(x)]["title"]=input("请输入新标题:")
    ReadA["Article"][int(x)]["time"] =datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    ReadA["Article"][int(x)]["content"] = input("请输入新内容:")
    temppath=os.path.join(path,username+".json")
    with open(temppath,"w",encoding="utf-8") as f_w:
        json.dump(ReadA,f_w)
        print("修改成功")
# MotifyArticle("小修")
u_name=""
def main():
    while True:
        x=int(input("欢迎来到BokeJJ,请选择\n 1.登录；2.注册，3.退出"))
        if x==1:
            Isgo=Login()
            if Isgo:
                while True:
                    y = int(input("请选择\n \t1.写文章\n；\t2.查看所有文章目录\n；\t3.查看一篇文章\n；\t4.删除一篇文章；\n；\t5.修改一篇文章\n；\t6.退出登录"))
                    if y== 1:
                        WriteArtile(u_name, path="Article")
                    elif y==2:
                        IndexAll(u_name, path="Article")
                    elif y ==3:
                        IndexOneArticle(u_name, path="Article")
                    elif y ==4:
                        DeloneArticle(u_name, path="Article")
                    elif y == 5:
                        MotifyArticle(u_name, path="Article")
                    elif y ==6:
                        break
                    else:
                        print("输入错误，请重新输入")
        elif x==2:
            Regeister(path="BokeJJ.json")#注册
        elif x==3:
            break
        else:
            print("输入错误，请重新输入")
main()



