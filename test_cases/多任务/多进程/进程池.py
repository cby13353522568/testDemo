# -*- coding: UTF-8 -*-
# @Time: 2021/2/7 18:52
# @File: 进程池.py
from multiprocessing import Pool
import random,os,time


def run(i):
    print("子进程{}:{}".format(i,os.getpid()))
    time.sleep(random.choice([1,2,3]))
    print("子进程{}结束".format(i))


if __name__ == "__main__":
    print("父进程开始")
    # 创建进程池对象
    processPool = Pool(2)  # 默认大小为CPU核心数
    for i in range(5):
        # 创建进程，放到进程池管理
        processPool.apply_async(run, args=(i,))
    # 多进程执行
    #processPool.apply_async(run1)

    processPool.close()  # close后不能再添加进程
    processPool.join()

    print("父进程结束")