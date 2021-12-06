# -*- coding: UTF-8 -*-
# @Time: 2021/2/7 17:52
# @File: 父进程等待子进程.py

from multiprocessing import Process
import time
import os


def process1(str):
    print("{}-{}，子进程1的父进程-{}".format(str,os.getpid(),os.getppid()))
    time.sleep(5)
    print("子进程1结束")


def process2(str):
    print("{}-{}，子进程2的父进程-{}".format(str,os.getpid(),os.getppid()))
    time.sleep(2)
    print("子进程2结束")


if __name__ == "__main__":
    print("父进程开始")   # 父进程不做具体任务
    p1 = Process(target=process1,args=("子进程1",))  # args传元组
    p2 = Process(target=process2,args=("子进程2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()   # 等待子进程结束父进程才结束
    print("父进程结束")
