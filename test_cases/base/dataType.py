# -*- coding: UTF-8 -*-
# @Time: 2020/12/27 10:47
# @File: dataType.py

# 字符串
str = 'abcd'
str1 = 'e'
print("1.+号拼接字符串：", str + str1)
print("2.join方法拼接字符串", ''.join([str, str1]))  # join 方法中传递的参数需要是可迭代的,每个字符后面都加  abcde

list1 = list(str)
list1.pop(1)  # 删除str中下标为1的
str2 = ''.join(list1)  # 列表转换为字符串
print("转换成列表删除 ", type(str2), str2)
print("replace方法替换成空", str.replace('c', ''))

print("replace方法替换", str.replace('c', '3'))

print("1.find方法查询,未查到返回-1，查到返回索引", str.find("f"))
print("2.index方法查询,未查询到报异常", str.index("a"))

# 列表
list2 = [1, 2, 3, 4]
list2.append(5)
print("1.append方法", list2)
list2.extend([6, 7])
print("2.extend方法", list2)
list2.insert(0,0)
print("3.insert方法", list2)

list2.pop(4)  # 下标
print("1.pop方法删除下标元素", list2)
list2.remove(7)  # 元素
print("2.remove方法删除具体元素", list2)

list2[0] = 0
print("1.列表下标元素替换", list2)

for i, v in enumerate(list2):
    print(i, v)

# 集合
set1 = {1, 2, 3, 4}
set1.add(5)
print("1.add方法", set1)
set1.update((5, 6))
print("2.update方法", set1)

set1.remove(6)  # 删除的值如果不存在，那么程序便会报KeyError错
print("1.remove方法", set1)
set1.discard(4)  #  discard 删除原先不存在的值，集合不发生变化而且也不会报错
print("2.discard方法", set1)

# 字典
dict = {'name': 1, 'age': 2}
dict["sex"] = 3
print("1.赋值新增", dict)
dict2 = {"home": 4}
dict.update(dict2)
print("2.update方法", dict)

dict.pop('home')  # 删除key
print("1.pop方法", dict)
del dict["sex"]
print("2.del方法", dict)

dict["name"] = 'c'
print("替换", dict)

print(list(dict.keys()), dict.values())
for k, v in dict.items():
    print(k, v)
