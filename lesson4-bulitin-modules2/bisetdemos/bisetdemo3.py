import bisect

#查找指定区间中包含的元素个数
# A = [1,2,2.5,3,3.5,4,5]
# lindex = bisect.bisect_left(A,2.5) # 2
# rindex = bisect.bisect_right(A,3.5) # 5
# print(lindex, rindex, rindex-lindex) # 3

# # 2.分数等级,according the value compared to breakpoints and get the grade
# def grade(score,breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]

# print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

#二分查找 binary search
A = [1,2,2.5,3,3.5,4,5]
# A = [1,2,2.5,3,3.5,4,5]

# def binary_search_bisect(lst, x):
#     from bisect import bisect_left
#     i = bisect_left(lst, x)
#     if i != len(lst) and lst[i] == x:
#         return i
#     return None

def binary_search_bisect(lst, x):
    from bisect import bisect_left
    i = bisect_left(lst, x)
    if  lst[i] == x:
        return i
    return None

# print(binary_search_bisect(A,4))
print(binary_search_bisect(A,5))