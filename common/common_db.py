import pymysql
class db():
    def __init__(self,user,pwd,host='dbproxy.mysre.cn',port=13366):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port

    def db_conn(self,db_name):
        conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,
                               db = db_name)
        return conn