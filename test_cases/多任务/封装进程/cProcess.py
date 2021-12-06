# -*- coding: UTF-8 -*-
# @Time: 2021/2/8 11:06
# @File: cProcess.py

from multiprocessing import Process
import os, time


class CProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程开始{}{}".format(self.name, os.getpid()))
        print("运行中")
        time.sleep(3)

        print("子进程结束{}{}".format(self.name, os.getpid()))
