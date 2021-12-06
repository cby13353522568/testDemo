# -*- coding: UTF-8 -*-
# @Time: 2021/2/8 11:22
# @File: runProcess.py

from cProcess import CProcess

if __name__ == "__main__":
    print("父进程开始")
    p = CProcess("testc.py")
    p.start()   # 自动调用p进程对象的run方法
    p.join()
    print("父进程结束")


