"""
os functions
os.getcwd() # get the current directory, usually means the workspace folder
os.chdir(path),path can be relative or absolute
os.listdir(path), show everything inside a directory,including folder and file
os.mkdir(dir),create a directory
os.makedirs("path1/path2/")
os.removedirs("path1/path2/")  remove path2 and then remove path1 until finished
os.rmdir("test2/test3")  delete one layer,here means test3 will be deleted... test2 no
os.remove(filename),delete a file
os.rename(oldfilename , newfilename)
os.stat(path)  # get infomation of a dir or file
os.system('command') # call a cmd command or start a app
os.environ # get the environment variable, this is a property ,not function
"""
import os

# print(os.getcwd())
# os.chdir("./lesson3-builtin-modules")
# os.chdir("D:\pc_programming_live\python\lesson3-builtin-modules")
# print(os.getcwd())
# ret = os.listdir(os.getcwd())
# print(ret)

# for dir in os.listdir(os.getcwd()):
#     print(os.listdir(dir))

os.chdir("./lesson3-builtin-modules")
# os.mkdir("test2")
# print(os.listdir(os.getcwd()))
# os.makedirs("demo/demo1/demo2")
# print(os.listdir(os.getcwd()))
# os.removedirs("demo/demo1/demo2")
# print(os.listdir(os.getcwd()))
# os.rmdir("test2/test3") # current dir is now lesson3-builtin-modules,so there is no test3,only have test2/test3

# os.remove("test2/text1")

# os.rename("test2/demo.txt","test2/sample.txt")
# print(os.stat("test2"))
# print(os.sep) # windows: \ linux : / this is a property not function

# print(os.name) # nt  this is a property not function

# os.system("notepad")
# os.system("mspaint")
# os.system("start .")

# print(type(os.environ))
# print(os.environ.get("path")) # get the system path variable

