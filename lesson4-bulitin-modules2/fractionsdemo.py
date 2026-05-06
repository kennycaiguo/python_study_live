"""
fractions builtin module
use the class : Fraction
"""
from fractions import Fraction
from decimal import Decimal

print(Fraction(16,-10)) # -8/5
print(Fraction(5)) # 5
print(Fraction()) # 0
print(Fraction('3/7')) # 3/7
print(Fraction('1.414213 \t\n')) #1414213/1000000
print(Fraction('-.125')) # -1/8
print(Fraction('7e-6')) # 7/1000000
print(Fraction(2.25)) # 9/4
print(Fraction(1.1)) # 2476979795053773/2251799813685248
print(Fraction(Decimal('1.1'))) # 11/10

#  Fraction对象可以直接进行加减乘除运行
