import sqlalchemy
#导入sqlalchemy.orm引擎模块
from sqlalchemy import create_engine

#导入对话
from sqlalchemy.orm import sessionmaker
#导入sqlalchemy.ext.declarative父类模块
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
import os
#创建数据库,stu表
Path=os.path.join("D:\SoftWares\Data","qiku")
try:
    if not os.path.exists(Path):
        print("----")
        engin=create_engine('mysql+mysqlconnector://root:361365@localhost')
        engin.execute("create database qiku")
except Exception as e:
    print(e)

engin = create_engine('mysql+mysqlconnector://root:361365@localhost/qiku')
Path2=os.path.join("D:\SoftWares\Data\qiku","stu.ibd")
try:
    if not os.path.exists(Path2):
        engin.execute("create table Stu (id int primary key auto_increment,name varchar(15) not null)")
except Exception as e1:
    print(e1)
#创建会话
Session=sessionmaker(bind=engin)
#创建交互
sess=Session()
#创建基本类
Base=declarative_base()
class Stu(Base):
    __tablename__='stu'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(15))

#插入数据
# isGo=True
# try:
#     while isGo:
#             Name=input("名字：")
#             sess.add(Stu(name=Name))
#             end2=input("是否结束输入（y）:")
#             if end2=="y":
#                 isGo=False
#     sess.commit()
# except Exception as e2:
#     print(e2)
#     sess.rollback()

#查找数据
#查看所有列
# result=sess.query(Stu)
# for i in result:
#     print(i.id,i.name)


#查看指定列
# result=sess.query(Stu)
# for i in result:
#     print(i.name)

#查看指定行
# result=sess.query(Stu).filter(Stu.id==6)
# for i in result:
#     print(i.id,i.name)

#添加
# sess.add(Stu(name="天明"))
# sess.commit()

#修改
# result=sess.query(Stu).filter(Stu.id==3).first()
# result.name="小明"
# sess.commit()
# print(result)

#删除
# sess.query(Stu).filter(Stu.id==3).delete()
# sess.commit()
