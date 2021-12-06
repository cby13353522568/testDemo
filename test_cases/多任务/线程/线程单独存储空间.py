# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 17:16
# @File: 线程单独存储空间.py
# 作用：为每个线程绑定数据库，http请求，用户身份信息等

import threading

local = threading.local()
num = 0

def run(x,n):
    x = x + n
    x = x - n

def func(n):
    # 每个线程local.x 都不同。
    local.x = num
    for i in range(1000000):
        run(local.x, n)

if __name__ == "__main__":
    print("主进程begin")
    t1 = threading.Thread(target=func, args=(1,))
    t2 = threading.Thread(target=func, args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
    print("主进程end")