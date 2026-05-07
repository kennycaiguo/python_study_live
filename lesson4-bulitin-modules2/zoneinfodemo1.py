import zoneinfo
from datetime import  datetime,timedelta,timezone

tz = zoneinfo.ZoneInfo("Pacific/Kwajalein")

date_utc = datetime(2021,11,7,20,tzinfo=timezone.utc)

date_tz = date_utc.astimezone(tz)

date_tz_dst = date_tz+timedelta(hours=1)

print("utc时间：",date_utc)
print("tz时间：",date_tz)
print("tz_dst时间：",date_tz_dst)
print("时区简称：",date_utc.tzname())

