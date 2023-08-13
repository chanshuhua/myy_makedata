import os
import datetime
import time

dt = datetime.datetime.now()
file_array = str(os.path.dirname(__file__))+'\\array.json'
file_txt = str(os.path.dirname(__file__)) + '\\data.json'
file_w_txt = str(os.path.dirname(__file__)) +  '\\data-{}.json'.format(str(time.mktime(dt.timetuple())))
file_w_array = str(os.path.dirname(__file__)) +  '\\array-{}.json'.format(str(time.mktime(dt.timetuple())))


def array_to_txt(f_from,f_to):
    with open(f_from,'r') as f :
        array = f.read()
    array_data = list(array.strip('[]',).replace("'","").split(','))
    # print(array_data)
    with open(f_to,'w') as fp:
        [fp.write(str(arr) + '\n') for arr in array_data]
        fp.close()

def txt_to_array(f_from,f_to):
    with open(f_from,'r',encoding='utf-8')as f:
        data = str(f.readlines()).replace('\\n','').replace(' ','')
    # print(data)
    with open(f_to, 'w') as fp:
        fp.write(data)
        fp.close()





if __name__ == '__main__':
   # array_to_txt(file_array,file_w_txt)
    txt_to_array(file_txt,file_w_array)
