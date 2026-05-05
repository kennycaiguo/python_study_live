"""
hashlib module

"""
import hashlib 
import os
# string hashing
# md5
# string = "Hello World"
# h = hashlib.md5(string.encode('utf-8'))
# print(h.hexdigest()) # b10a8db164e0754105b7a99be72e3fe5

# sha = hashlib.sha256(string.encode('utf-8'))
# print(sha.hexdigest()) # a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

# file hashing
fpath = os.path.abspath(__file__)
dir = os.path.dirname(fpath)
filedir = os.path.join(dir,"data.txt") # absolute path of a file

with open(filedir,'rb') as f:
    dg = hashlib.file_digest(f,"sha256")
    print(dg.hexdigest()) # 257d926d346543acb917940738e71d2b068d5a885123b1d7cea4e7babddcf8f7
print("=========================")

# password hashing
pwd =  b"user_password"
salt = os.urandom(16)

dk = hashlib.pbkdf2_hmac("sha256",pwd,salt,100000)
print(dk.hex()) # cbf7ca996d8d0707638daa1708f5783f1c46e0903beb59c4cc5c0be98408192c