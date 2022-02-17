# -*- coding: UTF-8 -*-
# @Time: 2020/12/15 20:54
# @File: 2 迭代器生成器.py

# 迭代器和生成器  用于循环访问数据量比较大的集合，不用把所有数据读取到内存，节省内存空间，提高访问速度
List = [1, 2, 3, 4]
it = iter(List)  # 创建迭代器对象
# print(it)
print(next(it), '*****')  # 读取迭代器的元素
for n in it:
    print(n)


# 生成器  带有yield的函数，称为生成器。主要为了节省内存
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield,相当于return。（首次进来直接return 一个迭代器对象，第二次调用从yield下一步开始。第三次调用又return）
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(20):  # for循环自动调用next()，读取迭代器元素
    print(n,end=',')
