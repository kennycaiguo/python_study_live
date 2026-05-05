"""
copy builtin module,do the memory copy ,not file copy,file copy use shutil module

"""

import copy

#Shallow copy
a = [[1, 2, 3], [4, 5, 6]]
b = copy.copy(a) # a shared link
# print(a,b)

b[0][1] = 10
print(a) # [[1, 10, 3], [4, 5, 6]]
print(b) # [[1, 10, 3], [4, 5, 6]]

# deepcopy -> independent copy : one changed,the other not changed
a = [[1, 2, 3], [4, 5, 6]]
c = copy.deepcopy(a)

c[0][0] =20
print(c) # [[20, 2, 3], [4, 5, 6]]
print(a) # [[1, 2, 3], [4, 5, 6]]