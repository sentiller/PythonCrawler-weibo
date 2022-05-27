# weibo.com
# 登录并且人为扫码
# 将cookie保存在cookies.json
# 在7.py中使用

from selenium import webdriver
from selenium.webdriver.common.by import By
import json

web = webdriver.Firefox()


class CookieSpider:
    def get_QR(self):
        web.get('https://weibo.com/login.php')
        # web.maximize_window()
        web.implicitly_wait(10)
        web.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()

    def get_cookie(self):
        cookie_ = web.get_cookies()  # 获取cookies
        json_cookie = json.dumps(cookie_)  # 转换成字符串保存
        with open("微博cookie.txt", "w") as f:
            f.write(json_cookie)
        print("cookie保存成功")


cs = CookieSpider()
cs.get_QR()
input()  # 扫码完成后输入，进入后面程序
cs.get_cookie()

web.close()