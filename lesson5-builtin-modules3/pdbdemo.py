"""pip install pysnooper"""
"""pdb常见指令
| break 或 b    | 设置断点                   |
| ------------- | -------------------------- |
| continue 或 c | 继续执行程序               |
| list 或 l     | 查看当前行的代码段         |
| step 或 s     | 进入函数                   |
| return 或 r   | 执行代码直到从当前函数返回 |
| exit 或 q     | 中止并退出                 |
| next 或 n     | 执行下一行                 |
| pp            | 打印变量的值               |
| help          | 帮助                       |

"""
def demo1():
    import pdb

    def divide(a, b):
        pdb.set_trace()  # 设置断点
        return a / b

    result = divide(10, 0)
    print("Result:", result)


def demo2():
    import pysnooper

    @pysnooper.snoop()
    def divide(a, b):
        return a / b

    result = divide(10, 0)
    print("Result:", result)



if __name__ == '__main__':
    # demo1()
    # demo2()
    