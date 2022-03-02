from functools import partial


"""
函数在执行时，要带上所有必要的参数进行调用。但是，有时参数可以在函数被调用之前提前获知。
这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
# 我们实现了一个取余函数，对于整数 100，取得对于不同数 m 的 100%m 的余数。
"""
def div(m, n):
    return m/n

div_by_100 = partial(div, m=100)
print(type(div_by_100))
