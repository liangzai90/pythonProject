import urllib.request
import urllib.parse
# url = "https://www.httpbin.org/post"
url = "https://www.baidu.com/"
# 定义请求头信息
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
# 将表单数据转换为bytes类型，并设置编码方式为utf-8
data = bytes(urllib.parse.urlencode({'hello':'python'}), encoding='utf-8')
#创建request对象
#r = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
#r = urllib.request.Request(url=url)  ## 不带请求头数据情况
r = urllib.request.Request(url=url,headers = headers)  ## 带请求头数据情况

response = urllib.request.urlopen(r)    #发送网络请求
print(response.read().decode('utf-8'))  #读取html代码并进行utf-8编码

'''
C:\ProgramData\Anaconda3\python.exe F:/python/202105Py/chap03/chap3.4.py
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "hello": "python"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "12", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "www.httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6090d7cb-5e0593de17575fa75e7342dd"
  }, 
  "json": null, 
  "origin": "112.10.95.69", 
  "url": "https://www.httpbin.org/post"
}
'''