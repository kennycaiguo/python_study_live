import fileinput
from glob import glob  # 使用正则匹配文件
 
 
with fileinput.input(files=glob("*.txt"), openhook=fileinput.hook_encoded("utf-8")) as f:  # 读取当前目录下，所有的txt文件
    for line in f:
        print(f"{fileinput.filename()} -> {line.strip()} | 第{fileinput.filelineno()}行 | 共读取{fileinput.lineno()}行")
