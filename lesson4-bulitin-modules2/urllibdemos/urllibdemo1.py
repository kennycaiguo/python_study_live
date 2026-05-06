"""
urllib builtin module
"""
from urllib import request
#导入urllib.request模块
url=request.urlopen("https://www.baidu.com")
#打开读取baidu信息
print(url.read().decode('utf-8'))
#read获取所有信息，并decode()命令将网页的信息进行解码

