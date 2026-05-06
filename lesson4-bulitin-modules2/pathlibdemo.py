"""
pathlib built-in module
"""

from pathlib import Path

# # 1.basic usage
# # 创建路径对象
# path = Path('folder') / 'subfolder' / 'file.txt' # 这种写法需要记住
# # 获取文件名
# basename = path.name
# print(basename)
# # 获取目录名
# dirname = path.parent
# print(dirname)
# # 判断是否存在
# exists = path.exists()
# print(exists)

# #2
path = Path(__file__)
# 这个属性能够获取到文件名
print(path.name) #pathlibdemo.py
# 这个属性能够获取到文件名的基本名称，去除扩展名
print(path.stem) #pathlibdemo
## 这个属性能够获取到文件名的扩展名
print(path.suffix) # .py
## 这个属性能够获取到文件名的扩展名列表
print(path.suffixes) # ['.py']
#文件所在的目录
print(path.parent) # D:\pc_programming_live\python_study_live\lesson4-bulitin-modules2
#文件所在的目录
print(path.parents[0]) # D:\pc_programming_live\python_study_live\lesson4-bulitin-modules2
#文件所在的目录的父目录
print(path.parents[1]) #D:\pc_programming_live\python_study_live
print(path.parts) # ('D:\\', 'pc_programming_live', 'python_study_live', 'lesson4-bulitin-modules2', 'pathlibdemo.py')
# 是否是绝对路径
print(path.is_absolute()) # True
#是否是某个路径的子路径
print(path.is_relative_to('/home')) # False
# 获取当前目录
print(path.cwd()) #D:\pc_programming_live\python_study_live\lesson4-bulitin-modules2
# 绝对路径
print(path.absolute()) # D:\pc_programming_live\python_study_live\lesson4-bulitin-modules2\pathlibdemo.py
#是否存在
print(path.exists()) # True,注意这个exists没有参数
# 是否是文件
print(path.is_file()) # True,这个方法没有参数
