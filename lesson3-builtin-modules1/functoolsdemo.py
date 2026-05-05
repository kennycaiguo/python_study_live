"""
functools builtin module

"""
import functools as ft
import math

# # 1. partial
# def power(a,b):
#     return a ** b
# pwr2 = ft.partial(power,b=2)
# print(pwr2(4)) # 16  b**2 = 16
# print(pwr2(8)) # 64  8**2 = 64

# # 2. partialmethod
# class Demo:
#     def __init__(self):
#         self.color = 'black'

#     def _color(self, type):
#         self.color = type

#     set_red = ft.partialmethod(_color, type='red')
#     set_blue = ft.partialmethod(_color, type='blue')
#     set_green = ft.partialmethod(_color, type='green')

# obj = Demo()
# print(obj.color)
# obj.set_blue()
# print(obj.color)

## 3.cmp_to_key
# def custom_cmp(x, y):
#     # return (x > y) - (x < y) # 升序排列
#     return (x < y) - (x > y) # 降序排列

# # 将比较函数转换为键函数
# key_func = ft.cmp_to_key(custom_cmp)

# # 使用转换后的键函数进行排序
# sorted_list = sorted([3, 1, 4, 1, 5, 9], key=key_func)

# print(sorted_list)  # Output: [1, 1, 3, 4, 5, 9]

# # 4. reduce = >get the total of a list
# lst = [2, 4, 7, 9, 1, 3]
# sum_of_lst = ft.reduce(lambda a,b:a+b ,lst)
# print(sum_of_lst) # 26

# lst2 = ["abc", "xyz", "def"]
# max_of_lst2 = ft.reduce(lambda a,b: a if a>b else b,lst2)
# print(max_of_lst2) # xyz 

from functools import *
# # 5. total_ordering
# @total_ordering
# class Num():
#     def __init__(self,value):
#         self.value = value

#     def __eq__(self, other):
#             return self.value == other.value
    
#     def __lt__(self,other):
#          return self.value < other.value
    
#     # def __gt__(self, other): # will generate by @total_ordering
#     #      return self.value > other.value


# n1 = Num(2)
# n2 = Num(5)
# n3 = Num(7)
# n4 = Num(2)

# print(n1 >= n4)
# print(n1 < n2)
# print(n3 > n4)

# # 6.update_wrapper()
# def power(a, b):
#     '''a to the power b'''
#     return a ** b

# pow2 = partial(power, b=2)
# pow2.__doc__ = 'a to the power 2'
# pow2.__name__ = 'pow2'

# print('Before update:')
# print('Doc:', pow2.__doc__)
# print('Name:', pow2.__name__)

# update_wrapper(pow2, power)

# print('After update:')
# print('Doc:', pow2.__doc__)
# print('Name:', pow2.__name__)

# # 7.wraps
# def my_decorator(func):
#     @wraps(func)  # This copies metadata from 'func' to 'wrapper'
#     def wrapper(*args, **kwargs):
#         """This is the wrapper's own internal docstring."""
#         print("Before calling the function")
#         result = func(*args, **kwargs)
#         print("After calling the function")
#         return result
#     return wrapper

# @my_decorator
# def say_hello():
#     """Greet the user."""
#     print("Hello!")

# # With @wraps, these reflect 'say_hello' instead of 'wrapper'
# print(say_hello.__name__)  # Output: say_hello
# print(say_hello.__doc__)   # Output: Greet the user.
# say_hello()
# """
# Before calling the function
# Hello!
# After calling the function
#"""

# # # 8.lrc_cache
# @lru_cache
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# # 5 * factorial(4)*4*factorial(3)*3*... = 5*4*3*2*1

# print(factorial(5)) # 120
# print(factorial.cache_info()) # CacheInfo(hits=0, misses=5, maxsize=128, currsize=5)

# # 9. singledispatch -> turns a function into a generic function

# @singledispatch
# def fun(s):
#     print(s)

# @fun.register(int)
# def _(s):
#     print(abs(s))

# @fun.register(list)
# def _(arr):
#     print(max(arr)) 
    

# fun('GeeksforGeeks')  
# fun(-10)
# fun(1.5)
# fun([10,5,21,17])

# # 10.singledispathmethod -> almost same thing like #9,but it use to decorate a class method
# # functools.singledispatchmethod is a decorator introduced in Python 3.8 that allows you to perform method overloading based on the type of a single argument
# class DataProcessor:
#     @singledispatchmethod
#     def process(self, data):
#         # Default implementation for unknown types
#         print("Normal process:")
#         print(data)

#     @process.register
#     def _(self, data: int):
#         print(f"Processing integer: {data * 10}")

#     @process.register
#     def _(self, data: str):
#         print(f"Processing string: {data.upper()}")

#     @process.register(list) # You can also specify the type explicitly
#     def _(self, data):
#         print(f"Processing list of length: {len(data)}")

# # Usage
# proc = DataProcessor()
# proc.process(5)          # Output: Processing integer: 50
# proc.process("hello")    # Output: Processing string: HELLO
# proc.process([1, 2, 3])  # Output: Processing list of length: 3
# proc.process(1.5)

# # 11.cache ,like lrc_cache
# @cache
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(4)) #24

# 12.cached_property # functools.cached_property is a Python decorator (added in 3.8) that transforms a class method into a property, computing its value only once and caching it for the lifetime of that instance
from functools import cached_property

class Dataset:
    def __init__(self, path):
        self.path = path

    @cached_property
    def data(self): # uesed as a property
        # Expensive loading/parsing
        # return self.path
        print(f"The data path:{self.path}")

ds = Dataset("c:/datas/")
ds.data  # The data path:c:/datas/