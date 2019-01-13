# import sqlalchemy,pymysql
# from sqltext.mysqlhelp import Helper


# py=Helper(_database="py1809",_password="361365")
# print(sqlalchemy.__version__)
# try:
#     py1=py.queryall("show tables")
#     print(py1)
#     py2=py.querymany("select * from test where id>2",size=2)
#     print(py2)
# except Exception as e:
#     print(e)



# 1.创建引擎对象
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:361365@localhost/py1809")
asd=engine.execute("show tables")
# asd1=engine
print(engine)


# 2.创建对话
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)

# 3.创建与表相应的类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String


Base=declarative_base()   #创建父类

#创建子类
class Test(Base):
    __tablename__="test"   #与表关联
    id=Column(Integer,primary_key=True)   #与表中的列关联
    class1 = Column(Integer)
    class2 = Column(Integer)


# 4.交互数据
session=Session()
# print(Session)
# print(session)

#1)查询

# resert=session.query(Test.id,Test.class1,Test.class2)
# print(resert)
# for i in resert:
#     print(i.id,i.class1,i.class2)

# resert=session.query(Test.class1,Test.class2).filter(Test.id>3)
# print(resert,type(resert))
# for i in resert:
#     print(i.class1,i.class2)

# resert=session.query(Test.class1,Test.class2).filter(Test.id>3).first()
# print(resert)

#2)添加数据
# t1=Test(id=0,class1=120,class2=120)
# session.add(t1)
# session.commit()

# 3)修改数据:（用实例对象修改，first）或（Query类的update({键:值}）
# resert=session.query(Test).filter(Test.id==4).first()
# resert.class1=27
# session.commit()
# print(type(resert))
# print(resert.class1)
# print(resert)

# resert=session.query(Test).filter(Test.id==10).update({Test.class1:99})
# session.commit()

# 4)删除数据
# resert=session.query(Test).filter(Test.id>8)
# resert.delete()
# session.commit()

# t4=session.query(Test).filter(Test.id==7).first()#t4为一个Test的一个实例
# print(t4)
# session.delete(t4)
# resert=session.query(Test)
# for i in resert:
#     print(i.id,i.class1,i.class2)
# session.commit()

# 5)扩展
