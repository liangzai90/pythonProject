print("\n--------------------------chap3.1---------------------------------------")
# HTTPResponse 常用的方法与属性获取信息
import urllib.request   # 导入request子模块
url = "https://www.python.org/"
response = urllib.request.urlopen(url=url)  # 发送网络请求
print("响应状态码为：",response.status)
print("响应头所有信息为：",response.getheaders())
print("响应头指定信息为：",response.getheader("Accept-Ranges"))
print("response is :", response)
#print("Python官网HTML代码如下：\n",response.read().decode("utf-8")) ## 读取html代并进行 utf-8 解码




print("\n--------------------------chap3.2---------------------------------------")
# 使用 urlopen() 方法发送 POST 请求
"""
urlopen()方法在默认的情况下发送的是GET请求，如果要发送POST请求，可以为其设置data参数，该参数是bytes类型
"""
import urllib.request  ## 导入 urllib.request 模块
import urllib.parse   ## 导入 urllib.parse模块
url = "https://www.httpbin.org/post"   # post 请求测试地址
data = bytes(urllib.parse.urlencode({'hello':'python'}), encoding='utf-8')
response = urllib.request.urlopen(url=url, data= data)  #发送网络请求
print(response.read().decode('utf-8'))
#url2 = "https://www.python.org/"
#response2 = urllib.request.urlopen(url=url2, timeout = 0.1) # 发送网络请求，设置超时时间为0.1秒
#print(response2.read().decode('utf-8'))




print("\n--------------------------chap3.3---------------------------------------")
# 捕获超时异常，处理网络超时
import urllib.request  # 导入urllib.request模块
import urllib.error   #导入urllib.error模块
import socket         #导入 socket 模块
#url = "https://www.python.org/"
url = "https://www.google.com/"
try:
    # 发送网络请求，设置超时时间为0.1秒
    response = urllib.request.urlopen(url=url,timeout=0.1)
    print(response.read().decode("utf-8"))  # 读取html代码并进行utf-8解码
except urllib.error.URLError as error :
    if isinstance(error.reason, socket.timeout):   #判断异常是否为超时异常
        print("当前任务已超时，即将执行下一个任务！")
    print("error is :", error.reason)




print("\n--------------------------chap3.4---------------------------------------")
# 设置请求头信息
"""
通过Request类构造一个带有headers请求头信息的Request对象，然后为urlopen()方法传入Request对象，再进行网络请求的发送
"""
import urllib.request
import urllib.parse
url = "https://www.httpbin.org/post"  #请求地址
# url = "https://www.baidu.com/"
# 定义请求头信息
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
# 将表单数据转换为bytes类型，并设置编码方式为utf-8
data = bytes(urllib.parse.urlencode({'hello':'python'}), encoding='utf-8')
#创建request对象
r = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
#r = urllib.request.Request(url=url)  ## 不带请求头数据情况
#r = urllib.request.Request(url=url,headers = headers)  ## 带请求头数据情况

response = urllib.request.urlopen(r)    #发送网络请求
print(response.read().decode('utf-8'))  #读取html代码并进行utf-8编码



print("\n--------------------------chap3.5---------------------------------------")
# 发送 POST 请求实现网页的模拟登陆，测试地址： http://site2.rjkflm.com:666/
import urllib.request    # 导入urllib.request模块
import urllib.parse      # 导入urllib.parse模块
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'  #登陆请求地址
# 将表单数据转换为 bytes 类型，并设置编码方式为 utf-8
data = bytes(urllib.parse.urlencode({'username':'henry','password':'heliang1990'}), encoding='utf-8')
print("data is :",data)
# 创建request对象
r = urllib.request.Request(url=url,data=data,method='POST')
response = urllib.request.urlopen(r)  # 发送网络请求
print(response.read().decode('utf-8'))  # 读取html代码并进行utf-8解码




print("\n--------------------------chap3.6---------------------------------------")
# 实现在模拟登陆过程中获取Cookie信息
"""
在获取Cookie信息的时候，需要创建一个CookieJar对象，然后生成Cookie处理器，接着创建opener对象，
再通过opener.open()方法发送登录请求，登录成功之后获取Cookie内容
"""
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
if response2 == '登录成功！':  # 注意，这里有感叹号
    print("-----success-----\n")
    for i in cookie:   # 循环遍历 Cookie 内容
        print("iii:",i);
        print(i.name + '=' + i.value)  # 打印登录成功的 Cookie 信息




print("\n--------------------------chap3.7---------------------------------------")
# 将Cookie信息保存为 LWP 格式的文件
"""
如果要将Cookie信息保存为LWP格式的Cookie文件，
需要创建LWPCookieJar对象，
然后通过 cookie.save() 方法将Cookie信息保存成文件
"""
import urllib.request  # 导入urllib.request模块
import urllib.parse   #导入urllib.parse模块
import http.cookiejar   #导入 http.cookiejar 子模块
import json           #导入json模块
# 将 Cookie 信息保存为 LWP 格式的文件
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
    print("cookie save success")




print("\n--------------------------chap3.8---------------------------------------")
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
# print(response.read().decode("utf-8"))   #打印登录后页面的html代码




print("\n--------------------------chap3.9---------------------------------------")
# 使用 urllib模块设置 代理IP
"""
使用Urllib模块设置代理IP，首先要创建ProxyHandler对象，其参数为字典类型的代理IP，
键名为协议类型（如HTTP 或者 HTTPS），值为代理链接。
然后利用 ProxyHandler 对象与build_opener()方法构件一个新的opener对象，
最后再发送网络请求即可。
"""
import urllib.request           # 导入 urllib.request 模块
url = "https://www.httpbin.org/get"   # 网络请求
# 创建代理 IP
proxy_handler =  urllib.request.ProxyHandler({"https":"58.220.95.114:10053"})  ##这里代理IP失效了
# 创建opener对象
opener = urllib.request.build_opener(proxy_handler)
try:
    response = opener.open(url, timeout =2)  # 发送网络请求
except urllib.error.URLError as error :
    print("chap3.9---error:",error.reason)
#print(response.read().decode("utf-8"))  # 打印返回内容




print("\n--------------------------chap3.10---------------------------------------")
# 调用 reason 属性处理 URLError 异常
"""
URLError类中提供了一个reason属性，可以通过这个属性了解出现异常的原因。
"""
import urllib.request   # 导入 urllib.request模块
import urllib.error     # 导入 urllib.error 模块
try:
    # 向不存在的网络地址发起请求
    response = urllib.request.urlopen("http://site2.rjkflm.com:666/123index.html")
except urllib.error.URLError as error:   # 捕获 异常信息，
    #打印异常原因
    print("chap3.10----error:",error.reason)




print("\n--------------------------chap3.11---------------------------------------")
# 使用 HTTPError 类捕获异常
import urllib.request   # 导入urllib.request模块
import urllib.error     #导入 urllib.error模块
try:
    #向不存在的网络地址发送请求
    response = urllib.request.urlopen("http://site2.rjkflm.com:666/123index.html")
    print(response.status)
except urllib.error.HTTPError as error:  # 捕获异常信息
    print("状态码为：",error.code)   #打印状态码
    print("异常信息为：",error.reason)   #打印异常原因
    print("请求头信息如下：",error.headers)   #打印请求头




print("\n--------------------------chap3.12---------------------------------------")
# 双重异常的捕获
"""
由于HTTPError是URLError的子类，有时HTTPError类会有捕获不到的异常，
所以可以先捕获子类HTTPError的异常，然后再去捕获父类URLError的异常，
这样就可以起到双重保险的作用
"""
import urllib.request   # 导入urllib.request模块
import urllib.error     #导入urllib.error模块
try:
    #向不存在的网络地址发送请求
    response = urllib.request.urlopen("https://www.python.org/666",timeout=0.1)
except urllib.error.HTTPError as error:   #HTTPError捕获异常信息
    print("状态码为：", error.code)   # 打印状态码
    print("HTTPError异常信息为：",error.reason)  #打印异常原因
    print("请求头信息如下：\n",error.headers)  # 打印请求头
except urllib.error.URLError as error:   # URLError捕获异常信息
    print("URLError异常信息为：",error.reason)




print("\n--------------------------chap3.13---------------------------------------")
# 使用urlparse()方法拆分 URL 的实例代码
"""
urllib.parse.urlparse(urlstring, scheme="",allow_fragments=True)
urlstring:需要拆分的URL，该参数为必选参数
scheme：可选参数，表示需要设置的默认协议。
allow_fragments:可选参数，如果该参数设置为False,表示忽略 fragment这部分内容，默认为True.

从运行结果来看，调用urlparse()方法返回一个ParseResult对象，由6部分组成：
scheme表示协议
netloc表示域名
path表示访问的路径
params表示参数
query表示查询条件
fragment表示片段标识符
"""
import urllib.parse #导入urllib.parse模块
parse_result = urllib.parse.urlparse("https://docs.python.org/3/library/urllib.parse.html")
print(type(parse_result))  #打印类型
print(parse_result)  #打印拆分后的结果

print("scheme值为：",parse_result.scheme)
print("netloc值为：",parse_result.netloc)
print("path值为：",parse_result.path)
print("params值为：",parse_result.params)
print("query值为：",parse_result.query)
print("fragment值为：",parse_result.fragment)




print("\n--------------------------chap3.14---------------------------------------")
# 使用 urlsplit() 方法拆分 URL
import urllib.parse    #导入urllib.parse模块
#需要拆分的URL
url = "https://docs.python.org/3/library/urllib.parse.html"
print(urllib.parse.urlsplit(url))  # 使用urllib.split()方法拆分 URL ,返回的结果中，params合并到了path当中
print(urllib.parse.urlparse(url))  # 使用urllib.parse()方法拆分 URL

urlsplit = urllib.parse.urlsplit(url)
print(urlsplit.scheme)  #属性获取拆分后的协议值
print(urlsplit[0])      #索引获取拆分后的协议值




print("\n--------------------------chap3.15---------------------------------------")
# 使用 urlunparse() 方法组合 URL
"""
urllib.parse.urlunparse(parts)
parts:表示用于组合URL的可选迭代对象
可迭代参数必须是 6 个
"""
import urllib.parse  #导入urllib.parse模块
list_url = ["https","docs.python.org", "3/library/urllib.parse.html","","",""]
tuple_url = ("https","docs.python.org","3/library/urllib.parse.html","","","")
dict_url = {"scheme":"https","netloc":"docs.python.org","path":"3/library/urllib.parse.html","params":"","query":"","fragment":""}

print("组合列表类型的URL:",urllib.parse.urlunparse(list_url))
print("组合元组类型的URL:",urllib.parse.urlunparse(tuple_url))
print("组合字典类型的URL:",urllib.parse.urlunparse(dict_url.values()))




print("\n--------------------------chap3.16---------------------------------------")
# 使用 urlunsplit() 方法组合 URL
"""
urllib.parse.urlunsplit(parts)
parts:表示用于组合URL的可迭代对象
可迭代参数必须是 5 个
"""
import urllib.parse    # 导入urllib.parse模块
list_url = ["https","docs.python.org", "3/library/urllib.parse.html","",""]
tuple_url = ("https","docs.python.org","3/library/urllib.parse.html","","")
dict_url = {"scheme":"https","netloc":"docs.python.org","path":"3/library/urllib.parse.html","query":"","fragment":""}

print("组合列表类型的URL:", urllib.parse.urlunsplit(list_url))
print("组合元祖类型的URL:",urllib.parse.urlunsplit(tuple_url))
print("组合字典类型的URL:", urllib.parse.urlunsplit(dict_url.values()))




print("\n--------------------------chap3.17---------------------------------------")
# 使用 urljoin() 方法连接 URL
"""
urllib.parse.urljoin(base, url, allow_fragments = True)
base:表示基础连接
url:表示新的链接
allow_fragment：可选参数，如果该参数设置为 False，表示忽略 fragment这部分内容，默认为 True
"""
import urllib.parse    # 导入urllib.parse模块
base_url = "https://docs.python.org"   #定义基础链接
# 第2个参数不完整时
print(urllib.parse.urljoin(base_url,"3/library/urllib.parse.html"))
#第2个参数完成时，直接返回第2个参数的链接
print(urllib.parse.urljoin(base_url,"https://docs.python.org/3/library/urllib.parse.html#url-parsing"))





print("\n--------------------------chap3.18---------------------------------------")
# 使用 urlencode() 方法编码请求参数
import urllib.parse   #导入urllib.parse模块
base_url = "http://httpbin.org/get?"  #定义基础链接
params = {"name":"Henry","country":"中国","age":30}   #定义字典类型的请求参数
url = base_url + urllib.parse.urlencode(params)  #连接请求地址
print("urlencode 编码后的请求地址为：\n",url)
"""
urlencode 编码后的请求地址为： http://httpbin.org/get?name=Henry&country=%E4%B8%AD%E5%9B%BD&age=30
"""




print("\n--------------------------chap3.19---------------------------------------")
# 使用 quote() 方法编码字符串参数
import urllib.parse    #导入urllib.parse模块
#base_url = "http://httpbin.org/get?country="
base_url = "http://httpbin.org/get?"
url = base_url + "name=" + urllib.parse.quote("henry") +"&country="+ urllib.parse.quote("中国") + "&age=" + urllib.parse.quote("30") #字符串编码
print("quote 编码后的请求地址为：\n",url)
"""
quote 编码后的请求地址为： http://httpbin.org/get?name=henry&country=%E4%B8%AD%E5%9B%BD&age=30
"""




print("\n--------------------------chap3.20---------------------------------------")
# 使用 unquote() 方法解码请求参数
import urllib.parse
u = urllib.parse.urlencode({"country":"中国","age":30,"name":"henry"})  #使用urlencode编码
q = urllib.parse.quote("country=中国&age=30&name=henry")  #使用quote编码
print("urlencode编码后结果为：",u)
print("quote编码后结果为：",q)
print("对urlencode解码：",urllib.parse.unquote(u))
print("对quote解码：",urllib.parse.unquote(q))
"""
urlencode编码后结果为： country=%E4%B8%AD%E5%9B%BD&age=30&name=henry
quote编码后结果为： country%3D%E4%B8%AD%E5%9B%BD%26age%3D30%26name%3Dhenry
对urlencode解码： country=中国&age=30&name=henry
对quote解码： country=中国&age=30&name=henry
"""




print("\n--------------------------chap3.21---------------------------------------")
# 使用 parse_qs() 方法将参数转换为字典类型
import urllib.parse    #导入urllib.parse模块
#定义一个请求地址
url = "http://httpbin.org/get?name=Henry&country=%E4%B8%AD%E5%9B%BD&age=30"
print("urlsplit is what:",urllib.parse.urlsplit(url))
q = urllib.parse.urlsplit(url).query  #获取参数
q_dict = urllib.parse.parse_qs(q)  # 将参数转换为字典类型的数据
print("数据类型为：",type(q_dict))
print("转换后的数据：", q_dict)
"""
urlsplit is what: SplitResult(scheme='http', netloc='httpbin.org', path='/get', query='name=Henry&country=%E4%B8%AD%E5%9B%BD&age=30', fragment='')
数据类型为： <class 'dict'>
转换后的数据： {'name': ['Henry'], 'country': ['中国'], 'age': ['30']}
"""



print("\n--------------------------chap3.22---------------------------------------")
# 使用 parse_qsl() 方法将参数转换为列表
import urllib.parse      #导入urllib.parse模块
str_params = "name=Henry&country=%E4%B8%AD%E5%9B%BD&age=30"  #字符串参数
list_params = urllib.parse.parse_qsl(str_params)  #将字符串参数转为 元组 所组成的列表
print("list_params数据类型为：",type(list_params))
print("list_params转换后的数据：", list_params)
"""
list_params数据类型为： <class 'list'>
list_params转换后的数据： [('name', 'Henry'), ('country', '中国'), ('age', '30')]
"""
