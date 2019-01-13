import pymysql
print (pymysql)

#2.构造链接对象
con=pymysql.connect(host="host", user="root", password="123456",
                 database="py1809_02", port=3306)
# print(con)

#3.构建游标与数据库交互
cur=con.cursor()
# print(cur)

#4.开始交互
resultrow=cur.execute("select * from class_1")
print(resultrow)

#获取游标中的所有数据
# result=cur.fetchall()
result1=cur.fetchone()
# result2=cur.fetchone()
# result2=cur.fetchmany(2)
# print(result1,result2)
#设置游标位置，默认是相对位置，也可以设为绝对位置、
#游标往下走两步，若为负数则是后退
# cur.scroll(-1)
result2=cur.fetchmany(2)
cur.scroll(0,mode="absolute")
result3=cur.fetchmany(2)
print(result1,result2,result3)

#6.操作完成，释放资源，先游标，后连接
cur.close()
con.close()
