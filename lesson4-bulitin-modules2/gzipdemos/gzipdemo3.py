# 利用gzip批量解压缩文件
import os
import gzip
 
 
def unzip_gz_file(path, new_path):
    # 需要创建一个保存解压后的文件的文件夹，否则报错
    base = os.path.abspath(path)
    dst_path = os.path.join(base,new_path)
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    count = 0
    try:
        for f_path in os.listdir(path):
            if '.gz' in f_path:
                try:
                    with gzip.GzipFile(fileobj=open(path + "/" + f_path, 'rb'), mode='rb') as g:
                        with open(dst_path + "/" + f_path.replace(".gz", ""), "wb") as f:
                            f.write(g.read())
                        print(count, f"文件{f_path}  解压完成...")
                except Exception as e:
                    print(f_path, e)
                count += 1
    except Exception as e:
        print(e)
    else:
        print("文件全部解压完成！")
 
 
path = './'
new_path = './unzip_file'
unzip_gz_file(path, new_path)


