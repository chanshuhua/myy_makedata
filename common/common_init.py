from config.read_config import  configyaml_by_key
from login_sso import Login

contract_id = configyaml_by_key("contract_info").get("contract_id")
login_info = Login().get_login_info()

def contract_project_list():
    pass




if __name__ == '__main__':
    print(contract_info)