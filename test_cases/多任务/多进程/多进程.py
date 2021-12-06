# -*- coding: UTF-8 -*-
# @Time: 2021/2/7 17:52
# @File: 多进程.py

from multiprocessing import Process
import time
import os


# 提供Process类来代表一个进程


def process1(str):
    while True:
        print("{}-{}，子进程的父进程-{}".format(str,os.getpid(),os.getppid()))
        time.sleep(1)


def process2():
    while True:
        print("主进程-{}".format(os.getpid()))
        time.sleep(2)


if __name__ == "__main__":
    p = Process(target=process1,args=("子进程",))  # args传元组
    p.start()
    process2()
