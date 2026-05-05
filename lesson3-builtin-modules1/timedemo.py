"""
time.time() # get the current time in timestamp format
time.localtime = > get a time_struct  like time.struct_time(tm_year=2026, tm_mon=4, tm_mday=20, tm_hour=14, tm_min=40, tm_sec=40, tm_wday=0, tm_yday=110, tm_isdst=0)
time.strftime(format,time_struct) # convert the time_struct into a string time format
time.strptime(time string,format) # turn the time string into time_struct
"""
import time

print(time.time()) # 1776717537.781657
# print(time.localtime()) # time.struct_time(tm_year=2026, tm_mon=4, tm_mday=20, tm_hour=14, tm_min=40, tm_sec=40, tm_wday=0, tm_yday=110, tm_isdst=0)
time_struct = time.localtime()
print(time.strftime("%Y-%m-%d %X",time_struct)) # 2026-04-20 14:44:55
print(time.strptime("2026-04-20 14:44:55","%Y-%m-%d %X"))


