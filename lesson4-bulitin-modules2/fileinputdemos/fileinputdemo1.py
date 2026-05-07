import fileinput

def readFile(file):
    for line in fileinput.input(file):
        print(fileinput.filename(),">>",fileinput.lineno(),">>",line)

if __name__ == '__main__':
    #调用读取两个文件内容
    readFile(("test.txt","test1.txt"))        # 不支持中文