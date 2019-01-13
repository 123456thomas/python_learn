import pymysql

#构建mysql辅助类
class Helper:
    def __init__(self,_host="localhost", _user="root", _password="123456",
                 _database="py1809", _port=3306):
        self.host=_host
        self.user=_user
        self.__password=_password
        self.database=_database
        self.port=_port
        self.con=None
        self.cur=None
        self.__connect()
    def __connect(self):
        #建立链接，构造游标对象
        try:
            self.con= pymysql.connect(host=self.host, user=self.user, password=self.__password,
                                  database=self.database, port=self.port)
            self.cur=self.con.cursor()
        except Exception as e:
            print(e)
    def queryone(self,query,arg=None):
        #查询一个数据，arg用于query的占位符
        try:
            self.cur.execute(query,arg)
            return self.cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            if self.con is not None:
                if self.cur is not None:
                    self.cur.close()
                self.con.close()
    def querymany(self,query,arg=None,size=1):
        try:
            self.cur.execute(query,arg)
            return self.cur.fetchmany(size)
        except Exception as e:
            print(e)
        finally:
            if self.con is not None:
                if self.cur is not None:
                    self.cur.close()
                self.con.close()
    def queryall(self,query,arg=None):
        #查询所有文件
        try:
            self.cur.execute(query,arg)
            return self.cur.fetchall()
        except Exception as e:
            print(e)
        finally:
            if self.con is not None:
                if self.cur is not None:
                    self.cur.close()
                self.con.close()
    def update(self,query,arg=None):
        #用于增、删、改,arg是个列表嵌套元组
        try:
            row=self.cur.execute(query,arg)
            if self.con is not None:
                self.con.commit()
            return row
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            if self.con is not None:
                if self.cur is not None:
                    self.cur.close()
                self.con.close()

