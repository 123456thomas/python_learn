import pymysql

con=pymysql.connect(host="localhost", user="root", password="361365",
                 database="mytest", port=3306)

cur=con.cursor()

# cur.execute("create table test1(Id int primary key,Name varchar(20) not null)")


cur.execute("create table test2(id int primary key,name varchar(20) not null,userid int, foreign key(userid) references test1(Id))")