# 使用 Cookie 信息登录并获取页面中的信息
import urllib.request
import http.cookiejar
# 登录后页面的请求地址
url = "http://site2.rjkflm.com:666/index/index/index.html"
cookie_file = "cookie.txt"  # Cookie 文件
cookie = http.cookiejar.LWPCookieJar()   # 创建 LWPCookieJar 对象
# 读取Cookie文件内容
cookie.load(cookie_file, ignore_expires=True, ignore_discard=True)
# 生成 Cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
#创建 opener 对象
opener = urllib.request.build_opener(handler)
response = opener.open(url)  # 发送网络请求
print(response.read().decode("utf-8"))   #打印登录后页面的html代码

