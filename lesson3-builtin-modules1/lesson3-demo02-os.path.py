"""
os.path.abspath(path)
path = '/home/user/documents/report.txt'
head, tail = os.path.split(path) # to get a filename and directory path from a file absolute path
print(head)  # 输出: /home/user/documents
print(tail)  # 输出: report.txt
abspath = os.path.abspath("sample.txt")
print(os.path.splitext(abspath)) # ('D:\\pc_programming_live\\python\\sample', '.txt') # to get a filename extension
os.path.dirname(abspath) # get the parent directory of a path
os.path.basename(abspath) # get a filename from a file absolute path
os.path.exists() # is a path (filename not includede) exists or not
os.path.isfile(path) # to find out if a path is a file,(is a path do not exists,return False)
os.path.isdir(path)  # to find out if a path is a directory
os.path.isabs(path)
os.path.join(basepath,subpath) # basepath/subpath
os.path.getsize(absolute path of a file) # file->file size directory->0
os.path.getmtime(abspath) # to get the last modify time
os.path.getctime(abspath) # to get the file creation time

"""
import os

# print(os.path.abspath("."))  # D:\pc_programming_live\python
abspath = os.path.abspath("lesson3-builtin-modules\\test2\\sample.txt")
# dir,filename = os.path.split(abspath) 
# print(dir) # D:\pc_programming_live\python\lesson3-builtin-modules\test2
# print(filename) # sample.txt

# print(os.path.splitext(abspath)) # ('D:\\pc_programming_live\\python\\lesson3-builtin-modules\\test2\\sample', '.txt')
# print(os.path.dirname(abspath)) # D:\pc_programming_live\python\lesson3-builtin-modules\test2

# print(os.path.basename(abspath)) # sample.txt
# print(os.path.exists(os.path.dirname(abspath))) # True  to find out is a directory exists,if this is a filename path,return False

# print(os.path.isfile(abspath)) # True
# print(os.path.isfile(os.path.basename(abspath))) # False
# print(os.path.isfile('D:\\pc_programming_live\\python\\lesson3-builtin-modules\\test2\\sample.txt')) # True

# print(os.path.isdir(abspath)) # False
# print(os.path.isdir(os.path.dirname(abspath))) # True

# print(os.path.isabs(abspath)) # True

# basedir = os.getcwd()
# ret_path = os.path.join(basedir,"lesson3-builtin-modules\\test2\\sample.txt")
# print(ret_path) #D:\pc_programming_live\python\lesson3-builtin-modules\test2\sample.txt

# print(os.path.getsize(abspath)) # 19
# print(os.path.getsize(os.getcwd())) # 0 
# print(os.path.getsize("demo.txt")) # FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'demo.txt'

# print(os.path.getmtime(abspath)) # timestamp : 1776354758.0866616
# print(os.path.getctime(abspath)) # timestamp : 1776354750.5059788
# print(os.path.getatime(abspath)) # timestamp : 1776354995.3779395

print(os.path.realpath(abspath))