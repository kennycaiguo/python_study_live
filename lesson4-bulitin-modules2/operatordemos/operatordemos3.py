import operator
from functools import reduce
 
sequence = 1, 2, 4
 
print("add", "=>", reduce(operator.add, sequence))
print("sub", "=>", reduce(operator.sub, sequence)) 
print("mul", "=>", reduce(operator.mul, sequence)) 
print("concat", "=>", operator.concat("spam", "egg")) 
print("getitem", "=>", operator.getitem(sequence, 2))
print("indexOf", "=>", operator.indexOf(sequence, 2)) 




