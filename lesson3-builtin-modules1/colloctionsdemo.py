"""
collections builtin modules
1.Couter class
2.OrderedDict ->OrderedDict maintains the sequence exactly as elements were added
3.DefaultDict
4.ChainMap
5.namedtuple
6.deque
7.UserDict
8.UserString
9.UserList
"""
import collections

# # Counter : to do statistic ,tell the numbers of a element
# # three ways to construct a Counter object
# #1
# counter = collections.Counter(['B','B','A','B','C','A','B','B','A','C'])
# # 2
# counter2 = collections.Counter({"A":3,"B":5,"C":2})
# # 3
# counter3 = collections.Counter(A=3,B=5,C=2)
# print(counter,counter2,counter3)

# # counter.elements() -> iterator,convert to a list
# print(list(counter2.elements())) # ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C']
# # counter[element] => to tell the numer of element inside the counter
# print(counter['A']) # 3
# print(counter["B"]) # 5
# print(counter["C"]) # 2
# print("=======================")
# # couter.update(new list) -> to change the elements number in a counter obj,add new to the old
# counter.update(A=5,B=4,C=3,E=3) 
# print(counter["A"]) # 3+5 = 8
# print(counter["B"]) # 5+4 =9 
# print(counter["C"]) # 2+3 = 5
# print(counter["D"]) # 0 we don't have any 'D' int the counter obj
# print(counter["E"]) # 0+3 ->3
# # counter.most_common() to get the elements that has the biggiest number
# print(counter.most_common()) # a tuple ,[('B', 9), ('A', 8), ('C', 5), ('E', 3)] from big - > small
# # partially upate element
# counter['B'] -= 6
# # print(counter)  # Counter({'A': 8, 'C': 5, 'B': 3, 'E': 3})

# # couter.subtract(another counter)
# counter.subtract(['A', 'A','C', 'C']) # inplace,it actually change the counter
# # print(counter) # Counter({'A': 6, 'B': 3, 'C': 3, 'E': 3})

# ctr1 = collections.Counter([1, 2, 2, 3])
# ctr2 = collections.Counter([2, 3, 3, 4])

# print(ctr1 + ctr2)   # Addition # create a new counter obj Counter({2: 3, 3: 3, 1: 1, 4: 1})
# print(ctr1 - ctr2)   # Subtraction # create a new counter obj Counter({1: 1, 2: 1})
# print(ctr1 & ctr2)   # Intersection # create a new counter obj Counter({2: 1, 3: 1})
# print(ctr1 | ctr2)   # or # create a new counter obj Counter({2: 2, 3: 2, 1: 1, 4: 1})

# OrderedDict 
# od = collections.OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4

# print("before delete:\n")  
# for key, value in od.items(): 
#     print(key, value) 
# # 1.delete one key and add it back it will become the last one  
# print("after delete:\n")   
# od.pop('a') 
# od['a'] = 5
# for key, value in od.items(): 
#     print(key, value) 

# print(list(od.items())) # [('b', 2), ('c', 3), ('d', 4), ('a', 5)]
# od['c'] = 5
# # 2.Changing value does not affect order
# for key, value in od.items(): 
#     print(key, value) 
# print("------------------------------------------")

from collections import *
# # 3. if 2 orderdict are not the same order ,they are not the same
# od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
# print(od1 == od2)   # False

# # 4. Reversing an OrderedDict
# print(OrderedDict(reversed(od1.items()))) # OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# # Pop last or first item
# # od1.popitem(last=True)
# # print(list(od1.items())) #[('a', 1), ('b', 2)]

# od1.popitem()
# print(list(od1.items())) #[('a', 1), ('b', 2)]

# # 6 move the key to either end
# print("operation to od2 \n")
# od2.move_to_end('b',last=True) # end
# print(list(od2.items())) # [('c', 3), ('a', 1), ('b', 2)]

# od2.move_to_end('b',last=False) # front
# print(list(od2.items())) # [('b', 2), ('c', 3), ('a', 1)]

# # remove a key pop(key)
# od2.pop('c')
# print(list(od2.items())) # [('b', 2), ('a', 1)]

# DefaultDict,int,list,str ...
# mydict = defaultdict(list)
# mydict["fruit"].append("apple")
# mydict["veg"].append("cabbage")
# print(mydict) # defaultdict(<class 'list'>, {'fruit': ['apple'], 'veg': ['cabbage']})

# # mydict["fruit"].append("pineaple")
# # print(mydict["fruit"]) # ['apple', 'pineaple']

# dic = defaultdict(dict)
# dic['jack'] = {"name":"jack","age":30,"gender":"male"}
# dic['linda'] = {"name":"linda","age":30,"gender":"female"}
# print(dic) # defaultdict(<class 'dict'>, {'jack': {'mame': 'jack', 'age': 30, 'gender': 'male'}, 'linda': {'mame': 'linda', 'age': 30, 'gender': 'female'}})

# dic["jack"]['name'] = "John"
# print(dic['jack']) # {'name': 'John', 'age': 30, 'gender': 'male'}
# print(dic["linda"].get("gender")) # female
# for k,v in dic['jack'].items():
#     print(f"{k}:{v}")

# # Using str Default Factory
# sd = defaultdict(str)
# sd['greeting'] = 'Hello'
# print(sd) # defaultdict(<class 'str'>, {'greeting': 'Hello'})
## grouping,very useful
# words = ["apple", "ant", "banana", "bat", "carrot", "cat"]
# words = ["apple","banana", "ant", "carrot", "bat",  "cat"]
# df = defaultdict(list)
# print(df)
# for w in words:
#     df[w[0]].append(w) # group by the first letter

# print(df) # defaultdict(<class 'list'>, {'a': ['apple', 'ant'], 'b': ['banana', 'bat'], 'c': ['carrot', 'cat']})
    

 # handling the missing key
# df = defaultdict(lambda:"Not Present")
# print(df) # defaultdict(<function <lambda> at 0x0000018ABFC404A0>, {})
# df['a'] = "hello"
# df['b'] = "girls"
# print(df['x']) # Not Present
# for k in df:
#     print(f"{k}:{df[k]}")

# print(df.__missing__('f'))
# print(df.__missing__('d'))
# for k in df:
#     print(f"{k}:{df[k]}")

# # ChainMap -> chain the dicts together,you can use it like a normal dict
# dic1 = {"name":"jack","gender":"male","age":20}
# dic2={"job":"accountant","pay":3000}
# dic3 = {"chilren":3,"wife":"mary"}
# chm = ChainMap(dic1,dic2,dic3)  # no order
# print(chm)
# for k,v in chm.items():
#     print(f"{k}:{v}")

# chm['name'] = "Mike"
# print(chm)    # ChainMap({'name': 'Mike', 'gender': 'male', 'age': 20}, {'job': 'accountant', 'pay': 3000}, {'chilren': 3, 'wife': 'mary'})
# print(chm.values()) # ValuesView(ChainMap({'name': 'Mike', 'gender': 'male', 'age': 20}, {'job': 'accountant', 'pay': 3000}, {'chilren': 3, 'wife': 'mary'}))
# print(chm.get("gender")) # male
# print("add a child")
# # using new_child() to add new dictionary return a new chainmap object,don't change the old one
# chm1 = chm.new_child({"address":"11 oxford road ,kgn5","email":"Jack123@hotmail.com"})
# print(chm1) # ChainMap({'address': '11 oxford road ,kgn5', 'email': 'Jack123@hotmail.com'}, {'name': 'Mike', 'gender': 'male', 'age': 20}, {'job': 'accountant', 'pay': 3000}, {'chilren': 3, 'wife': 'mary'})
# print(chm1.popitem())

# # namedtuple
# Student = namedtuple("Student",["name","age","phone"])
# jack = Student("Jack",19,"506 83329996")
# print(jack.name)
# print(jack.age)
# print(jack.phone)

# print(getattr(jack,"phone")) # 506 83329996

# # _make()method to change value
# john = jack._make(["John",30,"2661-8844"])
# # john = jack._make(name="John") # error，this method don't have name=
# for i in john:
#     print(i)
# """
# output:
# John
# 30
# 2661-8844
# """

# # _asdict() convert a namedtuple into a OrderDict
# print(john._asdict()) # {'name': 'John', 'age': 30, 'phone': '2661-8844'}

# # convert a dict into a namedtuple
# stu = {'name': "Nikhil", 'age': 19, 'phone': '1391997'}
# print(Student(**stu)) # Student(name='Nikhil', age=19, phone='1391997')
# # _fields property
# print(john._fields) # ('name', 'age', 'phone')

# # _replace() replace a value ,return a new namedtuple,better than _make
# mary = john._replace(name="Mary") # Student(name='Mary', age=30, phone='2661-8844')
# print(mary)
# mary2 = mary._replace(age=40) # 
# print(mary2) # Student(name='Mary', age=40, phone='2661-8844')

# # __new__() create a new namedtuple

# stu2 = Student.__new__(Student,"Linda",20,"12345678") # static method,not instance method
# print(stu2) # Student(name='Linda', age=20, phone='12345678')

# deque (Doubly Ended Queue) 
d = deque([10,20,30])
d.append(40) # add to the end
print(d)# deque([10, 20, 30, 40])
d.appendleft(50) # add to the front
print(d) # deque([50, 10, 20, 30, 40])
d.append(10)
print(d.count(10)) #2  count the numer of a element
print(d)
print(len(d)) # 6
d.pop() # remove the last item
print(d) # deque([50, 10, 20, 30, 40])
d.popleft() # remove the first item
print(d) # deque([10, 20, 30, 40])
d.reverse() # no return value
print(d) # deque([40, 30, 20, 10])

# UserDict
class MyUserDict(UserDict):
  def __setitem__(self, key, value):
    print(f"Setting {key} = {value}")
    super().__setitem__(key, value)

  def __getitem__(self, key):
    print(f"Getting {key}")
    return super().__getitem__(key)
  
  def __delitem__(self, key):
    print(f"DEL {key!r}")
    super().__delitem__(key)

# usrd = MyUserDict(name="Jack",age=19,gender="male")  
# # the data is a property that store the dict's key-value pairs,it's a dictionary  
# print(usrd.data)  #{'name': 'Jack', 'age': 19, 'gender': 'male'}
# usrd['name'] = "Jane"
# print(usrd) # {'name': 'Jane', 'age': 19, 'gender': 'male'}
# print(usrd.get("gender")) # male
# del usrd["gender"]
# print(usrd) # {'name': 'Jane', 'age': 19}

# Case-Insensitive Keys
# class CaseInsensitiveDict(UserDict):
#   def _key(self, key):
#     return key.lower() if isinstance(key, str) else key

#   def __setitem__(self, key, value):
#     super().__setitem__(self._key(key), value)

#   def __getitem__(self, key):
#     return super().__getitem__(self._key(key))

# d = CaseInsensitiveDict()
# d["Name"] = "Mamta"
# print(d["name"]) # Mamta
# print(d["NAME"]) # Mamta

# UserString
# Creating a Mutable String 
class Mystring(UserString): 
      
    # Function to append to string
    def append(self, s): 
        self.data += s 
          
    # Function to remove from string 
    def remove(self, s): 
        self.data = self.data.replace(s, "") 
      
# Driver's code 
# s1 = Mystring("Geeks") 
# print("Original String:", s1.data) #Geeks
  
# # Appending to string 
# s1.append("s") 
# print("String After Appending:", s1.data)  # Geekss
  
# # Removing from string 
# s1.remove("e") 
# print("String after Removing:", s1.data) # Gkss

d = 12344

# Creating an UserDict
# userS = Mystring(d)
# print(userS.data)
# userS.append("6")
# print(userS)
# userS.remove("6")
# print(userS)

# UserList similar to list object
ul = UserList()
ul.append(10)
ul.append(20)
ul.append(30)
print(ul)
print(ul.data) # [10, 20, 30]
ul.remove(10)







