"""
pickle module

"""
import pickle

Leo = {'key' : 'Leo', 'name' : 'Leo Johnson', 'age' : 21, 'pay' : 40000}
Harry = {'key' : 'Harry', 'name' : 'Harry Jenner','age' : 50, 'pay' : 50000}

data = {}
data["Leo"] = Leo
data["Harry"] = Harry

# dumps() and loads() 
# data_str = pickle.dumps(data)
# print(data_str,type(data_str)) #  <class 'bytes'>

# obj = pickle.loads(data_str)
# print(obj["Leo"],type(obj)) # {'key': 'Leo', 'name': 'Leo Johnson', 'age': 21, 'pay': 40000} <class 'dict'>

# dump(data,file handle) and load(file handle) # you need to open the file first and get the file handle
# with open("emp.pkl",'ab') as f:
#     pickle.dump(data,f)

with open("emp.pkl",'rb') as f:
    data = pickle.load(f)
    print(data)
