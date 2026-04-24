"""
the time submodule is different from time module,don't mixup

"""
from datetime import time # this is different from time module

## instance method
t = time(9,1,25)
# properties
print(t.hour) # 9
print(t.minute) # 1
print(t.second) #25
print(t.microsecond) #0
print(t.tzinfo) # None
## methods
print(t.replace(6,2,10)) # return a new object ,the old object no change
print(t.isoformat()) # 09:01:25
print(t.strftime("%I:%M %p")) #09:01 AM