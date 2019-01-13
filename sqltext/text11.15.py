import pymysql
from sqltext.sqlhelper import Helper as hp
from hashlib import md5

#第8题，编写MYSQL辅助类 提供 查询一条 查询N条  查询所有  更新 四种方法


#
# print(hp(_database="goods",_password="123456").queryone("select * from goods where price<%s",(3000)))
# print(hp(_database="goods",_password="123456").querymany("select * from goods where id>%s",(2),2))
#
# print(hp(_database="goods",_password="123456").queryall("select * from goods where price>%s",(2000)))
#
# hp(_database="goods",_password="123456").updates("insert into goods (names,price) values('jianguo',2100),('Meizu',3100)")
# print(hp(_database="goods",_password="123456").queryall("select * from goods"))

# 9，编写登录案例，最多登录三次，超过3题输出超出最大次数
count=3
while count>0:
    users=input("用户名:")
    pwds=input("密码:")
    try:
       pwd=hp(_database="py1809",_password="361365").queryone("select pwd from userdata where user=%s",(users,))
       shat = md5()#为了避免之前加密对shat的影响，每次加密必须初始化
       shat.update(pwds.encode("utf8"))
       shapwd = shat.hexdigest()
    except Exception as e:
        print(e)
    print(pwd)
    if pwd is not None:
        # shat.update(pwds.encode("utf8"))
        # shapwd=shat.hexdigest()
        #第二次输入正确，密码加密错误
        print(pwds)

        print(shapwd)
        if shapwd==pwd[0]:
            print("登录成功")
            print("登录%s次"%(4-count))
            break
        else:
            count-=1
            print("密码错误")
    else:
        count-=1
        print("用户名不存在")
    if count==0:
        print("超出登录次数，登录失败")


#10，编写例子通过executemany 一次性插入5条数据
# con=None
# cur=None
# con=pymysql.connect( host="localhost", user="root", password="361365",
#                  database="py1809", port=3306)
# cur=con.cursor()
# try:
#     cur.executemany("insert into test (class1,class2) values(%s,%s)",[(87,85),(100,98),(89,99),(92,95),(87,89)])
#     if con is not None:
#         con.commit()
# except Exception as e:
#     print(e)
#     if con is not None:
#         con.rollback()
# finally:
#     if cur is not None:
#         cur.close()
#     if con is not None:
#         con.close()