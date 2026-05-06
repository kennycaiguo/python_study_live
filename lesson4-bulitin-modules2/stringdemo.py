"""
python string builtin module
"""

import string as s
# props
## letters
print(s.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(s.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(s.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
## digits
print(s.digits) # 0123456789
print(s.hexdigits) # 0123456789abcdefABCDEF
print(s.octdigits) # 01234567
## special signs
print(s.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(s.printable) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
print(s.whitespace) # no output

# methods就是使用str类的方法string库只有一个capword()方法
# print(s)

# string库里面的Template类
from string import Template
 
s = Template('$who的年龄为:${age}')
print(s.safe_substitute({"who": "李华", "age": 13}))  # safe_*这个函数如果没有给字符串里面的所有变量赋值不会报错
print(s.safe_substitute(**{"who": "李华"}))
print(s.substitute(**{"who": "李华", "age": 13}))  # 但是这个函数，必须要给字符串里面所有定义的变量都赋值，否则会报错
# print(s.substitute({"who": "李华"})) #报错



