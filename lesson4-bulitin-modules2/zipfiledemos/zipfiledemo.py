import zipfile

def read_zip_file(zip_path):
    """
    读取zip文件内容并打印文件名和内容
    :param zip_path: zip文件路径
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 打印zip文件中的所有文件名
            print("Zip文件包含以下文件:")
            for file_name in zip_ref.namelist():
                print(f"- {file_name}")
            
            # 读取第一个文件的内容
            if zip_ref.namelist():
                first_file = zip_ref.namelist()[0]
                print(f"\n读取文件内容: {first_file}")
                with zip_ref.open(first_file) as file:
                    content = file.read()
                    try:
                        # 尝试UTF-8解码
                        print(content.decode('utf-8'))
                    except UnicodeDecodeError:
                        # 如果UTF-8解码失败，显示为字节
                        print("文件内容(二进制):")
                        print(content)
    
    except FileNotFoundError:
        print(f"错误: 文件 {zip_path} 不存在")
    except zipfile.BadZipFile:
        print(f"错误: {zip_path} 不是有效的ZIP文件")

def read_zip_files(zip_path):
    """
    读取zip文件内容并打印文件名和内容
    :param zip_path: zip文件路径
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 打印zip文件中的所有文件名
            print("Zip文件包含以下文件:")
            for file_name in zip_ref.namelist():
                print(f"\n读取文件内容: {file_name}")
                with zip_ref.open(file_name) as file:
                    content = file.read()
                    try:
                        # 尝试UTF-8解码
                        print(content.decode('utf-8'))
                    except UnicodeDecodeError:
                        # 如果UTF-8解码失败，显示为字节
                        print("文件内容(二进制):")
                        print(content)
    
    except FileNotFoundError:
        print(f"错误: 文件 {zip_path} 不存在")
    except zipfile.BadZipFile:
        print(f"错误: {zip_path} 不是有效的ZIP文件")


if __name__ == "__main__":
    zip_file_path = input("请输入ZIP文件路径: ")
    # zip_file_path ="./zips/zips1.zip"
    read_zip_files(zip_file_path)