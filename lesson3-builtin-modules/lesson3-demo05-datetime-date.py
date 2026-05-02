"""
datetime module
sub modeles:
    date : 日期类
    time : 时间类
    datetime : 日期和时间的类 ，相当于前面的两个类
    datedelta : 时间间隔

# 1.date sub module    
max
min
instance property and functions
d.year
d.month
d.day
method
d.replece # create a new date object
d.timetuple() # get a time_struct
d.toordinal() # days difference from 0001-01-01
d.weekday() # return an integar of weekdays ,monday=0
d.isoweekday() #  return an integar of weekdays ,monday=1
d.isocalendar() # return a tuple(year,week,weekday)
d.isoformat() # return a date string with "YYYY-MM-DD"
d.strftime("%Y-%m-%d")  # return a date string with "YYYY-MM-DD"
"""
from datetime import date

""" property"""
print(date.max) # 9999-12-31  9999-2026 
print(date.min) # 0001-01-01

"""instance method"""
d = date(2021,11,20)  # create a instance of date
print(d.year) # 2021
print(d.month) # 11
print(d.day) # 20

d2 = d.replace(2023,5,10) # create a new object,but the old no change
print(d) # 2021-11-20
print(d.timetuple()) # time.struct_time(tm_year=2021, tm_mon=11, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=324, tm_isdst=-1)
print(d.toordinal()) # 738114
print(d.weekday())  # 5 => saturday (monday=0)
print(d.isoweekday()) # 6 => saturday (monday=1)
print(d.isocalendar()) # datetime.IsoCalendarDate(year=2021, week=46, weekday=6)
print(d.isocalendar().year) #2021
print(d.isocalendar().week) #46
print(d.isocalendar().weekday) # 6
print(d.isoformat()) # 2021-11-20
print(d.strftime("%Y-%m-%d")) # 2021-11-20
