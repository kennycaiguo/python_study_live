"""
urllib builtin module
"""

# # 编码quote(string)
# from urllib import parse

# url = "http://www.baidu.com/s?wd={}"
# words = "爬虫"

# #quote()只能对字符串进行编码
# query_string = parse.quote(words)
# url = url.format(query_string)
# print(url) # http://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB

# # 编码urlencode() quote()只能对字符串编码，而urlencode()可以对查询字符串进行编码
# # 导入parse模块
# from urllib import parse

# #调用parse模块的urlencode()进行编码
# query_string = {'wd':'爬虫'}
# result = parse.urlencode(query_string)

# # format函数格式化字符串，进行url拼接
# url = 'http://www.baidu.com/s?{}'.format(result)
# print(url) # http://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB

# 解码 unquote(string)
# 解码就是对编码后的url进行还原。
from urllib import parse
string = '%E7%88%AC%E8%99%AB' 
result = parse.unquote(string)
print(result) # 爬虫