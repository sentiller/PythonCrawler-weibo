# 静态爬虫 requests模拟get post等操作

import requests
import urllib
from urllib.parse import urlencode

# url = 'https://s.weibo.com/weibo?q=%23+ urlencode({"wd": "23岁女生在货拉拉车上跳窗身亡"}%23'
url = 'https://s.weibo.com/weibo?q=%2323%E5%B2%81%E5%A5%B3%E7%94%9F%E5%9C%A8%E8%B4%A7%E6%8B%89%E6%8B%89%E8%BD%A6%E4%B8%8A%E8%B7%B3%E7%AA%97%E8%BA%AB%E4%BA%A1%23'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
response = requests.get(url,headers)
# response.encoding = 'utf-8'
# print(response)  # <Response [200]>
# print(response.status_code)  # 200
print(response.text)
# print(type(response.text))  # <class 'str'>
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.text)