import json
import random
import requests
import uuid
from datetime import datetime,date
import datetime
import ssl

create_default_https_context = ssl._create_unverified_context()

fq_user = {
    "user_id": 502,
    "user_code": 18665555013,
    "role_code": 1004,
    "user_name": "合同管理员接口",
    "user_station_name": "乙方合同负责人"

    # "user_id": 516168,
    # "user_code": 13425916002,
    # "role_code": 1002,
    # "user_name": "ccc2",
    # "user_station_name": "B岗位"
}

sp_user = {
    "user_id": 500,
    "user_code": 18665555011,
    "role_code": 1001,
    "user_name": "接口甲方啊",
    "user_station_name": "独一无二"

    # "user_id": 516167,
    # "user_code": 13425916001,
    # "role_code": 1001,
    # "user_name": "ccc1",
    # "user_station_name": "甲方项目管理员"
}

contract_info = {
    "contract_id": "6836",
    "yf_company": "北京市第三建筑工程公司",
    "yf_company_guid": "64e7cae5-08af-eb11-b73f-0050568d3d8d"

    # "contract_id": "24",
    # "yf_company": "青岛盛泽建设工程有限公司",
    # "yf_company_guid": "f6286717-fd5a-eb11-902c-cb823b2d279f"

}

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")





class makedata():

    def __init__(self):
        self.url = 'https://gcxt-beta.myfuwu.com.cn'
        self.random_uuid = str(uuid.uuid4())
        self.token = '2cc1299f47088c0ea54b97c868948450'
        self.tenant_id = 'xt57985278b86ec'
        # self.token = 'b09343be360affa01f226993b4bc5e0b'
        # self.tenant_id = 'xt605c5ff10a738'
        self.request_from = 'web'
        # self.request_from = 'yunfuwu_web'
        self.fq_user_id,self.fq_user_code,self.fq_role_code,self.fq_user_name,self.fq_station_name = fq_user["user_id"],fq_user["user_code"],fq_user["role_code"],fq_user["user_name"],fq_user["user_station_name"]
        self.sp_user_id,self.sp_user_code,self.sp_role_code,self.sp_user_name,self.sp_station_name = sp_user["user_id"],sp_user["user_code"],sp_user["role_code"],sp_user["user_name"],sp_user["user_station_name"]
        self.contract_id,self.yf_company,self.yf_company_guid = contract_info["contract_id"],contract_info["yf_company"],contract_info["yf_company_guid"]


    def get_contract_info(self,sql):

        contract_info = {
            "contract_id": "62",
            "yf_company": "北京市第三建筑工程公司",
            "yf_company_guid": "64e7cae5-08af-eb11-b73f-0050568d3d8d"
        }

    def create_worksheet_gld_fix(self):
        url = self.url + '/form/save'
        print(url)
        data = {
            "access_token": self.token,
            "user_id": self.fq_user_id,
            "role_code": self.fq_role_code,
            "cur_role_code": self.fq_role_code,
            "user_name": self.fq_user_name,
            "__tenant_id": self.tenant_id,
            "request_from": self.request_from,
            "__from": self.request_from,
            # "__vue_web": 'true',
            "biz_data": {
                "biz_type": "2",
                "biz_id": self.random_uuid,
                "user_id": self.fq_user_id,
                "tenant_id": self.tenant_id,
                "worksheet": {
                    "change_type": "现场签证",
                    "images": [],
                    "workloads": [],
                    "attachments": [],
                    "cc_user_ids": [],
                    "contract_id": self.contract_id,
                    "meeting_id": "",
                    "change_overview": "现场签证工联单"+ str(random.randint(1,1000)) + "# " +str(self.random_uuid),
                    "custom_10": self.yf_company,
                    "description": "1",
                    "required_completion_date": now,
                    "erp_change_type": "现场签证",
                    "change_reason": "见证签证",
                    "change_stage": "工程实施中",
                    "major": "给排水",
                    "estimated_cost": 1,
                    "custom_1": 1,
                    "flow": {
                        "type": "1",
                        "is_distinct": "0",
                        "flow": [
                            {
                                "select": "0",
                                "approve": "0",
                                "station": {
                                    "name": self.fq_station_name
                                },
                                "approver": {
                                    "approver_id": self.fq_user_id,
                                    "user_id": self.fq_user_id,
                                    "user_name": self.fq_user_name,
                                    "yf_provider_station_name": "",
                                    "yf_provider_station_id": ""
                                },
                                "step_name": "发起人"
                            },
                            {
                                "select": "1",
                                "approve": "0",
                                "origin_tmpl_id": 0,
                                "is_rollback": "0",
                                "station": {
                                    "name": self.sp_station_name
                                },
                                "node_setting": {
                                    "open_add_sign": "1",
                                    "is_allow_multi_approver_in_counter_sign": "0",
                                    "open_overall_contract_approve": "0"
                                },
                                "handle_mode": "0",
                                "more": "0",
                                "step_name": "签发",
                                "step_order": "0",
                                "handler_list": [
                                    {
                                        "flow_node_id": None,
                                        "flow_id": None,
                                        "handler_type": "1",
                                        "handler_code": "1197",
                                        "handler_name": self.sp_station_name,
                                        "select": "1",
                                        "approve": "0",
                                        "is_rollback": "0",
                                        "station": {
                                            "name": self.sp_station_name
                                        },
                                        "approver": {
                                            "approver_id": self.sp_user_id,
                                            "yf_provider_station_id": "",
                                            "yf_provider_station_name": ""
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    "attach_condition": [],
                    "flow_type": "1",
                    "worksheet_id": self.random_uuid,
                    "version": 1,
                    "check_status": "1"
                },
                "photos": [],
                "attachments": [],
                "attach_condition": []
            }

        }
        headers = {
            'content-type': "application/json",
            'charset': 'UTF-8'
        }
        print(json.dumps(data))
        request_data = json.loads(requests.post(url=url, data=json.dumps(data), headers=headers,verify=False).content.decode())
        return request_data

    def sign_xcqz(self):
        url = self.url + '/form/save'
        data = {}

        headers = {
            'content-type': "application/json",
            'charset': 'UTF-8'
        }
        # print(data)
        request_data = json.loads(requests.post(url=url, data=json.dumps(data), headers=headers).content.decode())
        return request_data

    def create_deduction_notice(self):
        url = self.url + '/form/save'
        data = {
                "access_token": self.token,
                "user_id": "516167",
                "role_code": "1001",
                "cur_role_code": "1001",
                "user_name": "ccc1（甲方）",
                "__tenant_id": self.tenant_id,
                "request_from": "yunfuwu_web",
                "__from": "yunfuwu_web",
                "__vue_web": 'true',
                "biz_data": {
                    "biz_type": "31",
                    "biz_id": self.random_uuid,
                    "user_id": "516167",
                    "tenant_id": self.tenant_id,
                    "deduction_notice": {
                        "images": [],
                        "attachments": [
                            {
                                "file_id": "53ee09c9-2e00-4813-8692-74e9b5e98b5b",
                                "file_name": "会动的鸭子.gif",
                                "file_path": "https://beta-gcxt.oss-cn-shenzhen.aliyuncs.com/gcxt/xt/poly/31/2023/05/04/b/3/e/poly_31_2023_05_04_b3e6d203-bf0e-4dff-85be-293907ccb2f6.gif",
                                "file_size": "250.478515625",
                                "create_time": "2023-05-04 14:00",
                                "create_by": "ccc1（甲方）",
                                "attach_name": "附件域2-全员可见",
                                "attach_class": "3a0a7b82-0976-01c1-73a2-8f54abaebd46",
                                "attach_remark": "123123",
                                "is_must": 1,
                                "is_append": "0",
                                "is_append_to_erp": "",
                                "user_id": "516167",
                                "__appendEditAble": 'false',
                                "__supplyEditAble": 'false',
                                "__fromRelatedDetail": 'false'
                            }
                        ],
                        "cc_user_ids": [],
                        "contract_id": "26781",
                        "custom_1": "",
                        "subject": "审批通过的扣款明细" + str(self.random_uuid),
                        "description": "审批通过的扣款明细"+str(random.randbytes(100)),
                        "deduction_type_name": "扣款类型-1",
                        "deduction_amount": 1,
                        "deduct_date": "2023-05-04",
                        "record_user_name": "ccc1（甲方）",
                        "record_date": "2023-05-04 14:00:01",
                        "flow": {
                            "type": "1",
                            "is_distinct": "0",
                            "flow": [
                                {
                                    "select": "0",
                                    "approve": "0",
                                    "station": {
                                        "name": "甲方成本经办人"
                                    },
                                    "approver": {
                                        "approver_id": "516167",
                                        "user_id": "516167",
                                        "user_name": "ccc1（甲方）",
                                        "yf_provider_station_name": "",
                                        "yf_provider_station_id": ""
                                    },
                                    "step_name": "发起人"
                                },
                                {
                                    "select": "1",
                                    "approve": "0",
                                    "origin_tmpl_id": 0,
                                    "is_rollback": "0",
                                    "station": {
                                        "name": "甲方成本经办人"
                                    },
                                    "node_setting": {
                                        "open_add_sign": "1",
                                        "is_allow_multi_approver_in_counter_sign": "0"
                                    },
                                    "handle_mode": "0",
                                    "more": "0",
                                    "step_name": "归档",
                                    "step_order": "0",
                                    "handler_list": [
                                        {
                                            "flow_node_id": 'null',
                                            "flow_id": 'null',
                                            "handler_type": "1",
                                            "handler_code": "11",
                                            "handler_name": "甲方成本经办人",
                                            "select": "1",
                                            "approve": "0",
                                            "is_rollback": "0",
                                            "station": {
                                                "name": "甲方成本经办人"
                                            },
                                            "approver": {
                                                "approver_id": "516185",
                                                "yf_provider_station_id": "",
                                                "yf_provider_station_name": ""
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "flow_type": "1",
                        "biz_id": self.random_uuid,
                        "change_type": "",
                        "version": 1,
                        "check_status": "1"
                    },
                    "photos": [],
                    "attachments": [
                        {
                            "file_id": "53ee09c9-2e00-4813-8692-74e9b5e98b5b",
                            "file_name": "会动的鸭子.gif",
                            "file_path": "https://beta-gcxt.oss-cn-shenzhen.aliyuncs.com/gcxt/xt/poly/31/2023/05/04/b/3/e/poly_31_2023_05_04_b3e6d203-bf0e-4dff-85be-293907ccb2f6.gif",
                            "file_size": "250.478515625",
                            "create_time": "2023-05-04 14:00",
                            "create_by": "ccc1（甲方）",
                            "attach_name": "附件域2-全员可见",
                            "attach_class": "3a0a7b82-0976-01c1-73a2-8f54abaebd46",
                            "attach_remark": "123123",
                            "is_must": 1,
                            "is_append": "0",
                            "is_append_to_erp": "",
                            "user_id": "516167",
                            "__appendEditAble": 'false',
                            "__supplyEditAble": 'false',
                            "__fromRelatedDetail": 'false'
                        }
                    ],
                    "attach_condition": [
                        {
                            "detail_id": "3a0a7b82-0976-72b6-2f5d-99a30f5fc0cf",
                            "attach_name": "附件域1-乙方合同负责人",
                            "attach_remark": "",
                            "attach_condition": [],
                            "station_condition": [
                                {
                                    "station_id": "10",
                                    "station_name": "甲方工程经办人",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1001",
                                        "1002"
                                    ]
                                },
                                {
                                    "station_id": "11",
                                    "station_name": "甲方成本经办人",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1001",
                                        "1002"
                                    ]
                                },
                                {
                                    "station_id": "13",
                                    "station_name": "平台公司管理员",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1001",
                                        "1002"
                                    ]
                                },
                                {
                                    "station_id": "47",
                                    "station_name": "甲方项目管理员",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1001",
                                        "1002"
                                    ]
                                },
                                {
                                    "station_id": "1228",
                                    "station_name": "甲方成本部经理",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1001",
                                        "1002"
                                    ]
                                },
                                {
                                    "station_id": "1448",
                                    "station_name": "甲方项目经理",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1001",
                                        "1002"
                                    ]
                                },
                                {
                                    "station_id": "8",
                                    "station_name": "专业监理工程师",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1003"
                                    ]
                                },
                                {
                                    "station_id": "9",
                                    "station_name": "监理总监",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1003"
                                    ]
                                },
                                {
                                    "station_id": "49",
                                    "station_name": "监理现场人员",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1003"
                                    ]
                                },
                                {
                                    "station_id": "1107",
                                    "station_name": "咨询工程师",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "998"
                                    ]
                                },
                                {
                                    "station_id": "1147",
                                    "station_name": "咨询公司工程师",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "998"
                                    ]
                                },
                                {
                                    "station_id": "50",
                                    "station_name": "乙方合同负责人",
                                    "uploadable": 1,
                                    "visible": 1,
                                    "disabled": 'true',
                                    "roles": [
                                        "1004"
                                    ]
                                },
                                {
                                    "station_id": "1441",
                                    "station_name": "乙方合同经办人（负责人）",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1004"
                                    ]
                                },
                                {
                                    "station_id": "12",
                                    "station_name": "乙方合同经办人",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1005"
                                    ]
                                },
                                {
                                    "station_id": "14",
                                    "station_name": "乙方现场工程师",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1005"
                                    ]
                                },
                                {
                                    "station_id": "53",
                                    "station_name": "乙方材料员",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1005"
                                    ]
                                },
                                {
                                    "station_id": "1443",
                                    "station_name": "乙方现场2",
                                    "uploadable": 0,
                                    "visible": 0,
                                    "disabled": 'false',
                                    "roles": [
                                        "1005"
                                    ]
                                }
                            ],
                            "is_must": 0
                        },
                        {
                            "detail_id": "3a0a7b82-0976-01c1-73a2-8f54abaebd46",
                            "attach_name": "附件域2-全员可见",
                            "attach_remark": "123123",
                            "attach_condition": [],
                            "station_condition": [],
                            "is_must": 1
                        }
                    ]
                }
}
        headers = {
            'content-type': "application/json",
            'charset': 'UTF-8'
        }
        # print(data)
        request_data = json.loads(requests.post(url=url, data=json.dumps(data), headers=headers).content.decode())
        return request_data

    def check_data(self):
        url = 'https://gcxt.mingyuanyun.com/list/get-list'
        data = {
              "access_token": "f8d0a9bfeb19361382da173a28aa3bd3",
              "user_id": "260377",
              "role_code": "2001",
              "cur_role_code": "2001",
              "user_name": "超级用户",
              "__tenant_id": "xt5ebe5d8c83763",
              "request_from": "yunfuwu_web",
              "__from": "yunfuwu_web",
              "__vue_web": 'true',
              "biz_type": "2",
              "keyword": "",
              "project_id": "",
              "company_id": "25",
              "filter": [
                {
                  "id": "project_ids",
                  "field": "",
                  "type": "select",
                  "text": "百合花园-一期",
                  "value": [
                    "105"
                  ]
                },
                {
                  "id": "_from",
                  "field": "来源",
                  "type": "normal",
                  "text": "工程协同发起",
                  "value": [
                    "web",
                    "app",
                    "yunfuwu_web"
                  ]
                }
              ],
              'status': "2",
              "page_index": 1,
              "page_size": 1000,
              "warning_status": 0,
              "unlock": 0,
              "change_type": "现场签证"
            }
        headers = {
            'content-type': "application/json",
            'charset': 'UTF-8'
        }
        request_data = json.loads(requests.post(url=url, data=json.dumps(data), headers=headers).content.decode())
        return request_data["data"]

    def add_data(self,data,select_data):
        ans = []
        cost = 0.0000
        for i in data:
            # print(i)
            if i[select_data]:
                ans.append(i[select_data])
        for i in ans:
            cost += float(i)
        return ans,cost

    def add_check_data(self,data,select_data,check_data):
        ans = []
        cost = 0.0000
        for i in data:
            print(i)
            if i[select_data] == check_data:
                ans.append(i[select_data])
        return ans, len(ans)

    def add_sptime_fqtime(self,times):
        total_ans = 0
        for i in times:
            time_1 = datetime.datetime.strptime(i[0],"%Y-%m-%d %H:%M:%S")
            time_2 = datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S")
            total_seconds = (time_2-time_1).total_seconds()
            total_ans += total_seconds
        ans_hour = total_ans/3600
        ans = (total_ans/86400)/len(times)
        return total_ans,ans_hour,ans

    def day_add_date(self):
        meet_result = date(2022,12,12) + datetime.timedelta(days = 45)
        work_result = date(2023,4,1) + datetime.timedelta(days = 30)
        confirm_result = date(2023,5,15) + datetime.timedelta(days=-90)
        return meet_result,work_result,confirm_result


if __name__ == '__main__':
    # request_data = makedata().check_data()
    # print(makedata().add_check_data(request_data,"erp_check_status","未审核"))
    # times = [['2023-01-05 21:42:58','2023-01-05 21:44:16'],
    #          ['2023-02-03 11:48:58', '2023-02-03 11:50:58'],
    #          ['2022-12-27 15:26:19','2022-12-27 15:26:37'],
    #          ['2023-03-15 17:36:48', '2023-03-15 17:38:08'],
    #          ['2023-02-28 20:29:11','2023-02-28 22:20:19'],
    #          ['2023-05-06 10:39:56','2023-05-06 10:42:46'],
    #
    #          ]
    # print(makedata().add_sptime_fqtime(times))
    # print(str(os.path.dirname(__file__))+'\data.json')
    # for i in range(5):
        # print(makedata().create_deduction_notice())
    for i in range(5):
         print(makedata().create_worksheet_gld_fix())