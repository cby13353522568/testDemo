# -*- coding: UTF-8 -*-
# @Time: 2021/2/8 11:32
# @File: 多进程通信.py

from multiprocessing import Process, Queue
import random,time
# 进程间通信使用队列Queue


def write(q):
    print("写的子进程开始")
    chars = ["a","b","c"]
    for char in chars:
        q.put(char)
    time.sleep(1)
    print("写的子进程结束")


def read(q, str):
    print("读的子进程开始")
    print(str)
    while True:
        value = q.get(True)
        print("value", value)
    print("读的子进程结束")


if __name__ == "__main__":
    print("父进程开始")

    q = Queue()  # 创建队列
    p = Process(target=write,args=(q,))
    p2 = Process(target=read,args=(q, "读取write的字节"))

    p.start()
    p2.start()

    p.join()
    p2.terminate()  # 强制停止进程

    print("父进程结束")