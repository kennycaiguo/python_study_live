"""
urllib builtin module
"""
from urllib.parse import urlunparse,urlunsplit
url_compos = ['http','www.baidu.com','index.html','user= test','a=6','comment']
print(urlunparse(url_compos)) # http://www.baidu.com/index.html;user= test?a=6#comment
# urlunsplit()
url_compos = ['http','www.baidu.com','index.html','user= test','a=2']
print(urlunsplit(url_compos)) # http://www.baidu.com/index.html?user= test#a=2