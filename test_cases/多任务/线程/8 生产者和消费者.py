# -*- coding: UTF-8 -*-
# @Time: 2021/2/9 22:02
# @File: 8 生产者和消费者.py

import threading,queue,time,random


# 生产者
def product(i, q):
    while True:
        num = random.randint(1, 100000)
        q.put(num)
        print("生产者{}生产了数据{}".format(i, num))
        time.sleep(3)
    # 任务完成
    q.task_done()


# 消费者
def customer(i, q):
    while True:
        data = q.get()
        if data is None:
            break
        print("消费者{}消费了数据{}".format(i, data))
        time.sleep(2)
    q.task_done()



if __name__ =="__main__":
    # 消息队列
    q = queue.Queue()

    # 启动生成着
    for i in range(4):
        threading.Thread(target=product, args=(i,q)).start()

    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer,args=(i,q)).start()
