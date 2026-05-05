"""
json module
json.loads convert json string into a dict
json.dumps convert dict into json string
json.load  convert file content into a dict
json.dump  cinvert dict into json string and save to a file
"""
import json

# loads()
# json_data = '{"name": "Alice", "active": true}'
# data = json.loads(json_data) # Converts to Python dict
# print(data["name"]) # Alice

# dumps() dict - > str
# d ={"name":"Jack","gender":"male","age":30}
# jstr = json.dumps(d)
# print(jstr,type(jstr)) # <class 'str'>

# dump(data,file handle,indent=4) # 第二个参数是file handle，也就是必须先打开一个文件。
# data = {"id": 1, "status": "ok"}
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)

# json.load(file handle) # 参数是文件句柄，不能直接传递文件名
with open('data.json', 'r', encoding='utf-8') as f:
    # 2. 用 json.load() 加载文件对象
    dic = json.load(f)
    print(dic,type(dic)) # {'id': 1, 'status': 'ok'} <class 'dict'>