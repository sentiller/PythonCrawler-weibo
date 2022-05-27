# weibo.com
# 没有保存cookie的功能
# 绕不过扫码登录这道坎， 执行失败
from selenium import webdriver
from time import sleep
import json


def web_initial():
    web = webdriver.Firefox()
    web.maximize_window()
    web.get(
        'https://weibo.com/login.php')
    return web


def login(web):
    with open('cookies.json', 'r', encoding='utf8') as f:
        # listCookies = json.loads(f.read())
        listCookies = json.loads(f.read())
        # print(listCookies)
    # 往web里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'domain': '.weibo.com',
            'httpOnly': False,
            'HostOnly': False,
            'sameSite': "None"
        }
        web.add_cookie(cookie_dict)
    sleep(3)
    web.refresh()  # 刷新网页,cookies才成功

if __name__ == "__main__":
    web = web_initial()
    login(web)
