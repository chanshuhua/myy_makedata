
db_source = \
    beta = [
        {
        "db_source":"gcxt_beta",
        "db_name":"gcxt_autotest",
        "user":"chensh06@295",
        "pwd":"d1a016d2c12b1afd585cd37fe73fb46f"
        },
        # {
        # "db_source":"gcxt_beta",
        # "db_name":"gcxt_betatest",
        # "user":"f919ba47-575b-46cf-86c4-78dfda196e88",
        # "pwd":"2TZ9Bmrau7Rf30wB"
        # },
    # {
    # "db_source": "mycommunity_beta",
    # "db_name": "mycommunity_jinhui",
    # "user": "chensh06@304",
    # "pwd": "0d5f9d905f233c680bf862c848fe1512"
    # },
    ]



def get_sql_info():
    return db_source[0]