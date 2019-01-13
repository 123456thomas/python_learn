import sqlalchemy
#导入sqlalchemy.orm引擎模块
from sqlalchemy import create_engine

#导入对话
from sqlalchemy.orm import sessionmaker
#导入sqlalchemy.ext.declarative父类模块
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
import os
from hashlib import sha1

#创建数据库,表
Path=os.path.join("D:\SoftWares\Data","game")
try:
    if not os.path.exists(Path):
        engin=create_engine('mysql+mysqlconnector://root:361365@localhost')
        engin.execute("create database game")
except Exception as e:
    print(e)

engin = create_engine('mysql+mysqlconnector://root:361365@localhost/game')
Path2=os.path.join("D:\SoftWares\Data\game","user.ibd")
try:
    if not os.path.exists(Path2):
        engin.execute("create table user (ID int primary key auto_increment,NAME varchar(15) not null,PWD varchar(50) not null)")
except Exception as e1:
    print(e1)

Path3=os.path.join("D:\SoftWares\Data\game","role.ibd")
try:
    if not os.path.exists(Path3):
        engin.execute("create table role (ID int primary key auto_increment,NICKNAME varchar(20) not null,TYPE varchar(20) not null,LEVEL int not null,USERID int not null, foreign key(USERID) references user(ID))")

except Exception as e2:
    print(e2)


#创建会话
Session=sessionmaker(bind=engin)
#创建交互
sess=Session()
#创建基本类
Base=declarative_base()
#用户类
class User(Base):
    __tablename__='user'
    ID=Column(Integer,primary_key=True,autoincrement=True)
    NAME=Column(String(15))
    PWD=Column(String(50))

#角色类
class Role(Base):
    __tablename__='role'
    ID=Column(Integer,primary_key=True,autoincrement=True)
    NICKNAME=Column(String(20))
    TYPE=Column(String(20))
    LEVEL=Column(Integer)
    USERID=Column(Integer)

#创建原始用户
mat=sha1()
mat.update("123456".encode("utf8"))
pwd0=mat.hexdigest()

try:
    result2 = sess.query(User.ID == 1).first()[0]
    if not result2:
        sess.add(User(ID=1,NAME="Li Ye",PWD=pwd0))
        sess.commit()
except Exception as e:
    print(e)
try:
    result21 = sess.query(Role.USERID == 1).first()
    if not result21:
        sess.add(Role(NICKNAME="庄周",TYPE="Master",LEVEL=20,USERID=1))
        sess.add(Role(NICKNAME="Arthur",TYPE="Worrior",LEVEL=20,USERID=1))
        sess.add(Role(NICKNAME="后羿",TYPE="Shooter",LEVEL=20,USERID=1))
        sess.add(Role(NICKNAME="白起",TYPE="Tank",LEVEL=20,USERID=1))
        sess.add(Role(NICKNAME="韩信",TYPE="Assassin",LEVEL=20,USERID=1))
        sess.commit()
except Exception as e:
    print(e)
    sess.rollback()

#登录方法
UserId=None
def Login():
    global UserId
    count=3
    while count>0:
        name=input("用户名:")
        pwd=input("密码:")
        matt=sha1()
        matt.update(pwd.encode("utf8"))
        pwd1=matt.hexdigest()
        Pwd=sess.query(User.PWD).filter(User.NAME==name).first()
        if Pwd is not None:
            if pwd1==Pwd[0]:
                print("Wellcome Universe, %s"%(name))
                restid=sess.query(User.ID).filter(User.NAME==name).first()[0]#获取外键，用于查看和创建英雄
                UserId=restid
                return True
            else:
                count-=1
                print("Password is wrong",count)
        else:
            count -= 1
            print("该用户名不存在",count)
# Login()

def Register():
    while True:
        try:
            name=input("用户名:")
            Pwd=sess.query(User.PWD).filter(User.NAME==name).first()
            if Pwd is None:
                pwd = input("密码:")
                matt = sha1()
                matt.update(pwd.encode("utf8"))
                pwd1 = matt.hexdigest()
                sess.add(User(NAME=name,PWD=pwd1))
                sess.commit()
                print("注册成功")
                break
            else:
                b1=input("该用户名已存在，是否继续注册（y）:")
                if b1!="y":
                    print("退出注册，再见")
                    break
        except Exception as e:
            print(e)
            sess.rollback()
# Register()
def GetRole(userid):
    b1=sess.query(Role.ID).filter(Role.USERID==userid).first()
    if b1 is not None:#判断是否有英雄
        result=sess.query(Role).filter(Role.USERID==userid)
        for i in result:
            print("英雄:%s\t类型:%s\t等级:%s"%(i.NICKNAME,i.TYPE,i.LEVEL))
    else:
        print("您还未创建角色")
# GetRole(3)

#创建角色：
def CreateRoles(userid):
    try:
        while True:
            typ1=input("请选择角色类型：\
            1.Master，2.Worrior,3.Shooter,4.Tank,5.Assassin")
            nick=input("请选择角色昵称：")
            if typ1=="1":
                Typ='Master'
            elif typ1=="2":
                Typ='Worrior'
            elif typ1=="3":
                Typ='Shooter'
            elif typ1 == "4":
                Typ = 'Tank'
            elif typ1 == "5":
                Typ = 'Assassin'
            else:
                print("输入错误，请输入角色类型编号")
                Typ=None
            if Typ is not None:
                b1=sess.query(Role.NICKNAME==nick,Role.TYPE==Typ).filter(Role.USERID==userid).first()

                #若b1=None,则没有创建过角色
                if b1 is not None:
                    if not (b1[0] and b1[1]):#确保一个用户的每种英雄不重名
                        sess.add(Role(NICKNAME=nick, TYPE=Typ, LEVEL=1, USERID=userid))
                    else:
                        print("该你的该角色已经存在")
                else:
                    sess.add(Role(NICKNAME=nick, TYPE=Typ, LEVEL=1, USERID=userid))
            b2=input("是否继续创建(y):")
            if b2 !="y":
                break
        sess.commit()
    except Exception as e:
        print(e)
        sess.rollback()
# CreateRoles(2)

def main():
    while True:
        t=input("欢迎来到鲲鹏:\n1.登录；2.注册;3.退出")
        if t=="1":
            ts=Login()
            if ts is True:
                while True:
                    t1=input("1.查看英雄;2.创建英雄；3.退出登录")
                    if t1=="1":
                        GetRole(UserId)
                    elif t1=="2":
                        CreateRoles(UserId)
                    elif t1=="3":
                        break
                    else:
                        print("输入错误")
        elif t=="2":
            Register()
        elif t=="3":
            print("再见")
            break
        else:
            print("输入错误")


if __name__ == '__main__':
    main()
