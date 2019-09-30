import time
import random


print(dir(time))


t = time.time()
print(t)            # 1568630897.982993


print(time.localtime())
# time.struct_time(tm_year=2019, tm_mon=9, tm_mday=16, tm_hour=16, tm_min=18, tm_sec=17, tm_wday=0, tm_yday=259, tm_isdst=0)

time_format = "%Y-%m-%d %H:%M:%S %Z"
lt = time.localtime()
ft = time.strftime(time_format, lt)
print(ft)

print(time.ctime())
print(time.asctime())

t = time.perf_counter()
time.sleep(0.2)
print(time.perf_counter()-t)
print(time.asctime())
print(time.ctime())
while True:
    t = time.time()
    rtime = random.randint(10000000, 100000000)
    print(time.ctime(rtime))
    time.sleep(.5)
    #if time.time() > t + 10:
    break

year = 1995
month = 1
day = 4

import datetime

dt = datetime.date(year=year, month=month, day=4)
print(dt.strftime("%d-%B-%Y %A %Z"))
print(type(dt))

dt2 = datetime.date.today()
life = dt2 - dt
print(dt2, dt, type(life), life)
print(life.total_seconds())

#dt3 = datetime.time.strftime("%a %Y, %b %d %H:%M:%S %Z")
dt3 = datetime.datetime.now() #%a %Y, %b %d %H:%M:%S %Z")
dt3 = dt3.strftime("%a %Y, %b %d %H:%M:%S %Z")
print(dt3)


import time
from datetime import datetime
print(time.timezone)


import pytz
local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %I:%M:%S %p"))
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %I:%M:%S %p"))
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %I:%M:%S %p"))

tz_usa = pytz.timezone('US/Pacific')
datetime_London = datetime.now(tz_usa)
print("Pacific:", datetime_London.strftime("%m/%d/%Y, %I:%M:%S %p"))

