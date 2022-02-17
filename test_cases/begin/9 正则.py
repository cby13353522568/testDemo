# -*- coding: UTF-8 -*-
# @Time: 2022/2/8 19:26
# @File: 9 正则.py

import re

str01 = "13353522568"
print(re.findall(R"^1[3578]\d{9}$",str01))  # 返回string中所有与pattern相匹配的全部字符串，返回形式为集合
print(re.match(R"^1[3578]\d{9}$",str01))   # string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None

str02 = "browser uses BBC’s https://www.apple.com If you’re  http://www.bt.cn thank you"
print(re.findall(r"\b(?:http|https)[:/\w.]*(?:cn|com)\b",str02))
