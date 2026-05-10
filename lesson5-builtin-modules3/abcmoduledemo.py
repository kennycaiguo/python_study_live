from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sound():
        pass


class Fish(Animal):  # 必须实现所有抽象类的方法，否则无法创建对象
    def __init__(self,name):
        self.name = name

    def eat(self):
        pass    # 写pass也是一种实现，叫做空实现

    def move(self):
        print(f"Fish {self.name} is swimming...")

    def sound(self):
        print(f"Fish {self.name} doesn't make any sound...")

def test_fish():
    f = Fish("nimo")    
    f.move()
    f.sound()   

class Person(ABC):
    @property # 把一个方法作为属性来使用，此时这个属性是只读的。
    @abstractmethod
    def name() -> str:
        pass

    @abstractmethod
    def speak():
        pass

class Emp(Person):
    def __init__(self,first,last):
        self.__fullname = f"{first} {last}"

    @property
    def name(self):
       return self.__fullname
    
    def speak(self):
        print(f"Hello,my name is {self.name}")

def test_person():
    p = Emp("Jack","Daniel")        
    print(f"Name:{p.name}")
    p.speak()

if __name__  == '__main__':
    # test_fish()
    test_person()