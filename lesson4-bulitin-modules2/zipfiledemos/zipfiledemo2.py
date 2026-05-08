import zipfile

# #创建压缩包
zf = zipfile.ZipFile("yasuoceshi.zip","w",zipfile.ZIP_DEFLATED)
# #写入文件
zf.write(r"log\log1.txt","log1.txt") # 不文件添加到压缩文件里面，这个文件必须存在
zf.write(r"log\log2.txt","log2.txt")
zf.close()

#解压单个文件
# zf = zipfile.ZipFile("yasuoceshi.zip","r")
# #第一个参数是之前压缩文件起的别名，第二个参数是要将文件解压到的路径
# zf.extract("log",r"C:\Users\dell\Desktop\log")
# zf.close()

#解压全部文件 只需要写路径，C:\Users\dell\Desktop\ceshi
# zf = zipfile.ZipFile("yasuoceshi.zip","r")
# zf.extractall(r"C:\Users\dell\Desktop\ceshi")
# zf.close()


# #向压缩包追加文件,追加文件模式用a
# zf = zipfile.ZipFile("yasuoceshi.zip","a",zipfile.ZIP_DEFLATED)
# # #写入文件
# # zf.write(r"C:\Users\dell\Desktop\log\info-20230315.log.0","log")
# zf.write(r"C:\Users\dell\Desktop\log\1.log","1.log")
# zf.close()

#使用with 来简化操作，压缩解压查看等操作 都可以使用，不用手动关闭
# with zipfile.ZipFile("yasuoceshi.zip","a",zipfile.ZIP_DEFLATED) as zf:
#     zf.write(r"C:\Users\dell\Desktop\log\port-admin.log","port-admin.log")


#查看压缩的文件,返回的是压缩后文件的列表
# with zipfile.ZipFile("yasuoceshi.zip","r") as zf:
#     lst = zf.namelist()
#     print(lst)


