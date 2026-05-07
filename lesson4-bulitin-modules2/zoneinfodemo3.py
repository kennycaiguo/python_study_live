from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 计算夏令时转换
dt = datetime(2024, 3, 31, 1, 30, tzinfo=ZoneInfo("Europe/London"))  # 夏令时开始时间
print(dt)  # 2024-03-31 01:30:00+00:00

# 夏令时期间加一小时
dt += timedelta(hours=1)
print(dt)  # 2024-03-31 02:30:00+01:00