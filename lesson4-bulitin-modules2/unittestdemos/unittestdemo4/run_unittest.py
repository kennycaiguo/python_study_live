# run_test.py，与test_register.py、register.py同一目录下
""" pip install html-testRunner"""
import unittest
import test_register
from HtmlTestRunner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 通过模块加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))

# 创建测试运行程序启动器
runner = HTMLTestRunner()                 

# 使用启动器去执行测试套件里的用例
runner.run(suite)

