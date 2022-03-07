# -*- coding: UTF-8 -*-
# @Time: 2020/12/19 17:23
# @File: 3 时间类.py
import datetime
import time

# time 是时间戳  datetime模块下有5个类，time时间对象，date日期对象，datetime日期时间对象，timedelta，tzinfo

# 当前时间戳
time_stamp = time.time()
print("time_stamp", time_stamp)
print("datetime", time.localtime(time_stamp))  # 把获取的时间戳转为当地的时间元组
print("格式化时间", time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  # 格式化时间  "%a-%b-%d %H:%M:%S"

today = datetime.datetime.today()  # 今天
today2 = datetime.date.today()
print(today, today2)
print(today - datetime.timedelta(days=1))  # 补时差 today + datetime.timedelta(hours=8) # 昨天
print(today.month - 1 if today.month - 1 else 12, '月')  # 上个月

# time转datetime
print("datetime", datetime.datetime.fromtimestamp(time_stamp))
# datetime转time
print("datetime转时间元组", today.timetuple())
print("datetime转时间戳",today.timestamp())
print(int(time.mktime(today.timetuple())))  # time.mktime将时间元组转化为时间戳
# datetime转字符串
today_str = today.strftime("%Y=%m=%d")
print(today_str)
# 字符串转datetime
today3 = datetime.datetime.strptime(today_str, "%Y=%m=%d")
print(today3)

d1 = datetime.date.today()
d2 = datetime.date(2021, 4, 6)
d3 = datetime.date(2022, 3, 4)
print((d3 - d2).days)
