# 利用8py的原理 读取weibo.com的评论
# 读取weiboAll.txt的微博链接，爬取所有评论
# 需要注意二级评论以及滑动刷新
# 先只获取一级评论吧
# weibo.com
# -- coding: utf-8 --
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import csv
import re

web = webdriver.Firefox()
web.maximize_window()

class CookieSpider:
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

weibofile = open('weibo_new3.txt', 'r', encoding='utf-8')

if __name__ == '__main__':
    cs = CookieSpider()
    cs.post_cookie()
    start = 1021
    count = 0
    for line in weibofile:
        count += 1
        print('当前微博：' + str(count))
        web.get(line)
        time.sleep(5)
        test = web.find_elements(By.XPATH,'//*[@class="vue-recycle-scroller__item-view"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]')  # 判断有没有评论
        if(len(test)==0): # 如果没有评论，则直接退出
            continue
        commentfile = open('./commentfile222_' + str(count) + '.csv', 'a', encoding='utf-8')
        csvwriter = csv.writer(commentfile)
        csvwriter.writerow(['text', 'time'])
        time.sleep(2)
        # web.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        text_1 = web.find_element(By.CLASS_NAME,'detail_wbtext_4CRf9').text
        text_1 = "".join(text_1.split())
        date_1 = web.find_element(By.CLASS_NAME,'head-info_time_6sFQg').text
        # print(text_1,date_1)
        csvwriter.writerow([text_1, date_1])

        time.sleep(2)
        web.execute_script(""" 
                (function () { 
                    var y = document.body.scrollTop; 
                    var step = 100; 
                    window.scroll(0, y); 
                    function f() { 
                        if (y < document.body.scrollHeight) { 
                            y += step; 
                            window.scroll(0, y); 
                            setTimeout(f, 800); 
                        }
                        else { 
                            window.scroll(0, y); 
                            document.title += "scroll-done";
                            document.title += y.toString(); 
                        } 
                    } 
                    setTimeout(f, 1000); 
                })(); 
                """)
        WebDriverWait(web,500,1).until(expected_conditions.title_contains('scroll-done'))
        span = re.search(r'scroll-done(.*?).*',web.title).span()
        maxy = int(web.title[span[0]+11: span[1]])
        print(maxy)
        # web.find_element(By.CSS_SELECTOR, 'div.item:nth-child(2)').click # 按时间排序
        web.execute_script("document.documentElement.scrollTo(0,0)")
        time.sleep(1)
        height = 0
        while(height<maxy):
            textlist = web.find_elements(By.XPATH, '//*[@class="vue-recycle-scroller__item-view"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]')
            textarr = []
            datelist = web.find_elements(By.XPATH, '//*[@class="vue-recycle-scroller__item-view"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
            datearr = []
            for t in textlist:
                text = t.text
                text = "".join(text.split())
                if(text == ''):
                    continue
                textarr.append(text)
            for d in datelist:
                date = d.text
                if(date == ''):
                    continue
                datearr.append(date)
            print('text: '+str(len(textarr))+' , date: '+str(len(datearr)))
            height += 800
            length = min(len(textarr), len(datearr))
            if(length == 0):
                continue
            length = min(len(textarr), len(datearr))
            for i in range(0,length):
                # print(textarr[i], datearr[i])
                csvwriter.writerow([textarr[i], datearr[i]])
            print(str(height))
            web.execute_script("document.documentElement.scrollTo(0,"+str(height)+")")
            time.sleep(1)
        # input('运行完成，输入继续')
        print('该微博完成，下一条')
        commentfile.close()
weibofile.close()
web.close()