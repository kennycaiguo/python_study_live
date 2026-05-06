"""
urllib builtin module
"""
from urllib.parse import urlparse

o = urlparse("https://docs.python.org/zh-cn/3/library/urllib.parse.html#module-urllib.parse")

print('scheme  :', o.scheme)
print('netloc  :', o.netloc)
print('path    :', o.path)
print('params  :', o.params)
print('query   :', o.query)
print('fragment:', o.fragment)
print('hostname:', o.hostname)

""" output
scheme  : https
netloc  : docs.python.org
path    : /zh-cn/3/library/urllib.parse.html
params  : 
query   : 
fragment: module-urllib.parse
hostname: docs.python.org
"""