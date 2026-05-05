"""
yaml module
load()
dump()
load_all()
dump_all()
safe_load()
safe_dump()
safe_load_all()
safe_dump_all()

reference site: https://www.geeksforgeeks.org/python/reading-and-writing-yaml-file-in-python/
"""

import yaml

# load(file handle)
with open("student.yaml") as f:
    res = yaml.load(f,Loader=yaml.FullLoader)
    # print(res)


# dump()
# dct = {'a':'python','b':'java'}
# res1 = yaml.dump(dct) # dump into a variable
# print(res1)
# dump() also can output to file
# config = {
#     'database': {
#         'host': 'localhost',
#         'port': 5432
#     },
#     'debug': True
# }

# # Writing to a file
# with open('output.yaml', 'w') as file:
#     yaml.dump(config, file, default_flow_style=False)


# load_all()
string = '''
---
name: tony
age: 20
---
name: lisy
age: 29
'''

# res2 = yaml.load_all(string,Loader=yaml.FullLoader)
# for data in res2:
#     print(data)

# safe_load(file handle)
with open("student.yaml") as f:
    res = yaml.safe_load(f)
    # print(res)  # {'name': 'zhangsan', 'age': 37, 'lower student': {'name': 'lisi', 'age': 25}, 'higher student': [{'name': 'wangwu', 'age': 35}, {'name1': 'zhaoliu', 'age1': 42}]}


# dump_all()
 # 4.将多段输出到yaml文件
# obj1 = {"name": "James", "age": 20}
# obj2 = ["Lily", 19]

# with open(r'a.yaml', 'w') as f:
#     yaml.dump_all([obj1, obj2], f)

# safe_dump()
config = {
    'database': {
        'host': 'localhost',
        'port': 5432
    },
    'debug': True
}

# Writing to a file
with open('conf.yaml', 'w') as file:
    yaml.safe_dump(config, file, default_flow_style=False)

