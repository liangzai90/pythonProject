import urllib.request  # 导入urllib.request模块
import urllib.error   #导入urllib.error模块
import socket         #导入 socket 模块

url = "https://www.python.orga"
try:
    # 发送网络请求，设置超时时间为0.1秒
    response = urllib.request.urlopen(url=url,timeout=0.1)
    print(response.read().decode("utf-8"))  # 读取html代码并进行utf-8解码
except urllib.error.URLError as error :
    if isinstance(error.reason, socket.timeout):   #判断异常是否为超时异常
        print("当前任务已超时，即将执行下一个任务！")
    print("error is :", error.reason)