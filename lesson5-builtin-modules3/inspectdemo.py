import inspect

# 1. 获取当前执行的函数或方法名、文件路径【并不是调用方】
def get_info():
    print(inspect.currentframe().f_code.co_filename) # 获取当前脚本文件的绝对路径
    return inspect.currentframe().f_code.co_name
# 2. 获取调用者信息
def get_caller_info():
    frame = inspect.currentframe().f_back
    print(f"调用者 {frame.f_code.co_filename} 调用行号:{frame.f_lineno}" )
# 调用上面的函数
def test_get_caller_info():
    get_caller_info()


# 3. 查看函数参数和返回值
def sample(name,age=20) ->str:
    pass

def get_func_param():
    print(inspect.signature(sample))

# 4. 获取源代码
class People:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def intro(self):
        print(f"My name is {self.name},i am {self.age} years, i am a {self.name}")   

# 4.2 获取函数源码
def get_class_source():
    source = inspect.getsource(People)
    print(source)

def get_func_source(func):
    print(inspect.getsource(func))  

# 5.获取类成员
def get_class_member(cls):
    methods = inspect.getmembers(cls,predicate=inspect.isfunction) 
    print(methods)   

# 6 获取类的继承情况
def get_inherate_info(clz):
    print(inspect.getmro(clz))
# 7.获取源代码的路径,函数或者类都可以
def get_sourcefile(methodorclz):
    print(inspect.getsourcefile(methodorclz))

def do_judge():
    print(inspect.ismodule(__file__))   # False 
    print(inspect.isclass(People)) # True
    print(inspect.ismethod(People.intro)) # False,在类里面定义的实例方法其实不是类方法，所有这里是False
    print(inspect.ismethod(People("Jack","male",18).intro)) # True
    print(inspect.isfunction(People.intro)) # True
    print(inspect.isfunction(People("Jack","male",18).intro)) # False，类方法不是函数，它是方法
    print(inspect.isfunction(get_sourcefile)) # True

if __name__ == '__main__':
    # get_info() # d:\pc_programming_live\python_study_live\lesson5-builtin-modules3\inspectdemo.py
    # test_get_caller_info() # 调用者 d:\pc_programming_live\python_study_live\lesson5-builtin-modules3\inspectdemo.py 调用行号:12
    # get_func_param() # (name, age=20) -> str
    # get_class_source()
    # get_func_source(get_class_source)
    # get_class_member(People)
    # get_inherate_info(People) # (<class '__main__.People'>, <class 'object'>)
    # get_sourcefile(People) # d:\pc_programming_live\python_study_live\lesson5-builtin-modules3\inspectdemo.py
    # get_sourcefile(People.intro) # d:\pc_programming_live\python_study_live\lesson5-builtin-modules3\inspectdemo.py
    # get_sourcefile(get_inherate_info) # d:\pc_programming_live\python_study_live\lesson5-builtin-modules3\inspectdemo.py
    do_judge()
