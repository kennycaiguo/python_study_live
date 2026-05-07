#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "A.L.Kun"
__file__ = "demo02.py"
__email__ = "liu.zhong.kun@foxmail.com"
 
import fileinput
from glob import glob  # 使用正则匹配文件
from io import StringIO
from requests import get
 
 
def getOnlineSource(url, *args, **kwargs):
    resp = get(url)
    resp.encoding = resp.apparent_encoding
    return StringIO(resp.text)  # 文件对象即为字符串流
 
# 可以用网址源码中文输入。需要传递一个钩子函数 
with fileinput.input("http://www.baidu.com", openhook=getOnlineSource) as f:  # 获取对应url中的资源，并输出
    for line in f:
        print(line)  # 输出每一行内容，即，等于是输出io流中的所有内偶然