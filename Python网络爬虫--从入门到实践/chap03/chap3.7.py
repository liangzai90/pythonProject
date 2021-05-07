import urllib.request
import urllib.parse
import http.cookiejar
import json

url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
data = bytes(urllib.parse.urlencode({'username':'henry','password':'heliang1990'}),encoding='utf-8')
cookie_file = 'cookie.txt'     ## 保存cookie文件
cookie = http.cookiejar.LWPCookieJar(cookie_file) # 创建LWPCookieJar对象
#生成 cookie 处理器
cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
# 创建 opener 对象
opener = urllib.request.build_opener(cookie_processor)
response = opener.open(url, data=data)
response = json.loads(response.read().decode('utf-8'))['msg']
if response =="登录成功！":
    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存 Cookie 文件

