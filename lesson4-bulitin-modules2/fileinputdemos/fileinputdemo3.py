#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import fileinput
from glob import glob  # 使用正则匹配文件
 
# 读取当前目录下，所有的txt文件，同时新建一个备份文件文件 
with fileinput.input(files=glob("*.txt"), inplace=True, backup=".bak") as f:  # 添加了backup参数后，就不会输出到命令行，而是输出到备份文件中
    # 在for循环里面的print内容不会输出到控制台上，而是直接输出到文件对应的行里面
    for line in f:
        print(f"{fileinput.filename()} -> {line.strip()} | 第{fileinput.filelineno()}行 | 共读取{fileinput.lineno()}行")  

        