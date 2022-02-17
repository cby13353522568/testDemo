# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 21:50
# @File: 7 线程事件.py

import threading,time
# 多线程下载


def run(e):
    e.wait()  # 阻塞，需要触发事件
    time.sleep(2)
    print("开始下载")
    e.clear()  # 重置阻塞


def func():
    event = threading.Event()
    t = threading.Thread(target=run, args=(event,))
    t.start()
    return event


if __name__ == "__main__":
    print("任务已添加")
    e = func()
    e.set()  # 触发事件

