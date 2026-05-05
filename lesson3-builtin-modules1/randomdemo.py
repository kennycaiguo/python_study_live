"""
ramdom module
methods:
random.random() return a float number between 0-1
random.uniform(start,end)) return a float number between start and end
random.randint(start,end)) return a integer number between start and end
random.randrange(start,end,step) almost same like randint,but it could control the step
random.shuffle(nums) # 1.prepare a list ,2.the shuffle method return None,because it will change the list
random.sample(lst,num) # 1.prepare a list 2.get a num of elements from the list,# 3.return the new list
"""
import random

# print(random.random()) # 0.6621749525544017
# print(random.uniform(1,10)) # 1.2056377672533736
# print(random.randint(1,20)) # 7
# print(random.randrange(1,40,2)) # integers only
# print(random.randrange(0.1,1.0,0.05)) # error,only integer allowed

nums = [10,2,3,5,8,7] # 1.prepare a list
# print(random.shuffle(nums)) # 2.shuffle  will change the list inplace
# print(nums) # 3.the order of elements in the list changed

print(random.sample(nums,4)) # [5, 8, 10, 2]