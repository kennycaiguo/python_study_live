"""
dbm.open() 模式参数详解dbm.open(filename, flag='r', mode=0o666) 中的 flag 参数决定了文件的操作模式：模式 
描述'r'只读（默认）'w'读写，不创建新文件'c'读写，如果不存在则创建（最常用）'n'始终创建新空数据库，进行读写
"""

import  dbm

def create_data():
    db = dbm.open("user.db",'c')
    db['user_id'] = '1'
    db['name'] = "Kenny rogers"
    db.setdefault(b"age", b"30")
    db.close()

def show_data():
    db=dbm.open("user.db",'r')
    for k, v in db.items():
        print(f"{k.decode()}: {v.decode()}")

    print(f"keys: {db.keys()}") # Output: keys: [b'age', b'name', b'user_id']
    print(f"values: {list(db.values())}") # Output: values: [b'30', b'John Doe', b'1']
    db.close()

def change_data(): # after you change data,you need to close the db first,or something comes out strange
     db = dbm.open("user.db",'c') 
     db['user_id'] = '2'
     db['name'] = b"James Lou"
     db['gender'] = 'male'
     db.close()

def del_record():
      db = dbm.open("user.db",'c') 
      # del the gender field
      del db['gender']
      db.close()  

def search_key():
    db = dbm.open("user.db",'c')   
    print("name" in db)  #True
    print("age" in db) #True
    print("gender" in db)# False

if __name__ == '__main__':
    # create_data()
    # show_data()
    # change_data()
    # del_record()
    search_key()