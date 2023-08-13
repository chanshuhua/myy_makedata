import json
import requests
from config.read_config import configyaml_by_key


env = "gcxt_beta"
user = "admin"
tenant = "gcxt_autotest"

global login_info
login_info = dict()

class Login():

    def __init__(self):
        self.env_url = configyaml_by_key(env)[env]
        self.userinfo = configyaml_by_key(user)[user]
        self.usertenant = configyaml_by_key(tenant)[tenant]
        self.usercode,self.userpwd = self.userinfo[0],self.userinfo[1]


    def login(self):
        '''登录'''
        url = self.env_url + 'user/login'
        data = {
            "__from": "web",
            "request_from": "web",
            "user_code":  self.usercode,
            "password": self.userpwd
            }
        self.login_request = json.loads(requests.post(url=url,json=data).content.decode())

    def login_env_info(self):
        '''获取环境登录相关信息'''
        return self.env_url,self.usertenant

    def login_user_info(self):
        '''获取用户登录相关信息'''
        self.login()
        # print(self.login_request)
        self.user_data_info = dict()
        self.user_data_info["user_id"] = self.login_request["data"].get("user_id")
        self.user_data_info["user_name"] = self.login_request["data"].get("name")
        self.user_data_info["user_code"] = self.login_request["data"].get("user_code")
        self.user_data_info["access_token"] = self.login_request["data"].get("access_token")
        # 组装租户信息
        self.user_tenant_info = dict()
        user_tenant_data = self.login_request["data"].get("tenant")
        if user_tenant_data:
            for tenant in user_tenant_data:
                if self.usertenant in tenant["tenant_code"]:
                    self.user_data_info["user_role_code"] = tenant.get("role_code")
                    self.user_data_info["user_main_station"] = tenant.get("station_name")
                    self.user_tenant_info["tenant_id"] = tenant["tenant_id"]
                    self.user_tenant_info["tenant_name"] = tenant["tenant_name"]
                    self.user_tenant_info["tenant_code"] = tenant["tenant_code"]
            if not self.user_tenant_info.get("tenant_id"):
                return "无该租户权限"
        else:
            return "无租户权限"

        login_info["env"] = self.env_url
        login_info["user_info"] = self.user_data_info
        login_info["tenant_info"] = self.user_tenant_info
        return self.user_data_info,self.user_tenant_info

    def refresh_login(self):
        print("重新登录")
        self.login_user_info()
        return login_info

    def get_login_info(self):
        if not login_info:
            self.login_user_info()
        return login_info




if __name__ == '__main__':
    print(Login().refresh_login())