# -*- coding: UTF-8 -*-
# @Time: 2020/12/9 20:50
# @File: base_3.py

# Tuple元组
a,b,c,d=1,2.0,"OK",[1,2]
tuple=(a,b,c)  #元组的元素不能修改
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(type(tuple))

# Set集合   两种创建方式
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites={a,b,c,c}  #重复元素自动去掉
var1=set("abcd")
var2=set("cdef")
print(sites,var1,var2)
print(var1 - var2) #差集
print(var1.difference(var2))
print(var1 | var2) #并集
print(var1.union(var2))
print(var1 & var2) #交集
print(var1.intersection(var2))
print(var1 ^ var2) #不同时存在的元素集
print(var1.symmetric_difference(var2))

#成员测试
if a in var1:
    print("在集合中")
else:
    print("不在集合中")

# Dictionary字典
# 列表是有序的对象集合，字典是无序的对象集合
student1={'name':'张三','age':10,'sex':'male'}
student1['class']='5'
student2=dict(name='李四',age=11)
student3=dict([('name','王五'),('age',12)])
print(student1,student2.keys(),student3.values())
student1.clear()
print(student1)

#字符转换
print(int(b),float(a),str(d),eval('a+b')) #eval() arg 1 must be a string, bytes or code object




