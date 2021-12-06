# -*- coding: UTF-8 -*-
# @Time: 2020/12/15 22:47
# @File: 4 数组字典遍历.py

#遍历
dict={1:"a",2:"b"}       #字典遍历同时返回k,v
for k,v in dict.items():
    print(k,v)

list=["a","b","c"]
for i,v in enumerate(list):
    print(i,v)

list1=["name","age"]
list2=["aaa",10]
for basic,info in zip(list1,list2):
    print("what \'s you {0}? {1}".format(basic,info))
