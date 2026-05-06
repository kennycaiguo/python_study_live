"""
decimal builtin module
"""

from decimal import Decimal,getcontext,ROUND_HALF_UP

# # d = Decimal(0.1) # 使用数字来构建Demimal对象，非常麻烦，后面有长长的小数位
# # print(d) # 0.1000000000000000055511151231257827021181583404541015625
# d = Decimal('0.1') # 必须使用数字字符串来构建小数的Demimal对象，否则无法保证精度，整数就无所谓
# print(d) # 0.1

# print(d + Decimal('0.2')) # 0.3
# # 默认精度通常是 28 位，舍入模式是 ROUND_HALF_EVEN（银行家舍入法）
# print(getcontext()) # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
# 修改全局精度为 6 位
# getcontext().prec = 6
# # 计算 1 / 7
# print(Decimal('1') / Decimal('7'))  # 输出: Decimal('0.142857')
# # 修改舍入模式为我们熟悉的“四舍五入”
# getcontext().rounding = ROUND_HALF_UP
# # 计算 2.5 舍入到整数
# print(Decimal('2.5').quantize(Decimal('1')))  # 输出: 3

# 案例：计算利息 假设我们需要计算 $10000 存款，年利率 3.5%，存期 1 年，结果保留两位小数。

principal = Decimal('10000')
rate = Decimal('0.035')
interest = principal * rate

# 使用 quantize 方法进行小数点后两位的精确舍入
final_amount = interest.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(f"利息: {final_amount}")  # 利息: 350.00


