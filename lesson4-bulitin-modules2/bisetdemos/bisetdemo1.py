"""
python biset module
"""
import bisect

# 示例有序列表
sorted_list = [1, 3, 3, 5, 7, 9]

# 插入元素4
bisect.insort_left(sorted_list, 4)
print(f"插入元素4后的列表：{sorted_list}") # 插入元素4后的列表：[1, 3, 3, 4, 5, 7, 9]