from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1
    total_price: float = field(init=False)  # 总价由其他字段计算
    
    def __post_init__(self):
        """初始化后自动计算总价"""
        self.total_price = self.price * self.quantity

# 使用示例
apple = Product("Apple", 5.5, 10)
banana = Product("Banana", 3.0)

print(f"Apple total: ${apple.total_price}")  # 输出: 55.0
print(f"Banana total: ${banana.total_price}")  # 输出: 3.0
