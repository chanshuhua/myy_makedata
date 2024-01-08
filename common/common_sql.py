import logging

from config import sql_config
from common import common_db


class DB_Conn():
    def db_model(self,db_source):
        # for db in db_source:
        #     print(common_db.db(user=db["user"], pwd=db["pwd"]).db_conn(db["db_name"]))
        #     return common_db.db(user=db["user"], pwd=db["pwd"]).db_conn(db["db_name"])
        return common_db.db(user=db_source["user"], pwd=db_source["pwd"]).db_conn(db_source["db_name"])



class DB(DB_Conn):
    def __init__(self):
        self.db = DB_Conn().db_model(sql_config.get_sql_info())
        self.cursor = self.db.cursor()

    def sql_query(self,sql):
        try:
            self.cursor.execute(sql)
            print([i for i in self.cursor.fetchall()])
        except Exception as e:
            logging.error("error message"+str(e))


    def sql_ac(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            logging.error("error message"+str(e))

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    # conn = DB()
    # name = "陈小甲"
    # # s = "update xt_user set name = '{}' where user_id = 516167".format(name)
    # s = "update xt_user set name = '%s' where user_id = 516167" %name
    # # print(s)
    # # conn.sql_ac("update xt_user set name = '%s' where user_id = 516167") %name
    # conn.sql_ac(s)
    # conn.sql_query("select * from xt_user where user_code = \'13425916001\'  limit 1 ;")
    # conn.close()
    pass