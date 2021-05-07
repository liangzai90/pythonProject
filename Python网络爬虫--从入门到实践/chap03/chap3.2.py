import urllib.request  ## 导入 urllib.request 模块
import urllib.parse   ## 导入 urllib.parse模块
url = "https://www.httpbin.org/post"   # post 请求测试地址
data = bytes(urllib.parse.urlencode({'hello':'python'}), encoding='utf-8')
response = urllib.request.urlopen(url=url, data= data)  #发送网络请求
# print(response.read().decode('utf-8'))

url2 = "https://www.python.org/"
response2 = urllib.request.urlopen(url=url2, timeout = 0.1) # 发送网络请求，设置超时时间为0.1秒
print(response2.read().decode('utf-8'))

'''
C:\ProgramData\Anaconda3\python.exe F:/python/202105Py/chap03/chap3.2.py
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
    "User-Agent": "Python-urllib/3.8", 
    "X-Amzn-Trace-Id": "Root=1-6090ceb8-26e973673745112356b4cca7"
  }, 
  "json": null, 
  "origin": "112.10.95.69", 
  "url": "https://www.httpbin.org/post"
}
'''