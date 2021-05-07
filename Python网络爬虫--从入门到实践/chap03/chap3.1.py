import urllib.request   # 导入request子模块
url = "https://www.python.org/"
response = urllib.request.urlopen(url=url)  # 发送网络请求
print("响应状态码为：",response.status)
print("响应头所有信息为：",response.getheaders())
print("响应头指定信息为：",response.getheader("Accept-Ranges"))
print("response is :", response)
print("Python官网HTML代码如下：\n",response.read().decode("utf-8")) ## 读取html代并进行 utf-8 解码


