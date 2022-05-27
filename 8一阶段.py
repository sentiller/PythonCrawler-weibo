# weibo。com
# 通过6获取cookie 7则可以自动登录
# 本代码开始访问
# 名词用小写连贯 动词用下划线分开
# 找到话题下微博，并保存对应的链接，保存在weibo.txt
# weibo.com
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# url = 'https://s.weibo.com/weibo?q=%2323岁女生在货拉拉车上跳窗身亡%23'
# subjectlist = [
#     '23岁女生在货拉拉车上跳窗身亡',
#     '货拉拉涉事司机被批捕',
#     '货拉拉跳窗身亡女孩搬家视频曝光',
#     '法医称货拉拉跟车女孩跳窗可能性不大',
#     '央视评女孩跳车身亡货拉拉难辞其咎',
#     '警方还原货拉拉乘客跳窗案经过',
#     '家属回应女孩跳货拉拉车窗身亡',
#     '央视评货拉拉事件中似是而非的声音',
#     '央视复盘货拉拉事件',
#     '货拉拉道歉',
#     '如何看待货拉拉司机被批捕',
#     '3D还原货拉拉坠车事件经过',
#     '货拉拉回应女子跳窗身亡',
#     '货拉拉涉事司机涉嫌过失致人死亡罪',
#     '货拉拉司机家属回应女子跳窗身亡'
# ]

web = webdriver.Firefox()
# web.maximize_window()

class CookieSpider:
    def get_QR(self):
        web.get('https://weibo.com/login.php')
        web.maximize_window()
        web.implicitly_wait(10)
        web.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()

    def get_cookie(self):
        cookie_ = web.get_cookies()  # 获取cookies
        json_cookie = json.dumps(cookie_)  # 转换成字符串保存
        with open("微博cookie.txt", "w") as f:
            f.write(json_cookie)
        print("cookie保存成功")

    def post_cookie(self):
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
    cs = CookieSpider()
    while(True):
        option = input('输入你要执行的操作：1登录,2自动登录,3其他操作')
        if(option == '1'):
            cs.get_QR()
            input('扫码完成后输入，进入后面程序')
            cs.get_cookie()
        elif(option == '2'):
            cs.post_cookie()
            subjectlist = [
                '23岁女生在货拉拉车上跳窗身亡',
                '货拉拉涉事司机被批捕',
                '货拉拉跳窗身亡女孩搬家视频曝光',
                '法医称货拉拉跟车女孩跳窗可能性不大',
                '央视评女孩跳车身亡货拉拉难辞其咎',
                '警方还原货拉拉乘客跳窗案经过',
                '家属回应女孩跳货拉拉车窗身亡',
                '央视评货拉拉事件中似是而非的声音',
                '央视复盘货拉拉事件',
                '货拉拉道歉',
                '如何看待货拉拉司机被批捕',
                '3D还原货拉拉坠车事件经过',
                '货拉拉回应女子跳窗身亡',
                '货拉拉涉事司机涉嫌过失致人死亡罪',
                '货拉拉司机家属回应女子跳窗身亡'
            ]
            for i in range(0, len(subjectlist)):
                el = subjectlist[i]
                print('当前话题：' + el)
                page = 0
                urlhrefs = []
                while(True):
                    page += 1
                    url = 'https://s.weibo.com/weibo?q=%23' + el + '%23&page=' + str(page)
                    web.get(url)
                    urls = web.find_elements(By.XPATH, '//*[@class="content"]/p[1]/a[1]')
                    if(urls == []):
                        break
                    print('第'+str(page)+'页,有'+str(len(urls))+'条微博。链接如下：')
                    for u in urls:
                        href = u.get_attribute("href")
                        print(href)
                        urlhrefs.append(href)
                urlhrefsstr = '\n'
                with open('weiboAll.txt', "a", encoding='utf-8') as f:
                    f.write(urlhrefsstr.join(urlhrefs))
                    f.write('\n')
web.close()