from enum import Enum

from enum import Enum

# 继承Enum类
class Status(Enum):
    WORKING = "努力工作赚钱养家！"
    BREAK = "休息是为了重新出发！"
    EATING = "好好吃饭，健康成长！"
    SLEEPING = "祝你做个好梦！"
    
    @classmethod
    def status(cls, hour):
        if hour < 7 or hour >= 23:
            return cls.WORKING
        elif 7 <= hour < 9 or 17 <= hour < 18: 
            return cls.EATING
        elif 9 <= hour < 12 or 14 <= hour < 17:
            return cls.WORKING
        else:
            return cls.BREAK

# 通过name访问
s = Status["WORKING"]
print(s.name, s.value)
# 通过value访问
s = Status("祝你做个好梦！")
print(s.name, s.value)
# 调用类方法
print(Status.status(9))