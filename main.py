import datetime
import random

from flow_config.set_flow import Flow


def exec():
    flow = Flow()
    flow.set_free_flow()






if __name__ == '__main__':
    # exec()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(random.randint(1,1000))