import tarfile

# 解压缩
# with tarfile.open("all.tar.gz",'r') as tf:
#     tf.extractall(path='extracted_files')

# 列出压缩包的内容
import tarfile

with tarfile.open('all.tar.gz', 'r') as tar:
    print("文件列表:", tar.getnames())
    for member in tar.getmembers():
        print(f"文件名: {member.name}, 大小: {member.size}字节")