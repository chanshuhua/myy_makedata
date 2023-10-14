
def sql_query(db_conn,sql):
        cursor = db_conn.cursor()
        cursor.execute(sql)
        return [i[0] for i in cursor.fetchall()]