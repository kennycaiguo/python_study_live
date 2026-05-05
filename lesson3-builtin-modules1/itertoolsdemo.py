"""
itertools built-in module to create iterators
methods
itertools.count(start [,step]) # create a iterator starting from start,step default is 1
itertools.cycle(iterable)  # create a iterator from that iterable data
itertools.repeat(ele [,n]) # repeat ele n times if n is set or unlimited
itertools.acumulate(p [,func]) # returns an iterator producing running totals or accumulated results from other binary functions
itertools.chain(p,q,...) # combine multiple iterables (like lists, tuples, or strings) into a single, seamless iterator.
itertools.chain.from_iterable(iterable) #  flatten a single iterable containing multiple nested iterables. It serves as an alternate constructor for itertools.chain()
itertools.compress(data,selector) # It returns an iterator that yields elements from data only when the corresponding element in selectors evaluates to True. It stops as soon as either the data or the selectors iterable is exhausted
itertools.dropwhile(predicate, iterable) # creates an iterator that skips (drops) elements from the beginning of an iterable as long as a specified condition (the predicate) is true
itertools.filterfalse(predicate, iterable) # creates an iterator which filters elements from an iterable, returning only those for which the predicate function returns False
itertools.groupby(iterable,key=None) #  group consecutive elements of an iterable that share the same key
itertools.islice(iterable,start,stop [,step]) # returns an iterator that yields selected elements lazily, making it highly memory-efficient for large datasets or infinite streams. 
itertools.starmap(function,iterable) # apply a function to arguments that are already grouped in tuples or other iterables
itertools.takewhile(predicate, iterable) # returns an iterator yielding elements from an iterable as long as a specified condition (the predicate) remains True
itertools.tee(iterable,n=2) #Python Standard Library function that creates independent iterators from a single source. It is primarily used when you need to consume the same data stream multiple times without reconstructing the original iterator. 
itertools.zip_longest(*iterables,fillvalue=None) # aggregate elements from multiple iterables in parallel. Unlike the built-in zip() function, which stops when the shortest iterable is exhausted, zip_longest() continues until the longest iterable is finished.

"""
import itertools as itt

# count()
# iter = itt.count(start=0,step=1)
# for i in iter:
#     if i>30 :
#         break
#     print(f"{i}")

# 2. cycle("abc")   # 无限重复a,b,c
# sum = 0
# for i in itt.cycle("hello"):
#     if sum > 10:
#         break
#     print(i,end= ",") # h,e,l,l,o,h,e,l,l,o,h,
#     sum += 1

# 3.repeat(obj,times)
""" 
obj : 循环的对象
times : 循环的次数
"""
# for x in itt.repeat("I love u",5):
#     print(x)

# 1. chain(p,q) : 将多个可迭代对象分别处理，可将多个序列处理为单个序列
 
"""
 p , q 都是可迭代对象
"""
# for i in itt.chain("Hello"," world of python"):
#     print(i,end=" ")

# # 2. chain.from_iterable(iterable)   # 这里相当于将一个迭代器的元素都拿来进行返回
# for i in itt.chain.from_iterable(["hello","python"]):
#     print(i,end=" ")  # h e l l o p y t h o n 
# print()

 # 1.compress(data,selector)
"""
data:一个可以用来迭代的数据。
selector:选择器,用来对data进行筛选。
生成一个筛选之后的迭代器,筛选规则为,当selector的第i个值为真,则保留data的第i个值,否则去除data的第i个值

"""
# for x in itt.compress('ABCDEF', [1, 0, 1, 0, 1, 1]): # A-1(KEEP) B-0(DISCARD) C-1(KEEP)  D-0(DISCARD) E-1(KEEP) F-1(KEEP)
#     print(x,end=" ") # A C E F 
# print()

# 2.dropwhile(predicate, iterable)
"""
predicate:一个判断函数,该函数返回值类型为bool。
iterable:可迭代对象。
注意:符合predicate条件的元素需要去除。
"""
#去除小于3的数
# for i in itt.dropwhile(lambda x:x<3,[1,2,3,4,5]):
#     print(i,end=" ")
# print()
# #输出 ： 3 4 5

# 3. takewhile(predicate, iterable)
"""
创建一个迭代器，只要 predicate 为真就从可迭代对象中返回元素。注意:可迭代对象里面不能有负数
"""
for i in itt.takewhile(lambda x: x > 5, [7, 6, 32, 3, 6, 5]):
    print(i,end=" ")
print()    # 7 6 32
# for i in itt.takewhile(lambda x: x > 1, [32, 6, 5,0]):
#     print(i,end=" ")
# print()   

