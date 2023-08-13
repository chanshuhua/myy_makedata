from config.read_config import configyaml_by_key
from common.Request import Request

env_url = list(configyaml_by_key("env").values())[0]
biz_type_flow = configyaml_by_key("biz_type_flow")


class Flow():
    def __init__(self):
        self.url = env_url

    def set_free_flow(self,):
        '''自由流程'''

        url = self.url + '/proc-tmpl/save-company-biz-flow'
        data = {
            "request_from": "web",
            "company_id": "44",
            "biz_type": "2",
            "change_type": "现场签证",
            "is_on_role": "0",
            # "detail": "[{\"role\":\"0\",\"role_name\":\"所有\",\"flow_type\":\"0\",\"is_distinct\":\"0\",\"step_list\":[{\"step_type\":\"1\",\"step_name\":\"发起人\"},{\"station_name\":\"甲方工程师2\",\"open_add_sign\":1,\"step_order\":\"5\",\"step_name\":\"签发\",\"step_type\":\"2\",\"handle_mode\":\"0\",\"is_allow_multi_approver_in_counter_sign\":\"0\",\"handler_list\":[\"1\"]}],\"branches\":[]}]"
            "detail" : [{
                "role":"0",
                "role_name":"所有",
                "flow_type":"0",
                "is_distinct":"0",
                "step_list":[],
                "branches":[]
                }]
        }
        print(url)
        flow_request = Request().request(url=url,data=data)
        return flow_request


if __name__ == '__main__':
     print(env_url)
     print(type(env_url))
     # name = {"name": "chen"}
     # name.update({"key": "value"})
     # print(name)

