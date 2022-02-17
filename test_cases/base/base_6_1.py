# -*- coding: UTF-8 -*-
# @Time: 2020/12/13 22:49
# @File: base_6_1.py

# 集合常用方法
set = {'a', 'b', 'c'}

# 新增元素
set.add('d')
print(set)
set.update((1, 2))  # update方法的参数可以为seq
print(set)

# 移除元素
set.remove(1)  # key不存在报错，keyError
print(set)
set.discard(2)  # key不存在不会报错
print(set)
print(set.pop())  # 随机删一个元素
print(set)

# 判断是否有相同元素
set1 = {1, 2, 3}
set2 = {2, 3}
print(set1.isdisjoint(set2))  # 没有相同元素返回True

# 判断是否是子集
print(set1.issubset(set2))  # set1是否是set2的子集
print(set1 >= set2)  # set1是否是set2的子集
print(set1.issuperset(set2))  # set2是否是set1的子集
