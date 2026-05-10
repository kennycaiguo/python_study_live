from dataclasses import dataclass, field  # 导入field函数

@dataclass
class GoodPerson:
    name: str
    # 使用list作为工厂函数，每次创建实例时生成新列表
    hobbies: list = field(default_factory=list)

p1 = GoodPerson("Alice")
p1.hobbies.append("reading")
print(p1.hobbies)
p2 = GoodPerson("Bob")
print(p2.hobbies)  # 输出[]，每个实例有独立的列表！
