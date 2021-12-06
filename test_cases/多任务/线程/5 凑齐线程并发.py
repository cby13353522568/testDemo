# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 19:08
# @File: 4 信号量控制线程数.py

import threading, time
bar = threading.Barrier(2)  # 凑够几个线程一起执行


def run():
    print("子线程{}start".format(threading.current_thread().name,))

    bar.wait()   # 凑够2个线程后才执行下面的end
    time.sleep(2)
    print("子线程{}end".format(threading.current_thread().name, ))



if __name__ == "__main__":
    print("主线程begin")
    for i in range(5):
        th = threading.Thread(target=run)
        th.start()


