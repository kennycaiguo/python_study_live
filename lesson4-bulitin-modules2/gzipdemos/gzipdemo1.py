# 直接将内容写进一个gzip文件

import gzip
## write a gzip file method1
# content="你好我好大家好"
# file = gzip.open("hi.txt.gz",'wb')
# file.write(content.encode())
# file.close()

# write a gzip file method2
# zf = gzip.GzipFile("hi2.txt.gz",mode='wb')
# content="welcome to my class of python"
# zf.write(content.encode())
# zf.close()

# read a gzip file
zf = gzip.open("hi2.txt.gz","rb")
print(zf.read().decode()) # welcome to my class of python
zf.close()