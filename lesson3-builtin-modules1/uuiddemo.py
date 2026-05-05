"""
uuid builtin module
methods
uuid.uuid1() # 用MAC地址，序列号和当前事件输出UUID
uuid.uuid3() # 用我们指定是namespace和字符串生成UUID
uuid.uuid4() # 生成一个随机的UUID
uuid.uuid5() # 和uuid3() 类似，只不过是用sha1生成UUID

# Representations of uuid1() 用uuid1()生成的对象有下面的字段属性
# bytes : Returns id in form of 16 byte string.
# int : Returns id in form of 128-bit integer.
# hex : Returns random id as 32 character hexadecimal string.
# Components of uuid1()
# version : version number of UUID.
# variant : The variant determining the internal layout of UUID.
# Fields of uuid1()
# time_low : The first 32 bits of id.
# time_mid : The next 16 bits of id.
# time_hi_version : The next 16 bits of id.
# clock_seq_hi_variant : Next 8 bits of id.
# clock_seq_low : Next 8 bits of id.
# node : Last 48 bits of id.
# time : Time component field of id.
# clock_seq : 14 bit sequence number.
"""
import uuid

id = uuid.uuid1()

# # Representations of uuid1()
# print ("The Representations of uuid1() are : ")
# print ("byte Representation : ",end="")
# print (repr(id.bytes)) # byte Representation : b'\xb5fm\x1cA\xbc\x11\xf1\x80\xc9\x94\xbbCV1]'

# print ("int Representation : ",end="")
# print (id.int) # int Representation : 241122094538019562272827473745052840285

# print ("hex Representation : ",end="")
# print (id.hex) # hex Representation : b5666d1c41bc11f180c994bb4356315d

# print("\n")

# # Components of uuid1()
# print ("The Components of uuid1() are : ")
# print ("Version  : ",end="")
# print (id.version) # Version  : 1

# print ("Variant : ",end="")
# print (id.variant) # Variant : specified in RFC 4122

# print("\n")

# # Fields of uuid1()
# print ("The Fields of uuid1() are : ")
# print ("Fields  : ",end="")
# print (id.fields) # Fields  : (3043388700, 16828, 4593, 128, 201, 163532009517405)

# print("\n")

# # Time Component of uuid1()
# print ("The time Component of uuid1() is : ")
# print ("Time component  : ",end="")
# print (id.node) # Time component  : 163532009517405

name = "python"
print(uuid.uuid1()) # 2a796b3b-41bd-11f1-a970-94bb4356315d
print(uuid.uuid5(uuid.NAMESPACE_URL,name)) #344979f2-3e10-505c-89bf-2d5c0fefed8d
print(uuid.uuid3(uuid.NAMESPACE_DNS,name)) # c9f8b609-b81e-3c95-8188-914324e741c8
print(uuid.uuid4()) # 987c63b-41af-4796-bf4b-ef8fd56f3c7c

