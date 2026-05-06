"""
python biset module

bisect_left(a, x): Binary searches for the correct insertion point for \(x\) in list \(a\) (assuming \(a\) is already sorted) and returns the index. It does not change the list.
insort_left(a, x): Binary searches for the correct insertion point (same as bisect_left) and then calls list.insert() to insert the value \(x\) into list \(a\) in-place.
bisect_left: 返回一个整数索引。
insort_left: 返回 None，它直接修改原列表。
"""
import bisect

# might have problem?
class Item:
    def __init__(self,value):
        self.value = value

# items =[Item(i) for i in (1,3,5,7)]   # List Comprehension    
items = [Item(1), Item(3), Item(5), Item(7)]
# 自定义比较函数
def compare(item:Item,other):
    return item.value - other.value
# get the insert position using compare function
# insert_pos = bisect.bisect_left(items,4,key=lambda x:compare(x,Item(4)))
insert_pos = bisect.bisect_right(items,4,key=lambda x:compare(x,Item(4)))

print(f"The insert position is {insert_pos}")
