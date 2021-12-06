# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 19:08
# @File: 4 信号量控制线程数.py

import threading,time
sem = threading.Semaphore(3)   # 控制一次性有几个线程能执行


def run():
    with sem:
        print("子线程{}".format(threading.current_thread().name,))
        time.sleep(2)


if __name__ == "__main__":
    print("主线程begin")
    for i in range(5):
        th = threading.Thread(target=run)
        th.start()


    print("主线程end")
