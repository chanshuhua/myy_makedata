
class sql():

    def sql_query(self,db_conn,sql):
        cursor = db_conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result