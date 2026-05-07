import array
# 一个array只能包含一种数据类型，输入不同类型会报错
arr = array.array("i",[1,2,3,5,7])

# 1.append
arr.append(6)
print(arr) # array('i', [1, 2, 3, 5, 7, 6])
# arr.append('8') #'str' object cannot be interpreted as an integer,报错
# 2.extend
arr.extend([0,4,9])
print(arr) # array('i', [1, 2, 3, 5, 7, 6, 0, 4, 9])
# 3.insert
arr.insert(5,10)
print(arr) # array('i', [1, 2, 3, 5, 7, 10, 6, 0, 4, 9])

# 4.from list
arr.fromlist([11,22,33])
print(arr) # array('i', [1, 2, 3, 5, 7, 10, 6, 0, 4, 9, 11, 22, 33])

# 5.index()
print(arr.index(5)) # 3

# 6.count(x) 获取值为 x 的元素的个数
arr.extend([1,2,2,2,4,4,3,3,3,3,])
print(arr) # array('i', [1, 2, 3, 5, 7, 10, 6, 0, 4, 9, 11, 22, 33, 1, 2, 2, 2, 4, 4, 3, 3, 3, 3])
print(arr.count(3)) # 5

# array.pop([i])将指定索引值的元素从数组中移除并返回，默认移除并返回数组中的最后一个元素。
arr.pop(2)
print(arr) # array('i', [1, 2, 5, 7, 10, 6, 0, 4, 9, 11, 22, 33, 1, 2, 2, 2, 4, 4, 3, 3, 3, 3])
arr.pop()
print(arr) # array('i', [1, 2, 5, 7, 10, 6, 0, 4, 9, 11, 22, 33, 1, 2, 2, 2, 4, 4, 3, 3, 3])

print(arr.itemsize) # 元素的数据类型所占的内存大小
arr.reverse()
print(arr) # array('i', [3, 3, 3, 4, 4, 2, 2, 2, 1, 33, 22, 11, 9, 4, 0, 6, 10, 7, 5, 2, 1])

lsr = arr.tolist()
print(lsr) # [3, 3, 3, 4, 4, 2, 2, 2, 1, 33, 22, 11, 9, 4, 0, 6, 10, 7, 5, 2, 1]
    


