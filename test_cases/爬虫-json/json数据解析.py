# -*- coding: UTF-8 -*-
# @Time: 2021/1/30 15:40
# @File: json数据解析.py
import json

#json字符串转成 python字典
#get 请求获取到的即为json字符串
jsonStr = '{"name":"c","age":18,"hobby":["movie","learn"],"friend":{"1":"a","2":"b"}}'
jsonData = json.loads(jsonStr)
print(type(jsonData),jsonData)
print(jsonData["name"])

#python字典转成 json字符串
jsonData2 = {"name":"c","age":18,"hobby":["movie","learn"],"friend":{"1":"a","2":"b"}}
jsonStr2 = json.dumps(jsonData2)
print(type(jsonStr2),jsonStr2)
