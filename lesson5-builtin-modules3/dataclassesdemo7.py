from dataclasses import dataclass, FrozenInstanceError
import weakref

# 1. init=False 示例
@dataclass(init=False)
class Person:
    name: str
    age: int
    
    # 手动定义 __init__ 方法
    def __init__(self, name):
        self.name = name
        self.age = 0  # 设置默认年龄

# 2. repr=False 示例
@dataclass(repr=False)
class Point:
    x: int
    y: int
    
    # 自定义 repr
    def __repr__(self):
        return f"Point at ({self.x}, {self.y})"

# 3. eq=True示例
@dataclass(eq=True)
class Product:
    id: int
    name: str

# 4. order=True 示例
@dataclass(order=True)
class Student:
    score: int
    name: str

# 5. unsafe_hash=True 示例
@dataclass(unsafe_hash=True)
class Book:
    title: str
    author: str

# 6. frozen=True 示例
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

# 7. match_args=True 示例 (Python 3.10+)
@dataclass(match_args=True)
class Shape:
    type: str
    size: int

# 8. kw_only=True 示例 (Python 3.10+)
@dataclass(kw_only=True)
class Car:
    brand: str
    model: str

# 9. slots=True 示例 (Python 3.10+)
@dataclass(slots=True)
class User:
    id: int
    username: str

# 10. weakref_slot=True 示例 (Python 3.11+)
@dataclass(slots=True, weakref_slot=True)
class Node:
    value: int

# 测试代码
if __name__ == "__main__":
    # 1. 测试 init=False
    p = Person("Alice")
    print(f"1. Person: {p.name}, {p.age}")
    
    # 2. 测试 repr=False
    point = Point(3, 4)
    print(f"2. Point: {point}")
    
    # 3. 测试 eq=True
    p1 = Product(1, "Apple")
    p2 = Product(1, "Apple")
    print(f"3. Products equal? {p1 == p2}")
    
    # 4. 测试 order=True
    s1 = Student(90, "Bob")
    s2 = Student(85, "Alice")
    print(f"4. s1 > s2? {s1 > s2}") # 按照参数定义顺序比较
    
    # 5. 测试 unsafe_hash=True
    book = Book("Python", "Guido")
    print(f"5. Book hash: {hash(book)}")
    
    # 6. 测试 frozen=True
    immutable_point = ImmutablePoint(1, 2)
    try:
        immutable_point.x = 3
    except FrozenInstanceError as e:
        print(f"6. Frozen error: {e}")
    
    # 7. 测试 match_args=True (Python 3.10+)
    shape = Shape("circle", 5)
    match shape:
        case Shape("circle", size):
            print(f"7. Circle with size {size}")
        case Shape("square", size):
            print(f"7. Square with size {size}")
    
    # 8. 测试 kw_only=True
    car = Car(brand="Toyota", model="Camry")
    print(f"8. Car: {car}")
    
    # 9. 测试 slots=True
    user = User(1, "admin")
    print(f"9. User: {user}")
    try:
        user.email = "admin@example.com"
    except AttributeError as e:
        print(f"9. Slots error: {e}")
    
    # 10. 测试 weakref_slot=True
    node = Node(10)
    ref = weakref.ref(node)
    print(f"10. Weakref node value: {ref().value}")
