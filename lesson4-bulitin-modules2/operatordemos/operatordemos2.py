import operator

result = operator.add(3,4)
print(result) # 7

print(operator.eq(result,7)) # True

str1 = "Hello"
str2 = "Girls"
combined = operator.concat(str1," ")
combined = operator.concat(combined,str2)
print(combined) # Hello Girls
