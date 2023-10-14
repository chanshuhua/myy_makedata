from common import common_db
from common import common_sql
db_source = [{
            "db_source":"gcxt_beta",
            "db_name":"gcxt_ngzy",
            "user":"chensh06@295",
            "pwd":"d1a016d2c12b1afd585cd37fe73fb46f"
            }
            # {
            # "db_source": "mycommunity_beta",
            # "db_name": "mycommunity_jinhui",
            # "user": "chensh06@304",
            # "pwd": "0d5f9d905f233c680bf862c848fe1512"
            # },
            ]

def db_model():
    # for db in db_source:
    #     print(common_db.db(user=db["user"], pwd=db["pwd"]).db_conn(db["db_name"]))
    #     return common_db.db(user=db["user"], pwd=db["pwd"]).db_conn(db["db_name"])
    return common_db.db(user=db_source[0]["user"], pwd=db_source[0]["pwd"]).db_conn(db_source[0]["db_name"])


def query(sql):
    # common_sql.sql_query(db_model(), sql)
    return common_sql.sql_query(db_model(), sql)



if __name__ == '__main__':

    # db_model()
    # sql_x = 'select yunfuwu_project_id from xt_project where erp_is_deleted = 0'
    # x = set(common_sql.sql().sql_query(db_conn=source["gcxt_jinhui"],sql= sql_x))
    # # print(list_x)
    # sql_y = 'select project_id from t_auth_project where is_deleted = 0 '
    # y = set(common_sql.sql().sql_query(db_conn=source["mycommunity_jinhui"], sql=sql_y))
    # # print(list_y)
    # m = set.intersection(x,y)
    # param = ''
    # for i in m:
    #     for j in i:
    #         param = param +'"'+j + '",'
    # param = param + '"0")'
    # sql_m = 'select contract_id from xt_project_contract where project_id in (select project_id from xt_project where yunfuwu_project_id in ('+param+')'
    # print(sql_m)
    # mm = set(common_sql.sql().sql_query(db_conn=source["gcxt_jinhui"], sql=sql_m))
    # print(mm)
    # soure = (common_db.db(user='',pwd='d1a016d2c12b1afd585cd37fe73fb46f').db_conn('gcxt_betatest'))

    print(query(sql = "SELECT contract_id FROM xt_project_contract WHERE project_id in (SELECT project_id FROM xt_jf_project WHERE user_id = '516167')"))