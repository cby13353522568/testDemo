# -*- coding: UTF-8 -*-
# @Time: 2021/1/30 16:29
# @File: sendHttps.py
import urllib.request
import json
import ssl
url = "http://www.baidu.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}
#context = ssl._create_unverified_context()
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
jsonStr = response.read().decode("UTF-8")
jsonData = json.loads(jsonStr, strict=False)
print(jsonData)




