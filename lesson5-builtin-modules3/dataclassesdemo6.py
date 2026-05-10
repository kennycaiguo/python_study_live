"""
数据类既可以作为父类被其他数据类继承，也可以被普通Python类继承：当数据类继承另一个数据类时，子类会自动合并父类的字段；而普通类继承数据类时，
若需使用父类的字段和构造逻辑，则必须手动调用父类的构造函数并处理相关参数。
"""
from dataclasses import dataclass

# 🟡 基类：形状（数据类）
@dataclass
class Shape:
    color: str

# 🟦 子类：正方形（数据类）
@dataclass
class Square(Shape):
    side_length: float = 1.0  # 默认边长为1

# 🟢 子类：圆形（普通类，不是数据类）
class Circle(Shape):
    def __init__(self, color: str, radius: float = 1.0):
        # 必须手动调用父类的构造函数来初始化 color
        super().__init__(color)
        self.radius = radius
    
    # 如果需要友好的打印格式，必须自己实现 __repr__ 方法
    def __repr__(self):
        return f"Circle(color='{self.color}', radius={self.radius})"

# 使用示例
red_square = Square("red")
print(red_square) 

blue_circle = Circle("blue", 5.0)
print(blue_circle) 

default_circle = Circle("green")
print(default_circle) 
