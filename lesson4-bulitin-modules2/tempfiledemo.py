""" 
tempfile bulitin module 
Python 的 tempfile 模块用于创建临时文件和目录,支持在所有平台(UNIX、Windows)自动安全地生成临时数据，并在使用后自动删除，
有效避免了磁盘空间垃圾累积和文件名冲突。核心工具包括 TemporaryFile(内存临时文件)、NamedTemporaryFile(具名临时文件)
和 TemporaryDirectory(临时目录)。
tempfile 模块默认操作%TEMP%目录

tempfile.TemporaryDirectory() ->TemporaryDirectory对象
可以使用他的name方法来获取临时目录,每一次生成的临时文件夹都不一样
"""
# 简单使用
# import tempfile  
# import os  
# # Create a temporary directory
# with tempfile.TemporaryDirectory() as temp_dir:  
#     print(f"Temporary directory created at: {temp_dir}")  
#     # Create a temporary file inside the directory
#     file_path = os.path.join(temp_dir, "sample.txt")  
#     with open(file_path, "w") as f:  
#         f.write("Hello, Temporary World!")  
#     # Read back the file
#     with open(file_path, "r") as f:  
#         print(f.read())  
# # At this point, the directory and its contents are deleted automatically
# print("Temporary directory cleaned up automatically.")

# #2. 自定义临时目录的命名和位置
# # tempfile 支持给临时目录添加前缀和后缀，方便调试时识别：
# import tempfile

# with tempfile.TemporaryDirectory(prefix="app_",suffix="_temp") as tmp_dir:
#     print(tmp_dir) # C:\Users\kenny\AppData\Local\Temp\app_9s9jqztr_temp

# 3.可以指定父目录：但是前提是这个目录已经存在否则报错
# import tempfile

# with tempfile.TemporaryDirectory(dir="mytemp",prefix="app_",suffix="_temp") as tmp_dir:
#     print(tmp_dir)

# 4.手动删除临时文件
import tempfile  
import shutil  
import os  
# Create a temporary directory manually
temp_dir = tempfile.mkdtemp()  
print(f"Created temporary directory: {temp_dir}")  
# Work inside it
file_path = os.path.join(temp_dir, "example2.txt")  
with open(file_path, "w") as f:  
    f.write("Manual cleanup required!")  
print("Files inside temp dir:", os.listdir(temp_dir))  
# Clean up manually when done
shutil.rmtree(temp_dir)  
print("Temporary directory removed.")