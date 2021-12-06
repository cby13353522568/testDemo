# -*- coding: UTF-8 -*-
# @Time: 2020/12/12 22:20
# @File: base_5.py

#字符串常用方法
str="hello,world!"
# 将字符串的第一个字符转换为大写
print(str.capitalize())
# 居中并填充其他位置（默认空格）
print(str.center(40,'*'))
print(str.ljust(40,'%'))
print(str.rjust(40,'%'))
# 统计字符串中子串出现的次数  str.count(sub, start= 0,end=len(string))
print(str.count('or', 0, len(str)))
# 检查字符串是否已obj结尾
print(str.endswith('d',0,len(str)))
print(str.endswith('d'))
print(str.startswith('h'))
# 检测 subStr 是否包含在字符串中，如果包含返回开始的索引值，否则返回-1
print(str.find('a',0,len(str)))
print(str.find('o',0,len(str)))
print(str.rfind('o',0,len(str)))  #从右开始
# 输入校验
print(str.isalnum()) #如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
print(str.isalpha()) #如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
print(str.isdigit()) #如果字符串只包含数字则返回 True 否则返回 False
# 指定分隔符，拼接字符串
print("-".join(str))
# 分割字符串
print(str.split('o'))   #返回分割后的字符串列表
# 截掉字符串左边的空格或指定字符。
str1="---hello,world---"
print(str1)
print(str1.lstrip('-'))
print(str1.rstrip('-'))
print(str1.strip("-"))
# 字符串替换
print(str.replace("o","a",1))   # 1是替换的次数