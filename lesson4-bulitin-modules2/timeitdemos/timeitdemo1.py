from timeit import timeit,repeat
## ex1
# res1 = timeit(stmt="[i for i in range(1000)]",number=100)

# statment = """
# l = []
# for i in range(1000):
#     l.append(i)

# """

# res2 = timeit(stmt=statment,number=100)

# #3、stmt值为一个函数
# def addelem():
#     l = []
#     for i in range(1000):
#         l.append(i)

# res3 = timeit(stmt=addelem,setup='from __main__ import addelem',number=100)

# # print(res1) # 0.0015446000033989549 列表推导式的效率比循环要高
# # print(res2) # 0.001992899997276254
# # print(res3) # 0.0019971000001532957

# ex2
# from timeit import timeit

# res = timeit(stmt="json.loads(json_data)",number=1000,
#            setup="import json;data={'name':'egon','age':18};json_data=json.dumps(data)"
#            )
# print(res) # 0.0011855000047944486