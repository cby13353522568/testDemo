# -*- coding: UTF-8 -*-
# @Time: 2020/12/14 21:42
# @File: 1 循环.py
import random

# 斐波那契数列
a, b = 0, 1
list = [a, b]
for i in range(10):
    list.append(list[i] + list[i + 1])
print(list)

# 条件控制
# x 为 0-99 取一个数，y 为 0-199 取一个数,如果 x>y 则输出 x，如果 x < y 则输出 x+y，否则输出y。 直到x=y，算出用了多少次
n = 0
while True:
    x = random.choice(range(0, 99))  # range(len(List)) 常用
    y = random.choice(range(0, 199))
    n += 1
    if (x > y):
        print("X>Y:", x, ">", y)
    elif (x < y):
        print("Y>X:", x, "<", y)
    else:
        print("相等数值：", x, "次数：", n)
        break

# 循环 python没有switch-case
'''
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
'''
# for 主要用来遍历
'''
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

#
for n in range(2, 10):  # range相当于[2,10)
    for x in range(2, n):
        print(n, x)
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
# 1、如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
# 2、如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行！

# pass语句块防止语法错误
if 3 > 2:
    pass
