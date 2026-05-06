"""
python operator builtin module
"""

import operator

# # ex1.创建一个字典
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# value = operator.getitem(my_dict,"b")
# print(value) # 2
# ex2
two_dim_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 使用 operator.getitem 和 map 函数获取每个子列表的第一个元素
first_elements = list(map(operator.getitem, two_dim_list, [0]*len(two_dim_list)))
print(first_elements)  # 输出: [1, 4, 7]
