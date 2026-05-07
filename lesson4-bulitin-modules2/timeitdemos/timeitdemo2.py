from timeit import timeit,repeat,Timer

def addelem():
    l = []
    for i in range(1000):
        l.append(i)

res31 = timeit(stmt=addelem, number=100)
res32 = Timer(lambda: addelem).repeat(repeat=1, number=100)  # Timer对象很慢
print(res31)
print(res32)

res = repeat(stmt="[i for i in range(1000)]", number=100, repeat=10)
print(res) #[0.002173500004573725, 0.0027968999929726124, 0.002493499996489845, 0.0018925000040326267, 0.0014866000128677115, 0.002145499995094724, 0.0017737000016495585, 0.0021572999976342544, 0.0017435999907320365, 0.0016152000025613233]