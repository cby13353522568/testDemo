# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 19:08
# @File: 4 信号量控制线程数.py

import threading, time, datetime


def run():
    print("子线程{}start".format(threading.current_thread().name,))
    print(datetime.datetime.fromtimestamp(time.time()))
    time.sleep(1)
    print("子线程{}end".format(threading.current_thread().name, ))


if __name__ == "__main__":
    print("主线程begin")
    print(datetime.datetime.fromtimestamp(time.time()))
    t = threading.Timer(5, run)  # 5s后执行
    t.start()
    t.join()
    print("主线程end")



