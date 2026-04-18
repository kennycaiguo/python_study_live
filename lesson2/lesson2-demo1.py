"""
built-in functions
abs(),all(),any(),
print(),range(),len()
enumerate()
eval(),exec()
max(),min()
filter(),map()
chr(),ord()
input()
divmod(),pow()
id()
sorted(),sum(),round(),reversed()
hasattr(),getattr(),delattr()
isinstance(object, classinfo)
type(),zip()
open()
"""

# abs
# a = -100
# print(abs(a)) # 100

# res = [True,False,True]
# print(all(res)) # False

# print(any(res)) # True

# names = ['Jack','Mary','Linda']
names = ('Jack','Mary','Linda')
# for idx,val in enumerate(names):
#     print(idx,val)
# print(len(names)) # 3

# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"

# print(dir(Person))

# eval()
# x = 10
# print(eval('x+10')) # 20

# cmd = 'print("Hello,Python")'
# exec(cmd)

# exec('a = 20')
# print("a=",a)

# data = [1,2,3,4,5]
# print(max(data)) # 5
# print(min(data)) # 1

# filter()
# data1 = [1,2,3,4,5]
# data2 = list(filter(lambda x:x%2==0,data1)) # the lambda function should return True or False else not work
# print(data2)
# data3 = list(filter(lambda x:x%2!=0,data1))
# print(data3) # [1, 3, 5]

# chr()  turn value into a letter
# print(chr(65)) #A
# # ord() get the ascii value of a letter
# print(ord('b')) #98

# name = input("Enter your name:")
# print(f"Hello,{name}")

# divmod will get the result and the remainder
# res,rem = divmod(10,3)
# print(res) # 3
# print(rem) # 1

# pow()
# a1 = pow(2,3) # 2**3 = 8
# print(a1)

# x = 100
# print(id(x)) # 140723498418056

l1 = [10,5,7,9,6,8]
# print(sorted(l1)) # [5, 6, 7, 8, 9, 10]
# print(sorted(l1,reverse=True)) # [10, 9, 8, 7, 6, 5]
# print(list(reversed(l1))) # [8, 6, 9, 7, 5, 10]

# sum() get the total
# l2 = [10,20,30,40]
# print(sum(l2)) #100 

# f = 10.345678
# print(round(f,2)) #10.35

class Animal(object):
    def __init__(self):
        self.name = "Bird"
        self.ability = "Fly"
        self.color = "Grey"
        self.feet = 2
        self.has_wings = True
    def fly():
        print("I am flying high in the sky")    

# print(hasattr(Animal,'name')) # False

bird = Animal()
# print(hasattr(bird,'color')) # True

# print(getattr(bird,'ability')) # Fly
# delattr(bird,'ability')
# print(getattr(bird,'ability')) # once you deleted a property,you can't get it again

# print(isinstance(bird,Animal)) # True
# print(isinstance(1,Animal)) # False

# print(type(bird)) # <class '__main__.Animal'>
names = ['Jack','Mary','Lucy']
scores = [90,80,50]
print(list(zip(names,scores))) # [('Jack', 90), ('Mary', 80), ('Lucy', 50)]

"""
file_object = open("filename.txt", mode="r", encoding="utf-8"), we will learn it next time
"""