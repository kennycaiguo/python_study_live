import hmac
import hashlib

def demo1():
    msg = b'Hello World'
    key = b'secret'
    res = hmac.new(msg,key,digestmod='MD5')
    # might need update...
    print(res.hexdigest()) # 8a315e3168dcd347b8bb3e2517da7b4d

def demo2():
    str1 ="zhaoliying"
    encodede = hmac.new(b"welcome to my lesson",bytes(str1,'utf-8'),hashlib.sha1)
    print(encodede.hexdigest())

# 二进制摘要
def demo3():
      str1 ="zhaoliying"
      encodede = hmac.new(b"welcome to my lesson",bytes(str1,'utf-8'),hashlib.sha1)
      print(encodede.digest())    

def demo4():
     # 网络通信中的HMAC签名生成和验证
    # 发送端
    message = b"Hello, HMAC!"
    key = b"secret_key"
    hmac_signature = hmac.new(key, message, hashlib.sha256).digest()

    # 将数据和HMAC签名一同发送

    # 接收端
    received_message = b"Hello, HMAC!"
    received_signature = hmac.new(key, received_message, hashlib.sha256).digest()

    if hmac.compare_digest(received_signature, hmac_signature):
        print("Message integrity verified.")
    else:
        print("Message integrity compromised!")      

if __name__ == '__main__':
    # demo1()
    # demo2()     # e834574a043ae5d490c04c38efdd07e69efbed7f
    # demo3() # b'\xe84WJ\x04:\xe5\xd4\x90\xc0L8\xef\xdd\x07\xe6\x9e\xfb\xed\x7f'
    demo4()

