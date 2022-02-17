# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 16:41
# @File: 2 线程锁解决数据共享.py


import threading
num = 0
lock = threading.Lock()  # 创建锁对象
# eg:同时操作一个账户时

def run(n):
    global num
    for i in range(10000000):
        '''
        lock.acquire()
        try:    # 确认代码块只有一个线程在执行，阻止多线程并行
            num = num + n
            num = num - n
        finally:
            lock.release()   # 避免死锁
        '''
        with lock:  # 自动上锁解锁，降低死锁风险
            num = num + n
            num = num - n



if __name__ == "__main__":
    print("主进程begin")
    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=run, args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
    print("主进程end")

