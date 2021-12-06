# -*- coding: UTF-8 -*-
# @Time: 2020/12/19 17:23
# @File: 3 时间类.py
import datetime
import time
print(dir(datetime))
#今天
today=datetime.date.today()
print(today)
#昨天
print(today - datetime.timedelta(days=1))  #补时差 today + datetime.timedelta(hours=8)
#上个月
print(today.month - 1 if today.month - 1 else 12)
#当前时间戳
time_stamp = time.time()
print("time_stamp",time_stamp)
#时间戳转datetime
print(datetime.datetime.fromtimestamp(time_stamp))
#datetime转时间戳
print(today.timetuple())
print(int(time.mktime(today.timetuple())))
#datetime转字符串
today_str = today.strftime("%Y%m%d")
print(today_str)
#字符串转datetime
today2 = datetime.datetime.strptime(today_str, "%Y%m%d")
print(today2)


d1 = datetime.date.today()
d2 = datetime.date(2020, 11, 26)
print((d1 - d2).days)

