"""
calendar built-in module
methods:

calendar.calendar(year) # return a one year carlendar
calendar.calendar(year,month) # return a one month carlendar of that year
calendar.weekday(year,month,day) # return the weekday of a day
calendar.isleap(year) # whether a year is leap year or not
carlendar.leapdays(start,end) # return how many leap years between start and end
calendar.timegm((y,m,d,h,m,s)) # turn a time tuple into a timestamp
calendar.monthcalendar()返回装着某年某月日历的二维列表
calendar.monthrange()返回包含了两个整数的元组，分别是某年某月第一天是周几，该月有多少天
calendar.firstweekday() # 返回一周第一天的编号,默认是0
setfirstweekday()设置一周的起始日期码,默认一周第一天为0,即周一

"""

import calendar

# print("calendar(years)返回某一年的日历：")       # calendar.prcal(2021)同样也可以实现此功能
# print(calendar.calendar(2021))

# print("firstweekday()返回每周的起始日：",calendar.firstweekday())       # 输出 ：0

# print("isleap()返回是否是闰年：",calendar.isleap(2016), calendar.isleap(2017))    # True ,False

# print("leapdays()返回两年之间的闰年总数：",calendar.leapdays(2000, 2013))  # leapdays()返回两年之间的闰年总数： 4

# print("month()返回某年某月的日历：",calendar.month(2021, 10))  # calendar.prmonth(2021, 10) 同样的效果

# print("calendar.monthcalendar()返回装着某年某月日历的二维列表：")
# print(calendar.monthcalendar(2021, 1))

# print("calendar.monthrange()返回包含了两个整数的元组，分别是某年某月第一天是周几，该月有多少天：")
# print(calendar.monthrange(2021, 1)) # 返回(4, 31)，4表示该月第一天为周五，31表示该月有31天

# print("setfirstweekday()设置一周的起始日期码,默认一周第一天为0,即周一：")
# calendar.setfirstweekday(1)
# print(calendar.firstweekday())      # 返回1
print("weekday()返回某年某月某日是周几：",calendar.weekday(2021, 1, 25)) 
