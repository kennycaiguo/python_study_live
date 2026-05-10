from dataclasses import dataclass
from datetime import datetime

@dataclass # 这个注解帮我们实现__init__,__eq__,__repr__和__hash__方法，他所注解的类的所有成员都应该是公有的
class Person:
    name:str
    age:int
    email:str = "agirldating@gmail.com"

    def sayhello(self):
        print(f"Hello,My name is {self.name},I am {self.age} years old,email:{self.email}")

      # 自定义方法：检查是否成年
    def is_adult(self) -> bool:
        """判断是否达到成年年龄(18岁)"""
        return self.age >= 18    
    
    # @property计算属性：出生年份（基于当前年龄推算）
    @property
    def birth_year(self) -> int:
        """根据当前年龄和年份，计算出生年份"""
        current_year = datetime.now().year
        return current_year - self.age
    
if __name__ == '__main__':
    p1 = Person("Jack",18)  # True   
    p2 = Person("Jesse",20)
    print(p1== Person("Jack",18))
    print(p2) # Person(name='Jesse', age=20, email='agirldating@gmail.com')
    p2.sayhello() # Hello,My name is Jesse,I am 20 years old,email:agirldating@gmail.com
    print(p1.birth_year) # 2008