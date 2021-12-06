# -*- coding: UTF-8 -*-
# @Time: 2021/2/7 18:42
# @File: 全局变量在多个进程中不能共享.py

from multiprocessing import Process
from time import sleep

num = 100  # 全局变量


def run():
    print("子进程开始")
    global num
    num += 1
    print("子进程中的num：", num)
    print("子进程结束")


if __name__ == "__main__":
    print("主进程开始")
    p = Process(target=run)
    p.start()
    p.join()
    print("全局变量的num", num)
    print("主进程结束")