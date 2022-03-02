# -*- coding: UTF-8 -*-
# @Time: 2020/12/19 9:27
# @File: 1 定义类.py
import builtins


class People:
    """一个简单的类实例"""
    name = ""
    __age = 28  # 私有属性,私有属性在类外部无法直接进行访问

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self, name, __age):  # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称
        print(name, __age)
        return 'hello world'

    def __hello(self):
        return ("私有方法")


# 实例化类
x = People("cby", 10)
# 访问类的属性和方法
print("People 类的属性 name 为：", x.name)
print("People 类的方法 hello 输出为：", x.hello("cby", 10))
# print(x.__age)
# print(x.__hello())

# 命名空间和作用域
# Python 的查找顺序为：局部的命名空间（函数中定义的名称） -> 全局命名空间（模块中定义的名称） -> 内置命名空间（python 语言内置的名称）
print(dir(builtins))  # 可以查看预定义了哪些变量
print(dir(People))
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了

"""
继承
super(子类，self).__init__(参数1，参数2，....)
父类名称.__init__(self,参数1，参数2，...)
"""
