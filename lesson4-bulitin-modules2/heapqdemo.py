"""
python heapq
"""
import heapq
# 1.基本使用
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap = []
for i in array:
    heapq.heappush(heap,i) # heappush(heap,list)
print(heap)  
heapq.heapify(array)   # heapq.heapify(list)
print(array)

# 2 堆排序
heap_sorted = [heapq.heappop(heap) for _ in range(len(heap))]
print(heap_sorted) # [5, 7, 10, 15, 17, 21, 24, 27, 30, 36, 45, 50]

# 3.获取堆中的最小值或最大值
print(heapq.nlargest(2,array))
print(heapq.nsmallest(2,array))

# 4.使用heapq合并两个有序列表,不会删除相同的样式
array_a = [10, 7, 15, 8]
array_b = [17, 3, 8, 20, 13]
array_merge = heapq.merge(sorted(array_a), sorted(array_b))
print("merge result:", list(array_merge)) # merge result: [3, 7, 8, 8, 10, 13, 15, 17, 20]

# 5，heapq替换数据的方法
array_c = [10, 7, 15, 8]
heapq.heapify(array_c)
print("before:", array_c)
# 先push再pop
item = heapq.heappushpop(array_c, 5)
print("after: ", array_c)
print(item)

array_d = [10, 7, 15, 8]
heapq.heapify(array_d)
print("before:", array_d)
# 先pop再push
item = heapq.heapreplace(array_d, 5)
print("after: ", array_d)
print(item)


