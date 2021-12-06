# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 22:20
# @File: 8 线程调度.py
import threading,time

# 线程1 打印0,2,4,6,8
# 线程2 打印1，3,5,7,9 调用线程打印 0,1,2 ..

cond = threading.Condition() # 线程条件变量

def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.notify()
            cond.wait()

if __name__ =="__main__":
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()