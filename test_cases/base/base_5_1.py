# -*- coding: UTF-8 -*-
# @Time: 2020/12/12 23:42
# @File: base_5_1.py

# 列表常用方法
list = [1, 2, 3, 4, 4]
list.append('5')  # 在列表末尾添加新的对象
print(list)
# 某个元素在列表中出现的次数
print(list.count(4))
# 在列表末尾一次性追加另一个序列中的多个值
list1 = (2, 3)
list.extend(list1)
print(list)
# 从列表中找出某个值第一个匹配项的索引位置
print(list.index(4, 0, len(list)))
# 将指定对象插入列表的指定位置。
list.insert(0, 0)
print(list)
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list.pop(5))
print(list)
# 移除列表中某个值的第一个匹配项
list.remove('5')
print(list)
# 反向列表中元素
list.reverse()
print(list)
# 列表排序
list.sort(reverse=False)  # 临时排序sorted()方法，没有改变元素的原始存储位置，只是用于排序输出
print(list)
list2 = list.copy()
print("list2:", list2)  # 注意拼接用的逗号，而不是+
list2.clear()
print(list2)
