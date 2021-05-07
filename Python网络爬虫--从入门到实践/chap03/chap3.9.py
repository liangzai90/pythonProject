# 使用 urllib模块设置 代理IP
import urllib.request           # 导入 urllib.requestt 模块
url = "https://www.httpbin.org/get"   # 网络请求
# 创建代理 IP
proxy_handler =  urllib.request.ProxyHandler({"https":"58.220.95.114:10053"})
# 创建opener对象
opener = urllib.request.build_opener(proxy_handler)
response = opener.open(url, timeout =2)  # 发送网络请求
print(response.read().decode("utf-8"))  # 打印返回内容
