"""
the datetime module has three classes: time,date,datetime
now ,we going to learn the datetime classs of datetime module
dt.year
dt.month
dt.day
dt.hour
dt.minute
dt.second
dt.microsecond

methods
now()
today()
timestamp()
fromtimestamp()
combine(date object,time object) -> datetime string

"""
from datetime import datetime ,date,time,timedelta

dt = datetime(2020,9,22,10,35,28,322)
"""properties"""

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
"""methods - static methods"""
print(dt.today()) # 2026-04-22 08:01:51.438331
print(dt.now()) # 2026-04-22 08:02:17.443458
print(datetime.now())  # static method
print(dt.timestamp())  # get timestamp
print(dt.fromtimestamp(1600792528.000322)) # 2020-09-22 10:35:28.000322
print(dt.utcfromtimestamp(1600792528.000322)) # 2020-09-22 16:35:28.000322, outdated method

date1 = date(2023,10,1)
time1 = time(10,11,12)
dt1_str = datetime.combine(date1,time1)
print(dt1_str) # 2023-10-01 10:11:12

# time_del = datetime.now() - dt
# print(time_del)
# Create a duration of 1 day, 2 hours, and 30 minutes
delta = timedelta(days=3,hours=3,minutes=20)
print(datetime.now()+delta) # 2026-04-25 11:41:13.462189
print(datetime.now()-timedelta(days=3)) # 2026-04-19 08:23:53.430154
dt2 = datetime(2026,4,22,10,35,28,322)
print(datetime.strptime("2026-04-22 10:00:00","%Y-%m-%d %H:%M:%S"))