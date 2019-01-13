import pymysql
#导入文件中的所有类
from Project.sqltext.mysqlhelp import Helper

py=Helper(_password="361365",_database="py1809_02")
print(py)

pya=py.queryall("select * from stud")
print(pya)
# pya1=py.update("insert into stud values(0,'Tim','man'),(0,'Tiem','women'),(0,'Tifm','man')")
# print(pya1)
# try:
#     #建立连接
#     con=None
#     con=pymysql.connect(host="192.168.12.64", user="aa", password="123456",
#                      database="py1809", port=3306)
#     # print(con)
#     #建立游标
#     cur=con.cursor()
#
#     #交互
#     resultrow=cur.execute("select * from sql_01")
#     # print(resultrow)
#     print(cur.fetchall())
#     num1=input("name")
#     num2=input("age")
#     num3 = input("weight")
#     num4= input("EQ")
#
#     resultrow=cur.execute("insert into sql_01 values(%s,%s,%s,%s,%s)",(0,num1,int(num2),int(num3),int(num4)))
#     #获取游标数据
#
#     #提交生效
#     con.commit()
# except Exception as e:
#     print(e)
#     if con is not None:
#         con.rollback()
# finally:
#     if con is not None:
#         if cur is not None:
#             cur.close()
#         con.close()

