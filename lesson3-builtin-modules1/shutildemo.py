"""
shutil module
比较特殊的2个方法: shutil.copymode(src,dst)只拷贝权限不拷贝内容,shutil.copystat(src,dst)只拷贝元数据,src和dst都必须存在
"""
import shutil
import os

# shutil.copy(src,dst)
basedir = os.path.dirname(os.path.abspath(__file__))
# shutil.copy(os.path.join(basedir,"data.txt"),"datacopy.txt")

# shutil.copy2(src,dst) # 有点多余，使用copy就好
# shutil.copy2("datacopy.txt","datacopy2.txt")

# shutil.copyfileobj(srchandle,dsthandle) # copy file handle，good
# with open("data.json",'r') as src,open("datacpy.json",'w') as dst:
#     shutil.copyfileobj(src,dst)

# shutil.copyfile(src,target)
# shutil.copyfile("datacopy.txt","datac.txt") # 有点多余，使用copy就好

# shutil.copytree(src,target) # verygood 拷贝这个文件夹，把里面的文件和子文件夹全部拷贝
# src_dir = os.path.join(basedir,"test2")
# shutil.copytree(src_dir,"test2cpy")

# # shutil.copymode(src,dst) #只拷贝权限，两个文件都必须存在，否则报错
# shutil.copymode(os.path.join(basedir,"data.txt"),"data2.txt")

# shutil.copystat() # 拷贝元数据，两个文件都必须存在
# shutil.copystat(os.path.join(basedir,"data.txt"),"data2.txt")

# shutil.rmtree()   # delete no matter empty or not
# shutil.rmtree("test2cpy")

# shutil.move(srcpath,dstpath) # move from srcpath to dstpath
# shutil.move(os.path.join(basedir,"test.txt"),"test.txt")

# shutil.which(cmd) # get application's path
# print(shutil.which("notepad.exe")) # C:\WINDOWS\system32\notepad.exe

# shutil.disk_usage(drive) # show the usage of a disk drive
# print(shutil.disk_usage("c:")) # usage(total=289086107648, used=105277739008, free=183808368640)

# shutil.make_archive(dstpath,file extension,srcpath) # 制作压缩文件
# shutil.make_archive("test2","zip",os.path.join(basedir,"test2"))
# shutil.unpack_archive(srcpath,dstpath) # 解压缩
# shutil.unpack_archive("test2.zip","test2_upacked")

# shutil.get_archive_formats() # get the supported archive formats,rar not supported
# print(shutil.get_archive_formats()) #[('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]

# shutil.get_unpack_formats()  # get the supported unpack formats
print(shutil.get_unpack_formats()) # [('bztar', ['.tar.bz2', '.tbz2'], "bzip2'ed tar-file"), ('gztar', ['.tar.gz', '.tgz'], "gzip'ed tar-file"), ('tar', ['.tar'], 'uncompressed tar file'), ('xztar', ['.tar.xz', '.txz'], "xz'ed tar-file"), ('zip', ['.zip'], 'ZIP file')]
