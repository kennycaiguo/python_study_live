"""
python data type
int,str,float,bool,list,tuple,set,dict
"""

a = 10
print(type(a)) # <class 'int'>
s = "Hello ,Python"
print(type(s)) # <class 'str'>
f = 10.1
print(type(f)) # <class 'float'>

b = False
print(type(b)) # <class 'bool'>

l = [1,2,3,4,5]
print(type(l)) # <class 'list'>
s1 = {1,2,4}
print(type(s1)) # <class 'set'>
t = (10,20,30)
print(type(t)) # <class 'tuple'>
d = {"name":"ken","age":36}
print(type(d)) # <class 'dict'>

print("=======================================")
class Person(object):
    def __init__(self):
        self.name = "Jack"
        self.age=20
        self.address = "3 pawsey road ,kgn5"

    def sayHi(self):
         print(f"Hello,my name is {self.name},i am {self.age} years old,i live in {self.address}")   

p = Person()
p.sayHi()
print(type(p)) # <class '__main__.Person'>

