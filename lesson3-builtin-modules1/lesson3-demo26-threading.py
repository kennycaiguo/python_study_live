"""
threading built-in module

"""
import threading
from threading import * 
import time

# # Thread class
## ex1
# def square(num):
#     print(f"num ** 2={num **2}")
#     time.sleep(1)

# def cube(num):
#     print(f"num ** 3={num ** 3}")
#     time.sleep(1)    

# t1 = Thread(target=square,args=(4,))    
# t2 = Thread(target=cube,args=(4,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# # ex2
# def print_num():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Thread:{threading.current_thread().name},Number:{i}")

# t = Thread(target=print_num)
# t.start()

# for i in range(5): # MainThread
#     time.sleep(1)
#     print(f"Thread:{threading.current_thread().name},Number:{i}")

# # concurrent.futures.ThreadPoolExecutor
# from concurrent.futures import ThreadPoolExecutor

# def worker(task):
#     print(f"Task:{task} is running")

# with ThreadPoolExecutor(max_workers=2) as executor:
#     executor.submit(worker,1)
#     executor.submit(worker,2)

