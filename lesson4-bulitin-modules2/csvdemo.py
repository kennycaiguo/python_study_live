"""
python csv built-in module
"""
import csv

# 1.create a csv file method1
# data = [['姓名', '年龄'], ['张三', 25], ['李四', 30]]
# with open("test.csv",mode='w',encoding='utf-8-sig',newline='') as f:
#     csv_writer = csv.writer(f) # create a csv writer
#     csv_writer.writerows(data)

# # 2.create a csv method2
# fields = ["name","age","gender"]   
# rows =[
#    {"name":"Magret","age":19,"gender":"female"}, 
#    {"name":"Mark","age":17,"gender":"male"}, 
#    {"name":"Jerry","age":18,"gender":"male"}, 
#    {"name":"Jesse","age":18,"gender":"female"}, 
#    {"name":"Beckey","age":18,"gender":"female"}, 
# ] 
# with open("test2.csv",mode='w',encoding='utf-8-sig',newline='') as f:
#     dict_writer = csv.DictWriter(f,fieldnames=fields)
#     dict_writer.writeheader() # no params
#     # dict_writer.writerow({"name":"Mary","age":18,"gender":"female"})
#     dict_writer.writerows(rows)

# 3.read method1
# with open("test2.csv",mode='r',encoding='utf-8-sig',newline='') as f:
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         print(row)

# 4.read csv method 2
with open("test2.csv",mode='r',encoding='utf-8-sig',newline='') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(row)