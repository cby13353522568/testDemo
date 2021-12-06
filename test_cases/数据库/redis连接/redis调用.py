# -*- coding: UTF-8 -*-
# @Time: 2021/2/20 13:49
# @File: redis调用.py
from cRedis import CRedis

re = CRedis("123456")
print(re.get("sss"))