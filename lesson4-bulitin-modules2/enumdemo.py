from enum import Enum

class Status(Enum):
    Good=100
    Normal=80
    Ok=70
    Soso=60
    Bad = 50


print(Status.Bad.value < 60)  # True

# Status.Bad.value = 30 #错误，枚举的值不允许修改
# print(Status.Bad.value) # AttributeError: <enum 'Enum'> cannot set attribute 'value'

print(len(Status)) # 5

class Duty(Enum):
    WORKING = "努力工作赚钱养家！"
    BREAK = "休息是为了重新出发！"
    EATING = "好好吃饭，健康成长！"
    SLEEPING = "祝你做个好梦！"

def what_to_do(d:Duty):
    print(d.value)  

what_to_do(Duty.WORKING)    