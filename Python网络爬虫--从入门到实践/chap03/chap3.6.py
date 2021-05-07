import urllib.request     # 导入urllib.request 模块
import urllib.parse       # 导入urllib.parse模块
import http.cookiejar    # 导入http.cookiejar 模块
import json             # 导入json模块
url ='http://site2.rjkflm.com:666/index/index/chklogin.html'
# 将表单数据转换为 bytes类型，并设置编码方式为 utf-8
data = bytes(urllib.parse.urlencode({'username':'henry','password':'heliang1990'}), encoding='utf-8')
cookie = http.cookiejar.CookieJar()  # 创建 CookieJar对象
cookie_processor = urllib.request.HTTPCookieProcessor(cookie)   #生成Cookie处理器
opener = urllib.request.build_opener(cookie_processor)  # 创建opener对象
response = opener.open(url, data = data)   # 发送登录请求
response1 = json.loads(response.read().decode('utf-8'))
print("response1:", response1)
print("cookie:",cookie)
response2 = response1['msg']
if response2 == '登录成功！':  ## 注意，这里有感叹号
    print("-----success-----\n")
    for i in cookie:   # 循环遍历 Cookie 内容
        print("iii:",i);
        print(i.name + '=' + i.value)  # 打印登录成功的 Cookie 信息
