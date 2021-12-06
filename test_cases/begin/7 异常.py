# -*- coding: UTF-8 -*-
# @Time: 2020/12/17 20:56
# @File: 7 异常.py

# 错误和异常
# 语法错误，SyntaxError: invalid syntax （if后面没跟:等的问题）
# 异常 try-expect-else-finally
try:
    print(10/0)
except (ZeroDivisionError,NameError) as err0:    #一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
    #print("除数不能为0")
    #pass
    print("err0: {}".format(err0))   # 忽略异常的名称，它将被当作通配符使用
except TypeError:
    print(1)
else:     #try字句未发生异常时执行
    print("没有异常")
finally:     #不管是否发生异常最后都会走
    print("异常被catch")

# raise 抛出异常
'''if True:
    #raise TypeError
    raise Exception("死循环！")'''
# 如果只想知道是否抛出异常，并不想处理，可以直接用raise再次抛出
'''try:
    raise NameError
except NameError:
    print("检查是否有error，不处理")
    raise'''

# 断言 判断表达式，false的时候 触发异常
#assert 5>10   #相当于if not 5>10: raise AssertionError
