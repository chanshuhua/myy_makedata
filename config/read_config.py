import json
import os
import yaml


config_info = {}

def read_configyaml():
    config_file = os.path.join(os.path.dirname(__file__), 'config_beta.yaml')
    f = open(config_file, 'r', encoding='utf-8')
    config_content = yaml.load(f.read(), Loader=yaml.FullLoader)
    return config_content

def configyaml_by_key(*args):
    '''
    两个层级的yaml文件
    :param args:
    :return:
    '''
    keys,values,moreargs = [],[],{}
    args = list(args)
    configyaml_data = read_configyaml()
    for key,value in configyaml_data.items():
        keys.append(key)
        values.append(value)
    if len(args) == 1 and args[0] in keys:
        return configyaml_data[args[0]]
    if len(args):
        for arg in args:
            for value in values:
                if arg in value.keys():
                    moreargs[arg] = value.get(arg)
        return moreargs
    else:
        return "找不到结果"

if __name__ == '__main__':
    f = configyaml_by_key('biz_type_model')
    print(f)