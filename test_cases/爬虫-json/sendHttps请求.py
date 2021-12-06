# -*- coding: UTF-8 -*-
# @Time: 2021/1/30 19:13
# @File: sendHttps请求.py
import urllib.request
import json
import ssl

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=80&limit=20"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
jsonData = json.loads(data)
print(jsonData)
