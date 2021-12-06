# -*- coding: UTF-8 -*-
# @Time: 2021/6/1 19:12
# @File: 01 async_回调函数.py
import threading
import time


#通过协程处理异步
def longIO():
    print("耗时操作开始")
    time.sleep(5)
    print("耗时操作结束")
    # 不要线程返回数据
    yield "longIO生成器返回数据"


def genCoroutine(f):
    def wrapper(*args,**kwargs):
        gen1 = f()   # reqA()的生成器
        gen2 = next(gen1)  # longIO的生成器
        def run(g):
            res = next(g)
            try:
                gen1.send(res)  # 返回reqA()的数据
            except StopIteration as e:
                pass
        threading.Thread(target=run,args=(gen2,)).start()
    return wrapper


@genCoroutine  # 自定义装饰器
def reqA():
    print("请求A开始")
    res = yield longIO()
    print("装饰器接受数据：",res)
    print("请求A结束")

def reqB():
    print("请求B开始")
    print("请求B结束")

def main():
    '''
    global gen
    gen = reqA()   # 生成器，使用了 yield 的函数被称为生成器
    next(gen)     # 调用生成器
    '''
    reqA()   # 给reqA()加装饰器来达到 上面三步的效果
    reqB()

if __name__ == "__main__":
    main()