# run_test.py，与test_register.py、register.py同一目录下
import unittest
import test_register

# 第一步，创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中
# 方式1，添加单条测试用例
# case = test_register.TestRegister("test_register_success")	# 创建一个用例对象，注意：通过用例类去创建测试用例对象的时候，需要传入用例的方法名（字符串类型）
# suite.addTest(case)	# 添加用例到测试套件中

# 方式2，添加多条测试用例
# case1 = test_register.TestRegister("test_register_success")
# case2 = test_register.TestRegister("test_username_isnull")
# suite.addTest([case1, case2])	# 添加用例到测试套件中

# 方式3，添加一个测试用例类
# loader = unittest.TestLoader()	# 创建一个加载对象
# suite.addTest(loader.loadTestsFromTestCase(test_register.TestRegister))

# 方式4，添加一个模块
loader = unittest.TestLoader()	# 创建一个加载对象
suite.addTest(loader.loadTestsFromModule(test_register))

# 方式5，指定测试用例的所在的目录路径，进行加载
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r"d:\learn\python"))

## 这个是笔记，想念展示有几种方法