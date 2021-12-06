# -*- coding: UTF-8 -*-
# @Time: 2020/12/27 10:47
# @File: dataType.py
'''
#字符串
print("字符串增".center(30,"-"))
str='abcd'
str1='e'
print("1.+号拼接字符串：",str+str1)
print("2.join方法拼接字符串",''.join([str,str1])) #join 方法中传递的参数需要是可迭代的,每个字符后面都加  abcde
print("字符串删".center(30,"-"))
print("1.strip方法删除开头和结尾的字符",str.strip('a'))  #注意只能删开头结尾   bcd 注意,都不是改变原来的字符串，需要新赋值
list=list(str)
list.pop(1)
str2=''.join(list)  #列表转换为字符串
print("2.转换成列表删除 ",type(str2),str2)
print("3.replace方法替换成空",str.replace('c',''))
print("字符串改".center(30,"-"))
print("1.replace方法替换",str.replace('c','3'))
print("字符串查".center(30,"-"))
print("1.find方法查询,未查到返回-1，查到返回索引",str.find("f"))
print("2.index方法查询,未查询到报异常",str.index("a"))

#列表
print("列表增".center(30,"-"))
list=[1,2,3,4]
list.append(5)
print("1.append方法",list)
list.extend([6,7])
print("2.extend方法",list)
print("列表删".center(30,"-"))
list.pop(4)  #下标
print("1.pop方法删除",list)
list.remove(7) #元素
print("2.remove方法删除",list)
print("列表改".center(30,"-"))
list[0]=0
print("1.列表下标元素替换",list)
print("列表查".center(30,"-"))
for i,v in enumerate(list):
    print(i,v)
#集合
print("集合增".center(30,"-"))
set={1,2,3,4}
set.add(5)
print("1.add方法",set)
set.update((5,6))
print("2.update方法",set)
print("集合删".center(30,"-"))
set.remove(6)
print("1.remove方法",set)
set.discard(4)
print("2.discard方法",set)
'''
#字典
print("字典增".center(30,"-"))
dict={'name':1,'age':2}
dict["sex"]=3
print("1.赋值新增",dict)
dict2={"home":4}
dict.update(dict2)
print("2.update方法",dict)
print("字典删".center(30,"-"))
dict.pop('home')
print("1.pop方法",dict)
del dict["sex"]
print("2.del方法",dict)
print("字典改".center(30,"-"))
dict["name"]='c'
print("替换",dict)
print("字典查".center(30,"-"))
print(list(dict.keys()),dict.values())
for k,v in dict.items():
    print(k,v)