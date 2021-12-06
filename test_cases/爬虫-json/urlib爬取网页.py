# -*- coding: UTF-8 -*-
# @Time: 2021/1/28 22:02
# @File: urlib爬取网页.py

import urllib.request
import urllib

response = urllib.request.urlopen("http://www.baidu.com")

'''
data = response.read()  #读取全部内容
with open(r"E:\cui\C_TEST\test_cases\爬虫-json\1.html","wb") as file:
    file.write(data)

data = response.readline()
data2 = response.readlines() #读取全部，但是读出来是list
'''
#response属性
print(response.info())  #当前环境信息
print(response.getcode())   #状态码
print(response.geturl())   #正在爬取的地址
url = r'https://v.sogou.com/v?query=%E6%96%97%E9%B1%BC&p=40230600&tab=video&ie=utf8&rawQuery=douyu'
print(urllib.request.unquote(url))   #解码unquote，编码quote

#爬取网页直接写入文件
urllib.request.urlretrieve("http://www.baidu.com",r"E:\cui\C_TEST\test_cases\爬虫-json\2.html")
#该方法会产生缓存
urllib.request.urlcleanup()