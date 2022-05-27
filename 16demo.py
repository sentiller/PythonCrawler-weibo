#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
#接口地址
url ="http://ltpapi.xfyun.cn/v1/sa"
#开放平台应用ID
# x_appid = "acb16291"
x_appid = "1ba03812"
#开放平台应用接口秘钥
# api_key = "0ba2d5e298305f01584ffd1b737abd41"
api_key = "37de3791c3f464f4321f7b60b93b500b"
#语言文本
TEXT="回应个屁啊？！这回应多少天前的了？？？"


def main():
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    result = result.decode('utf-8')
    resultjson = json.loads(result)
    print(resultjson)
    print(type(resultjson))
    negative_prob = resultjson['data']['sa'][0]['negative_prob']
    sentiment = resultjson['data']['sa'][0]['sentiment']
    print(sentiment)
    print(type(sentiment))
    return


if __name__ == '__main__':
    main()
