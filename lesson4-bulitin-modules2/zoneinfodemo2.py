from datetime import datetime
from zoneinfo import ZoneInfo

tokyo_time = datetime.now(ZoneInfo("Asia/Tokyo"))
print(tokyo_time)  # 2024-01-28 14:39:17+09:00

# datetime对象
naive_datetime = datetime.now()

# 设定时区为伦敦时间
london_time = naive_datetime.replace(tzinfo=ZoneInfo("Europe/London"))

print(london_time)
# 转换到纽约时间
new_york_time = london_time.astimezone(ZoneInfo("America/New_York"))
print(new_york_time)  # 时间会自动转换到纽约时间

from datetime import timedelta

# 新加坡时间加上6小时
singapore_time = datetime.now(ZoneInfo("Asia/Singapore"))
six_hours_later = singapore_time + timedelta(hours=6)

print(six_hours_later)  # 自动考虑时区变化

