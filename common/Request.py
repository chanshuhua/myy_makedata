import json
from time import sleep
import requests
from login_sso import Login


class Request():
    def request(self,url,data=None):
        login_info = Login().get_login_info()
        header = {
            "Content-Type":"application/json"
        }
        if data:
            data.update({
                "user_id": login_info["user_info"].__getitem__("user_id"),
                "__tenant_id": login_info["tenant_info"].__getitem__("tenant_id"),
                "cur_role_code": login_info["user_info"].__getitem__("user_role_code"),
                "access_token": login_info["user_info"].__getitem__("access_token"),
                "__from": "web",
                "user_name": login_info["user_info"].__getitem__("user_name")
            })
            request_data = json.loads(requests.post(url=url, json=data, headers=header).content.decode())

        else:
            request_data = json.loads(requests.get(url=url, params=data).content.decode())

        if request_data["success"] == 0 and request_data["message"] == "token失效":
            print(Login().refresh_login())
            self.request(url=url,data=data)

        return request_data
