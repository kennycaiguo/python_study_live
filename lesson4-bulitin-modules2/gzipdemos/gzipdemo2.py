# 直接将内容写进一个gzip文件

import gzip

# unzip,method1
# def do_unzip(zipfile,file):
#     with open(file,'wb') as f:
#         zf = gzip.open(zipfile,'rb')
#         f.write(zf.read()) 
#         zf.close()     

# do_unzip("hi2.txt.gz","hi2.txt")        

# unzip,method2
# def do_unzip2(zipfile,file):
#     with open(file,'wb') as f:
#         zf = gzip.GzipFile(zipfile,mode='rb')
#         f.write(zf.read()) 
#         zf.close()  

# do_unzip2("hi.txt.gz","hi.txt")

# unzip,method3
def do_unzip3(zipfile,file):
    with open(zipfile,'rb') as zf,open(file,'wb') as f:
       f.write(gzip.decompress(zf.read()))  

do_unzip3("hi.txt.gz","hi.txt")

