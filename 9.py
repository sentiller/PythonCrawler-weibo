# weibo.cn
# 单条微博的评论读取
# 获取所有评论并保存在txt中
# 在10.py中读取该txt并且生成词云
# 没有自动登录， 本程序不能执行，只能读取第一页

import time
import requests
from bs4 import BeautifulSoup


headers ={

'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

'accept-language':'zh-CN,zh;q=0.9',

'cache-control':'max-age=0',

'cookie':'ALF=1587263529; _T_WM=98012988932; SUB=_2A25zcBXjDeRhGeBI6lMS-SnNwjiIHXVQmrurrDV6PUJbkdANLWLVkW1NRryekjjW7K01YTgDTWaldRtUKap4aqOS; SUHB=09P9rXjh_9wMmP; SCF=AgOabTn6Fb5gHUI6gnRn-uXK4LjyzBuKwBvG7NVXp5smWGjQ-X0wM7rEFzDX9QI5nZ3OD0lQwDXAU3nlqvwVeMg.; SSOLoginState=1584686515; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4484509997073735%26luicode%3D20000061%26lfid%3D4484509997073735',

'upgrade-insecure-requests':'1',

'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

}

requests.post()


for i in range(1,20):

    url = 'https://weibo.cn/comment/LfJbPDCgM?uid=2656274875&rl=0&gid=10001&page='+str(i)+'display=0&retcode=6102'

    response = requests.get(url,headers=headers)
    # response = requests.get('https://weibo.cn/pub/')

    html = response.text
    # print(html)

    soup = BeautifulSoup(html,'html.parser')
    comment_list = soup.find_all(class_='ctt')

    with open('comments.txt','a') as writer: # 注意是append追加形式
        for comment in comment_list:  # 遍历评论
            # 获取评论信息
            com = comment.get_text()
            print(com)
            # 评论中有："回复@断流年举樽祭:因为贵" 只要：后面的内容
            if ":" in com:
                com = com.split(":")[-1]
            # 写入文件，注意一个评论一行
            writer.write(com+'\n')

    print('保存完第%d页'% i)
    time.sleep(3)