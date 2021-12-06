# -*- coding: UTF-8 -*-
# @Time: 2020/12/10 22:25
# @File: base_4.py
import math  #Number 常用函数
import random

print(math.ceil(5.1))   #向上取整 6
print(math.floor(4.9))       #向下取整 4
print(max(1,2,3))
print(min([1,2,3],[2,3,4]))
print(round(2.675,2))   #四舍五入，2表示保留两位小数

# 随机数
print(random.random())   #[0,1)的实数
print(random.randint(1,10))   # 随机整数
print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))    #random.choice(seq)  --seq可以是一个列表，元组或字符串
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))
list=[1,2,3,4]   #random.shuffle(list)  --list为列表，无返回值
random.shuffle(list)

print(list)
print ("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))  #随机生成下一个实数，它在 [x,y] 范围内

#字符串格式化
name="cby"
print("%s你好，%.2f" %(name,1000))
print("{1}{0}{1}".format("c","b"))
print(f"hello,{name}") #python3.6

