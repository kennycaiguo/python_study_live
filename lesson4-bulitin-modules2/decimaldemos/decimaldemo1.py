"""
decimal builtin module
"""

from decimal import Decimal,getcontext

# d = Decimal(0.1) # 使用数字来构建Demimal对象，非常麻烦，后面有长长的小数位
# print(d) # 0.1000000000000000055511151231257827021181583404541015625
d = Decimal('0.1') # 必须使用数字字符串来构建Demimal对象，否则无法保证精度
print(d) # 0.1

print(d + Decimal('0.2')) # 0.3

