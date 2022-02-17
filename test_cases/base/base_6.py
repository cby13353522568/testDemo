# -*- coding: UTF-8 -*-
# @Time: 2020/12/13 22:08
# @File: base_6.py

# 字典常用方法
dict = {'Name': 'Zara', 'Age': 7}
print("字典长度 : % d" % len(dict))
print(dict.keys(), list(dict.values()))  # 返回一个迭代器，可以使用 list() 来转换为列表

dict.clear()  # 清空字典
print(dict)

seq = [1, 2, 3]  # 创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
dict1 = dict.fromkeys(seq, 10)
print(dict1)

print(dict1[1])  # 如果key不存在，报错
print(dict1.get(4))  # 如果key不存在，返回None
print(dict1.setdefault(4, 4))  # 如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值
print(dict1)
print(4 in dict1)  # 判断键是否存在于字典中

dict2 = {5: 5}
dict1.update(dict2)  # 字典不能+，update更新
print(dict1)

print(dict1.pop(5))  # 删除字典给定键 key 所对应的值，返回值为被删除的值
print(dict1)
