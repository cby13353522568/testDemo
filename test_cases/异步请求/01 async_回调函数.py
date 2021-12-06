# -*- coding: UTF-8 -*-
# @Time: 2021/6/1 19:12
# @File: 01 async_回调函数.py
import threading
import time

def longIO(callback):
    def run(cb):
        print("耗时操作开始")
        time.sleep(5)
        print("耗时操作结束")
        cb("异步返回数据")
    threading.Thread(target=run,args=(callback,)).start()

# 回调函数,可以类比ajax 当耗时操作又返回时
def finish(data):
    print("回调开始")
    print("回调接受数据",data)
    print("回调结束")


def reqA():
    print("请求A开始")
    longIO(finish)
    print("请求A结束")

def reqB():
    print("请求B开始")
    print("请求B结束")

def main():
    reqA()
    reqB()

if __name__ == "__main__":
    main()