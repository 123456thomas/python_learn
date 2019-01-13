import pymysql

con=pymysql.connect(host="localhost", user="root", password="123456",
                 database="goods", port=3306)

cur=con.cursor()

cur.execute("select newfun(3,34)")
row=cur.fetchall()
print(row)
