# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 11:19
# @File: 多线程.py

import threading


def run(str):
    print("子线程{}开始".format(threading.current_thread().name))
    print(str)
    print("子线程{}结束".format(threading.current_thread().name))


if __name__ == "__main__":
    print("主线程{}开始".format(threading.current_thread().name))
    th = threading.Thread(target=run, args=("c",), name="Thread-c")
    th.start()
    th.join()

    print("主线程{}结束".format(threading.current_thread().name))