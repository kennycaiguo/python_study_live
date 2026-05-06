"""
decimal builtin module
"""

import json
from decimal import Decimal

data = {'price': Decimal('99.99')}
# 直接转 JSON 会报错，需要自定义 default 函数
# json.dumps(data) # TypeError: Object of type Decimal is not JSON serializable

def decimal_to_str(obj):
    if isinstance(obj,Decimal):
        return str(obj)
    raise TypeError

json_str = json.dumps(data,default=decimal_to_str)
print(json_str)  # {"price": "99.99"}
# 在存入数据库（如 PostgreSQL 或 MySQL）时，通常建议使用字符串格式或者数据库原生的 DECIMAL 类型进行对接。


