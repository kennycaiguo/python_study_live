from dataclasses import (
    dataclass, asdict, astuple, replace, fields, 
    is_dataclass, make_dataclass, InitVar,field
)

# 定义基础数据类（含InitVar演示）
@dataclass
class Person:
    name: str
    age: int
    # InitVar标记：address仅用于初始化，不会成为实例属性
    address: InitVar[str] = field(default="未知地址")  # 设置默认值

    def __post_init__(self, address):
        # 利用InitVar参数初始化实例属性
        self.full_info = f"{self.name} ({self.age}), 地址: {address}"

# 创建实例
person = Person("Alice", 30, "123 Main St")

# 1. asdict()：转字典
print("asdict结果:", asdict(person))

# 2. astuple()：转元组
print("astuple结果:", astuple(person))

# 3. replace()：创建副本并修改字段
new_person = replace(person, age=31)
print("replace后的实例:", new_person)

# 4. fields()：获取字段信息
print("\n字段信息:")
for field_info in fields(person):
    print(f"字段名: {field_info.name}, 类型: {field_info.type}, 是否InitVar: {isinstance(field_info.type, InitVar)}")

# 5. is_dataclass()：判断是否为数据类
print("\nis_dataclass(Person):", is_dataclass(Person))
print("is_dataclass(person):", is_dataclass(person))
print("is_dataclass(dict):", is_dataclass(dict))

# 6. make_dataclass()：动态创建数据类
DynamicPerson = make_dataclass(
    "DynamicPerson",  # 类名
    [("name", str), ("age", int)],  # 字段列表
    namespace={"greet": lambda self: f"Hello, {self.name}!"}  # 额外方法/属性
)
dynamic_person = DynamicPerson("Bob", 25)
print("\n动态创建的数据类实例:", dynamic_person)
print("动态类方法调用:", dynamic_person.greet())
