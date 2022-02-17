# -*- coding: UTF-8 -*-
# @Time: 2021/1/30 14:33
# @File: 模拟浏览器.py
import urllib.request
import urllib.parse

# User-Agent:浏览器信息

url = "http://www.baidu.com"
# 模拟请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

# 设置一个请求体 GET

# print(data)

# POST请求
data2 = {"wd": "cat"}
dataPost = urllib.parse.urlencode(data2).encode("UTF-8")  # post请求需要打包入参,且必须编码
reqPost = urllib.request.Request(url=url, data=dataPost)
responsePost = urllib.request.urlopen(reqPost)
response2 = responsePost.read().decode("UTF-8")
print(response2)
