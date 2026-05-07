from typing import Dict, List, Tuple, Set

# user_info: Dict[str, int] = {"age": 18, "id": 1001}
# scores: List[float] = [98.5, 88.0, 100.0]
# point: Tuple[int, int, int] = (10, 20, 30)          # 定长定类型
# flexible_tuple: Tuple[int, ...] = (1, 2, 3, 4)      # 变长同类型（Python 3.11+ 更优雅）
# unique_ids: Set[str] = {"id1", "id2"}

from typing import Sequence

def print_reverse(s:Sequence[int]):
    print(s[::-1])

# print_reverse([1,2,3,6,7])
print_reverse((1,2,3,6,7)) # (7, 6, 3, 2, 1)
print_reverse(('a','b','c','d')) # ('d', 'c', 'b', 'a')

from typing import Optional

def greet(name: Optional[str] = None) -> None:
    print(f"Hello, {name or 'Guest'}")

greet() # Hello, Guest
greet("Lili") # Hello, Lili

from typing import Callable

def calculate(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

print(calculate(3, 4, lambda x, y: x * y)) # 12
