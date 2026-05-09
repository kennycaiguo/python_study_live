
 
'''
     python中的zlib模块提供了压缩和解压缩的方法
     
     实现功能：
     
         读取一个文件的内容，然后把该文件的内容以字符串的形式返回
         然后对返回回来的字符串进行压缩处理，然后写入到另一个文件中
         同时，也提供一个方法进行对压缩内容进行解压缩
 
'''

import os
import zlib
 
#global var
#打印日志信息
SHOW_LOG =  True
#原信息存放地址
ORI_PATH = ''
#压缩后文件存放地址
COM_PATH = ''
 
def get_content(path):
    '''读取一个文件的内容，然后把该文件的内容以字符串的形式返回'''
    if os.path.exists(path):
        c = ''
        if SHOW_LOG:
             print('打开文件:[{}]'.format(path))
        with open(path, 'r+') as pf:
             for line in pf:
                 if SHOW_LOG:
                     print('读取内容：[{}]'.format(line))
                 c += line
             return c
    else:
         print('the path [{}] is not exist!'.format(path))
 
def compress_test(data):
     '''对data进行压缩，然后返回压缩后的内容'''
     if SHOW_LOG:
         print('压缩内容：[{}]'.format(data))
     return zlib.compress(bytes(data, 'utf-8'))
    
 
def decompress_test(cdata):
     '''对cdata进行解压缩，然后返回解压缩后的内容'''
     if SHOW_LOG:
         print('解压缩内容：[{}]'.format(cdata))
     return zlib.decompress(cdata)
 
def write_file(path, data):
     '''把data写入到指定的文件'''
     if os.path.exists(path):
         if SHOW_LOG:
             print('打开文件:[{}]'.format(path))
         with open(path, 'w+') as pf:
             pf.write(str(data))
             if SHOW_LOG:
                 print('写入内容:[{}]'.format(data))
             pf.close()
     else:
         print('the path [{}] is not exist!'.format(path))
 
def init():
     global SHOW_LOG
     SHOW_LOG = True
     global ORI_PATH
     ORI_PATH = './test.txt'
     global COM_PATH
     COM_PATH = './com.txt'
     
 
def main():
     init()
     #获取原信息
     data = get_content(ORI_PATH)
     #对内容进行压缩
     cdata = compress_test(data)
     #写入压缩文件内容
     write_file(COM_PATH, cdata)
     #获取压缩文件内容
     c_data = get_content(COM_PATH)
     print('压缩内容：[{}]'.format(c_data))
     #解压信息
     dedata = decompress_test(cdata)
     print(dedata)
 
if __name__ == '__main__':
     main()