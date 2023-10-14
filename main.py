import datetime
import random

from flow_config.set_flow import Flow
erp_module = []

def exec():
    flow = Flow()
    flow.set_free_flow()






if __name__ == '__main__':
    # exec()
    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # print(random.randint(1,1000))

    datare = {
        "success": 1,
        "data": [
          {
            "biz_id": 2,
            "biz_name": "工联单"
          },
          {
            "biz_id": 3,
            "biz_name": "完工单"
          },
          {
            "biz_id": 5,
            "biz_name": "产值申报单"
          },
          {
            "biz_id": 71,
            "biz_name": "结算申请"
          },
          {
            "biz_id": 11,
            "biz_name": "付款申请"
          }
        ],
  "message": "",
  "current_ts": ""
}
    erp_module = []
    for dat in datare["data"]:
        erp_module.append(dat["biz_id"])
    print(erp_module)
