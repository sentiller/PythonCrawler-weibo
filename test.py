# import re
# import pandas as pd
#
# # str = 'nihao , wo shi shabi1000'
# # time = '21-3-2 24:00'
# # reg = r'shabi(.*?).*'
# # reg1 = r'(.*?) (.*?)'
# # span = re.search(reg, str).span()
# # d = 5
#
# # line = "nihao" \
# #        "wohao "
# # print(line)
# # print(line.replace('\n',''))
# # print(span)
# # print(span[0])
# # print(str[span[0]+d: span[1]])
# # print(time)
# # # print(re.search(reg1, time))
# # span = re.search(reg1, time).span()
# # print(span)
# # date = time[span[0]: span[1]-1]
# # print(date)
# #
# # dict = {'21-2-21': 63, '21-2-22': 978, '21-2-23': 966, '21-2-24': 1505, '21-2-25': 745, '21-2-26': 995, '21-2-27': 56, '21-2-28': 32, '21-3-1': 207, '21-3-2': 414, '21-3-3': 1405, '21-3-4': 2167, '21-3-5': 849, '21-3-6': 469, '21-3-7': 178, '21-3-8': 148, '21-3-9': 167, '21-3-10': 81, '21-3-11': 51, '21-3-12': 31, '21-3-13': 38, '21-3-14': 20, '21-3-15': 19, '21-3-16': 12, '21-3-17': 18, '21-3-18': 6, '21-3-19': 14, '21-3-20': 9, '21-3-21': 3, '21-3-22': 4, '21-3-23': 5, '21-3-24': 5, '21-3-25': 4, '21-3-26': 2, '21-3-27': 6, '21-3-28': 9, '21-3-29': 2, '21-3-30': 4, '21-3-31': 1, 'other': 990}
# # df = pd.DataFrame.from_dict(dict,orient='index')
# # print(df)
#
# # from datetime import  timedelta
# # import pandas as pd
# # from datetime import datetime,timedelta
# # # now = datetime.now()
# # now = pd.to_datetime('2021-03-01')
# # # past = datetime(2010,11,12,13,14,15,16)
# # past = pd.to_datetime('2021-02-20')
# # timespan = now - past
# # timenaps = past - now
# # print(now)
# # print(timespan)
# # print(timenaps)
# # print(now<past)
#
# # f = open('stopwords.txt','r',encoding='utf=8')
# # stop = []
# # for line in f:
# #     word = line[0:-1]
# #     stop.append(word)
# # f.close()
# # print(stop)
# # str = '#23岁女生在货拉拉车上跳窗身亡##货拉拉跳窗身亡女孩搬家视频曝光#我最惊险的一次是在邮轮工作的经历，当时到达阿布扎比港口中午休息的时候我下船准备去附近的超市买点生活用品，因为那个时间点人比较少，'
# def replace_char(old_string,index1,index2):
#     # old_string = str(old_string)
#     # 新的字符串 = 老字符串[:要替换的索引位置] + 替换成的目标字符 + 老字符串[要替换的索引位置+1:]
#     new_string = old_string[:index1] + old_string[index2:]
#     return new_string
# str = '#货拉拉跳窗身亡女孩搬家视频曝光#女孩#@123i love你好'
# state = 0
# pos = [0,0]
# str1 = ''
# while(True):
#     if(re.search(r'#', str) == None):
#         break
#     for i in re.finditer(r'#', str):
#         if(state==0):
#             state = 1
#             pos[0]=i.span()[0]
#         elif(state==1):
#             pos[1]=i.span()[1]
#             str = replace_char(str,pos[0],pos[1])
#             state = 0
#             pos = [0,0]
#             break
#     # print(i.group(),i.span())
# print(str)
# li = re.findall(r'[\u4e00-\u9fa5]+', str)
# print(li)
# print(type(li))
# print(''.join(re.findall(r'[\u4e00-\u9fa5]+', str)))
# # print(result)
#
# # str_txt = '测试文本ceshi'
# # cut_bytes = str_txt.encode('utf-8')
# # print(len(cut_bytes))
# # cut_tmp = cut_bytes[:900] # 此处截取bytes长度900
# # cut_res = cut_tmp.decode('utf-8', errors='ignore')  # 按bytes截取时有小部分无效的字节，传入errors='ignore'忽略错误
# # # print('cut_res 长度 字节数', len(cut_res), len(cut_res.encode()))

# import pandas as pd
# file = 'commentfile222_1.csv'
# df = pd.read_csv(file, header=0)
# print(df.shape[0])

import random
import pandas as pd

def randomchoose(file):
    df = pd.read_csv(file, header=0)
    maxnum = df.shape[0]-1
    print(maxnum)
    li = random.sample(range(1, maxnum), maxnum-20)
    li.sort()
    print(li)
    print(len(li))
    df = df.drop(li)
    print(df)
    print(df.shape)
    df.to_csv(file,index=False)
    print('完成随机选取')
file = 'commentfile222_1.csv'
randomchoose(file)

