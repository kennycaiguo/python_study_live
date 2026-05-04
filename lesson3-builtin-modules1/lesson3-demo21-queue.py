"""
queue builtin module
we us the Queue class more often
methods of Queue:

"""
from queue import Queue
 
 
q = Queue(maxsize=5)

# 向队列写入元素
q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')


print("返回队列的大小:",q.qsize())  # 返回队列的大小: 5


if q.full():        # 判断队列是否满了
    for x in range(5):
        print(q.get())      # 获取元素
    else:
        print("为空判断:",q.empty()) #为空判断: True

        