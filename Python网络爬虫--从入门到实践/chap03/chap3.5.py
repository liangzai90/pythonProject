import urllib.request
import urllib.parse
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
# 将表单数据转换为 bytes 类型，并设置编码方式为 utf-8
data = bytes(urllib.parse.urlencode({'username':'henry','password':'heliang1990'}), encoding='utf-8')
print("data is :",data,"\n")
# 创建request对象
r = urllib.request.Request(url=url,data=data,method='POST')
response = urllib.request.urlopen(r)  # 发送网络请求
print(response.read().decode('utf-8'))  # 读取html代码并进行utf-8解码
