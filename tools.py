import encodings
import hashlib
import json

import requests

config = [312900,[1800,2000,35000,55]]



def countt(target = config[0],price = config[1]):
    res = len(price)*[0]
    # for i in res:
    #     for j in price:
    #         if
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1, 1000):
                for d in range(1, 1000):
                    if a*price[0]+b*price[1]+c*price[2]+d*price[3] == target:
                        return a, b, c, d


def get_item(erp_contract_id,tenant_id):
    try:
        url = 'https://gcxt.yl-beta.mycyjg.com/workload-item-erp/run-syn-data'
        data = {
            # "synType":1,
            "id":erp_contract_id,
            "type":"RefGuid",
            "access_token":"08dbf48a-b511-42bb-8728-43fdd31f1fe3",
            "__tenant_id":tenant_id,
            "raw":1
        }
        print(data)
        data = json.loads(requests.get(url=url,json=data).content.decode())
    except Exception():
        print(Exception)
    return data["data"]["data"]


def md5_hash(s):
    m = hashlib.md5()  # 创建md5对象
    m.update(s.encode(encoding='utf-8'))
    return m.hexdigest()

def sum(data):
    summary = 0
    imitems = 0
    ftitems = 0
    s = data["ModifiedTime"]+data["VersionNumber"]
    detail = data["Detail"]
    for i in detail :
        if i in ("Item","MeasureItem","FeeItem","TaxItem","SummaryMeasureItem","OtherItem"):
            print(i,len(detail[i]))
            imitems = len(detail["Item"]) + len(detail["MeasureItem"])
            ftitems = len(detail["FeeItem"]) + len(detail["TaxItem"])
        summary += len(detail[i])
    print("Item"+"MeasureItem %s" %imitems)
    print("FeeItem" + "TaxItem %s" % ftitems)
    print("总数 %s" % summary)
    print(md5_hash(s))



config_item = {
    "erp_contract_id" : "08dc083a-4770-4b8a-841e-bbf3ad99bfe6" ,
    "tenant_id" : "xt578c843a07379"
}
if __name__ == '__main__':
    details = get_item(config_item["erp_contract_id"],config_item["tenant_id"])
    print(details)
    sum(details)
