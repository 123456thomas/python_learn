import  pymysql

#建立mysql辅助类
class Helper:
    def __init__(self,_host="localhost", _user="root", _password="123456",
                 _database="py1809", _port=3306):
        self.con=None
        self.cur=None
        self.host=_host
        self.user=_user
        self.password=_password
        self.database=_database
        self.port=_port
        self.__connect()
    def __connect(self):
        #创建连接和游标
        try:
            self.con=pymysql.connect(self.host,self.user,self.password,self.database,self.port)
            self.cur=self.con.cursor()
        except Exception as e:
            print(e)
    def queryone(self,query,arg=None):
        try:
            self.cur.execute(query,arg)
            row=self.cur.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.con is not None:
                self.con.close()
    def querymany(self,query,arg=None,size=1):
        #一次查询多个
        try:
            self.cur.execute(query,arg)
            print(size)
            return self.cur.fetchmany(size)
        except Exception as e:
            print(e)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.con is not None:
                self.con.close()
    def queryall(self,query,arg=None):
        #一次查询多个
        try:
            self.cur.execute(query,arg)
            row=self.cur.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.con is not None:
                self.con.close()
    def updates(self,query,arg=None):
        #数据更新，可用于插入、删除、修改
        try:
            self.cur.execute(query,arg)
            if self.con is not None:
                self.con.commit()
        except Exception as e:
            print(e)
            if self.con is not None:
                self.con.rollback()
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.con is not None:
                self.con.close()