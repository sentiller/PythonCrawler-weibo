# weibo.cn
# 实现weibo.cn的自动登录
import requests
import json

def login():
    login_url = 'https://passport.weibo.cn/signin/login'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }
    body = {
        "fClientid": "18520780424",
        "fCode": "111111qq"
    }
    try:
        res = requests.post(url=login_url, headers=headers, data=body)


        input('验证成功后输入：')

        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie
    except Exception as err:
        print('获取cookie失败：\n{0}'.format(err))


cookie = login()
json_cookie = json.dumps(cookie)  # 转换成字符串保存
with open("weibocnCookie.json", "w") as f:
    f.write(json_cookie)
print("cookie保存成功")
