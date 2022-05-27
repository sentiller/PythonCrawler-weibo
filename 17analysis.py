#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
import re
#接口地址
url ="http://ltpapi.xfyun.cn/v1/sa"
#开放平台应用ID
x_appid = "acb16291"
#开放平台应用接口秘钥
api_key = "0ba2d5e298305f01584ffd1b737abd41"
#语言文本
# TEXT="唉...还不如不跳呢，如果没跳的话不管怎样也许会有一线生机..."

start = 0

def get_result(text):
    body = urllib.parse.urlencode({'text': text}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    # time.sleep(1)
    result = urllib.request.urlopen(req)
    result = result.read()
    # print(result.decode('utf-8'))
    result = result.decode('utf-8')
    resultjson = json.loads(result) # type == dict
    if(resultjson['code']!='0'):
        return result
    negative_prob = resultjson['data']['sa'][0]['negative_prob']
    neutral_prob = resultjson['data']['sa'][0]['neutral_prob']
    positive_prob = resultjson['data']['sa'][0]['positive_prob']
    sentiment = resultjson['data']['sa'][0]['sentiment'] # type == int 0：代表中性，1：代表褒义，2：代表贬义
    return negative_prob,neutral_prob,positive_prob,sentiment

def replace_char(old_string,index1,index2):
    # old_string = str(old_string)
    # 新的字符串 = 老字符串[:要替换的索引位置] + 替换成的目标字符 + 老字符串[要替换的索引位置+1:]
    new_string = old_string[:index1] + old_string[index2:]
    return new_string

def main():
    commentfile = 'commentfile222_1.txt'
    sentimentsfile = 'sentimentsfile1.txt'
    count = 0
    sentiments = open(sentimentsfile,'a',encoding='utf-8')
    with open(commentfile,'r',encoding='utf-8') as f:
        for line in f:
            count+=1
            if(count<start):
                continue
            print('当前行数：'+str(count))
            linetext = line[0:-1]
            # 删除话题
            state = 0
            pos = [0, 0]
            while (True):
                if (re.search(r'#', linetext) == None):
                    break
                for i in re.finditer(r'#', linetext):
                    if (state == 0):
                        state = 1
                        pos[0] = i.span()[0]
                    elif (state == 1):
                        pos[1] = i.span()[1]
                        linetext = replace_char(linetext, pos[0], pos[1])
                        state = 0
                        pos = [0, 0]
                        break
            linetext = ''.join(re.findall(r'[\u4e00-\u9fa5]+', linetext)) # 过滤只剩下中文
            print('有效文字：'+linetext)
            if(len(linetext)==0):
                sentiments.write('0 0 -1\n')
                print('字数为零，跳过')
                continue
            # 截取有效的500字节
            linetextbytes = linetext.encode('utf-8')
            cutlinetextbytes = linetextbytes[0:500]
            cutlinetext = cutlinetextbytes.decode('utf-8', errors='ignore')
            print('字节长度：'+str(len(cutlinetextbytes)))
            negative_prob,neutral_prob,positive_prob,senti = get_result(cutlinetext)
            if(type(senti)==int):
                print('感情结果：'+str(negative_prob)+" "+str(neutral_prob)+" "+str(positive_prob)+" "+str(senti))
                sentiments.write(str(negative_prob)+" "+str(neutral_prob)+" "+str(positive_prob)+" "+str(senti)+'\n')
            else:
                print(senti)
                break
    sentiments.close()


if __name__ == '__main__':
    main()
