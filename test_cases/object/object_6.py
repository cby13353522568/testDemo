# -*- coding: UTF-8 -*-
# @Time: 2020/12/24 22:34
# @File: object_6.py

#获取列表最小值
'''list=[1,2,3,4]
print(min(list))

#移除str指定元素
str="abcd"
new_str=""
for i in range(0,len(str)):
    if str[i]!='b':
        new_str+=str[i]
print(new_str)

#字典按照key排序
dict={2:"b",1:"c",3:"y"}
keys=list(dict.keys())
keys.sort()
for key in keys:
    print(key,dict[key])

#字典按照value排序
dict={2:"b",1:"c",3:"y"}
values=list(dict.values())
keys=list(dict.keys())
values.sort()
for value in values:
    print(keys[values.index(value)],value)  #index 方法返回元素在list中的索引
'''

#冒泡
a=[3,2,5,7,1,4]
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    print(a)
