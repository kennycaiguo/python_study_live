import sqlite3 # open terminal to run the script

#1.create db
conn = sqlite3.connect("mydb.db")

# 创建游标对象执行 SQL 命令
cursor = conn.cursor()

# 2.create table
cursor.execute(
    """
   create table if not exists users(
     id integer primary key,
     name varchar(50) not null,
     age integer,
     email text unique
   )
"""
)

conn.commit()
# # 3.insert data
# ## insert one data
# cursor.execute("""
# insert into users(name,age,email) values(?,?,?)
# """,("Linda",20,"Lindaislinda@gmail.com"))
# ## batch insert 
# datas = [
#     ("Linda2",22,"Linda2islinda@gmail.com"),
#     ("Lindy",20,"Lindyislinda@gmail.com"),
#     ("Jack",21,"Jack1234@gmail.com")
# ]
# cursor.executemany("""
# insert into users(name,age,email) values(?,?,?)
# """,datas)
# # don't forget to commit->connection obj
# conn.commit()

# 4.query datas
## show everything
# cursor.execute("select * from users") # no return value
# users_data = cursor.fetchall() # needs to receive the return value
# print(users_data)
# # get some not all
# cursor.execute("select * from users") # no return value
# users_data = cursor.fetchmany(3) # needs to receive the return value
# print(users_data) # [(1, 'Linda', 20, 'Lindaislinda@gmail.com'), (2, 'Linda2', 22, 'Linda2islinda@gmail.com'), (3, 'Lindy', 20, 'Lindyislinda@gmail.com')]
## query by term
# cursor.execute("select * from users where name=?",("Linda",)) # no return value
# user = cursor.fetchone() # needs to receive the return value
# print(user)  # (1, 'Linda', 20, 'Lindaislinda@gmail.com')

# cursor.execute("select * from users where age<?",(22,)) # no return value
# user = cursor.fetchall() # needs to receive the return value
# print(user)  # [(1, 'Linda', 20, 'Lindaislinda@gmail.com'), (3, 'Lindy', 20, 'Lindyislinda@gmail.com'), (4, 'Jack', 21, 'Jack1234@gmail.com')]

# 5.update data
# cursor.execute("update users set name=?,age=? where age>?",("John",18,21))
# conn.commit()

# 6.delete
cursor.execute("delete from users where name=?",("Lindy",))
conn.commit()