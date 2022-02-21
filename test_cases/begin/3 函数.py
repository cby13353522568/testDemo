# -*- coding: UTF-8 -*-
# @Time: 2020/12/15 21:31
# @File: 3 函数.py

# 函数
def hello(name):
    print("hello", name)


x = "cby"
hello(x)  # 第一种参数类型：必需参数，不传会报错

# 匿名函数 lambda
niming = lambda var1, var2: var1 + var2
print(niming(1, 2))

# 2.关键字参数 ,不需要按照指定顺序传
hello(name='cby')


# 3.默认参数
def hello2(name="ccc"):
    print("hello", name)

hello2()


# 4.不定长参数，不知道要传多少个参数
def hello3(var1, *varTuple):  # varTuple 会以元组形式导入
    print(var1)
    for i in varTuple:
        print(i)

hello3("a", "b", "c")


def hello4(var1, **varDict):  # varDict 会以字典形式导入
    print(var1, varDict)


hello4(1, name="ccc", age=10, sex=3)

# 列表推导式
vec = [2, 4, 6]
x = [3 * x for x in vec if x > 2]
print(x)

dict = {x: x ** 2 for x in vec}
print(dict)


class Cat:
    def __str__(self):   # 打印对象时会展示对象的介绍信息
        print("对象介绍")
    def drink(self):
        print("1")
cat = Cat()
print(cat)
