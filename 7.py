# weibo.com
# 读取6.py保存的cookies.json
# 实现自动登录
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = webdriver.Firefox()
web.maximize_window()


def post_cookie():
    web.get('https://weibo.com/login.php')
    with open('微博cookie.txt', "r", encoding='utf-8') as f:
        cookies = json.loads(f.read())

    for cookie in cookies:
        data = {
            'domain': '.weibo.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        web.add_cookie(data)
    web.implicitly_wait(10)
    web.refresh()  # 刷新一下页面，就能成功登录


def post_content(your_content):
    web.find_element(By.XPATH, '//*[@id="homeWrap"]/div[1]/div/div[1]/div/textarea').send_keys(your_content)
    web.find_element(By.XPATH, '//*[@id="homeWrap"]/div[1]/div/div[4]/div/button').click()
    print("发帖成功")

def search_content(your_content):
    input= web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/span/form/div/input')
    input.send_keys(your_content)
    input.click()
    input.send_keys(Keys.ENTER)
    print("搜索成功")


if __name__ == '__main__':
    post_cookie()
    your_content = input("请输入你想要发送的内容:")
    search_content(your_content)
    # post_content(your_content)
web.close()