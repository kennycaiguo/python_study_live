"""
math built-in module
Constants in Math Module:
Euler's Number : e
pi
tau : pi * 2 
Infinity
Not a Number (NaN)

methods:
math.cos(x) #求余弦值
math.sin(x)  #求正弦值 
math.tan(x) # 求正切值
math.ceil(x) #向上取整
math.floor(x) # 向下取整
math.fabs(x)  # absolute value in floating point type
math.factorial(n) # 阶乘
math.fmod(a,b) # 
math.fsum([a,b.c]) # get total
math.isnan(n) 
math.pow(base,exp)
math.sqrt(a)
math.log(a)
math.gcd(a,b) # 最大公约数  find the greatest common divisor of two numbers passed as the arguments.
math.exp(y)  alculate the power of e 也就是计算e的y次方
math.degrees(a)  # convert argument value from radians to degrees蝴蝶转化为角度
math.radians(b)  # convert argument value from degrees to radians.角度转化为弧度
math.gamma(gamma_var)  return the gamma value of the argument.
math.copysign(x, y)  Returns the number with the value of ‘x’ but with the sign of ‘y’
math.isinf(num)
math.isnan(a)
math.isfinite(x)
"""
import math

# # Constants:
# # The math.e constant returns the Euler’s number: 2.71828182846.
# print(math.e) # 2.718281828459045
# # math.pi.
# print (math.pi) # 3.141592653589793
# # math.tau = 2*math.pi
# print(math.tau) # 6.283185307179586
# # Infinity basically means something which is never-ending or boundless from both directions
# print (math.inf)  # inf
# print (-math.inf) # -inf
# print (math.inf > 10e108)    # True
# print (-math.inf < -10e108)  # True 
# # NaN Values
# print (math.nan) # nan

# methods
# print("次方运算:",math.pow(5, 2))       # 结果 ： 25.0
# print("开方运算:",math.sqrt(64))        # 结果 ：8.0
# print("对数运算:",math.log(100, 10))    # 结果 ：2.0
# print("返回已2为底x的对数:",math.log2(3))       # 结果 ：1.584962500721156
# print("返回以10为底x的对数:",math.log10(1000))  # 结果 ：3.0
# print("求和:",math.fsum([3,4,5]))       # 结果 ： 12
# print("取余运算:",math.fmod(8, 3))       # 结果 ： 2.0
# print("向上取整:",math.ceil(8.3))       # 结果 ： 9
# print("向下取整:",math.floor(8.3))       # 结果 ： 8

# # gcd(a,b) 
# a = 15
# b = 5
# print ("The gcd of 5 and 15 is : ", end="") 
# print (math.gcd(b, a)) # The gcd of 5 and 15 is : 5
# # fabs(a) return the absolute value in floating point of 
# print(math.fabs(3)) # 3.0
# print(math.fabs(-1.5)) # 1.5
# # math.exp(n) 也就是计算e的y次方
# test_int = 4
# test_neg_int = -3
# test_float = 0.00
# print (math.exp(test_int))  # 54.598150033144236
# print (math.exp(test_neg_int))  # 0.049787068367863944
# print (math.exp(test_float)) # 1.0

"""
log() function returns the logarithmic value of a with base b. If the base is not mentioned, the computed value is of the natural log.
log2(a) function computes value of log a with base 2. This value is more accurate than the value of the function discussed above.
log10(a) function computes value of log a with base 10. This value is more accurate than the value of the function discussed above.
"""
# print ("The value of log 2 with base 3 is : ", end="")  
# print (math.log(2,3))  # The value of log 2 with base 3 is : 0.6309297535714574
# print ("The value of log2 of 16 is : ", end="") 
# print (math.log2(16)) # The value of log2 of 16 is : 4.0     2**4 == 16
# print ("The value of log10 of 10000 is : ", end="") 
# print (math.log10(10000)) # The value of log10 of 10000 is : 4.0    10**4 == 10000

a = math.pi/6
b = 30
# print ("The converted value from radians to degrees is : ", end="") 
# print (math.degrees(a))  # The converted value from radians to degrees is : 29.999999999999996
# print ("The converted value from degrees to radians is : ", end="") 
# print (math.radians(b))  # The converted value from degrees to radians is : 0.5235987755982988

# gamma_var = 6
# print ("The gamma value of the given argument is : "+ str(math.gamma(gamma_var))) # The gamma value of the given argument is : 120.0

# print (math.isinf(math.pi))         # False
# print (math.isinf(math.e))         # False
# print (math.isinf(float('inf')))   # True

# print (math.isnan(math.pi))  # False
# print (math.isnan(math.e))   # False
# print (math.isnan(float('nan'))) # True

# print(math.copysign(5,-2)) # -5.0