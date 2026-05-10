from dataclasses import dataclass, field
import uuid
from datetime import date

@dataclass
class Book:
    """一个表示图书信息的数据类"""
    
    # 图书的基本信息，创建实例时必须提供
    title: str          # 书名
    author: str         # 作者
    price: float        # 价格
    
    # 图书的唯一标识，使用UUID自动生成，比较对象时忽略此字段
    book_id: str = field(
        default_factory=lambda: str(uuid.uuid4())[:6],  # 生成6位的唯一ID
        compare=False                                   # 比较对象时不考虑这个字段
    )
    # 出版日期，默认使用当前日期，比较对象时忽略此字段
    publish_date: date = field(
        default_factory=date.today                     # 默认使用今天的日期
    )
    # 内部库存编码，有默认值，打印对象时不显示此字段
    inventory_code: str = field(
        default="N/A",                                  # 默认值为"N/A"
        compare=False,
        repr=False                                      # 打印对象时不显示这个字段
    )

# 创建两本内容相同的图书实例
book1 = Book("Python编程", "张三", 59.90, inventory_code="PY-001")
book2 = Book("Python编程", "张三", 59.90, inventory_code="PY-002")

# 打印第一本书的信息（不会显示inventory_code）
print("第一本书信息:", book1)
# 比较两本书是否相等（只会比较title, author, price）
print("两本书是否相等?", book1 == book2)

# 访问被隐藏的字段
print("第一本书的库存编码:", book1.inventory_code)
print("第一本书的ID:", book1.book_id)

