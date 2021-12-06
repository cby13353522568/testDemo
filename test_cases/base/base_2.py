# -*- coding: UTF-8 -*-
# @Time: 2020/12/4 20:44
# @File: base_2.py

a, b, c = 1, 2, "runoob"   #同时赋值
print(a, b, c)

print(type(a))  #查询变量所指的对象类型
print(isinstance(c,int))

del(a)  #del语句删除一些对象引用
#print(a)  #NameError

print(2 / 4)  # 除法，得到一个浮点数
print(2 // 4) # 除法，得到一个整数
print(2 % 4)  # 混合计算时，Python会把整型转换成为浮点数

list=[b,c]
print(list)
list[0]=3
print(list)

