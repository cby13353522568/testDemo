from datetime import datetime
import sched
import time


def timedTask():
    # 初始化 sched 模块的 scheduler 类
    scheduler = sched.scheduler(time.time, time.sleep)
    # 增加调度任务 enter(delay, priority, action, argument=(), kwargs={})
    # delay 表示延迟多长时间执行任务，单位是秒。priority为优先级，越小优先级越大。两个任务指定相同的延迟时间，优先级大的任务会向被执行。action 即需要执行的函数
    scheduler.enter(10, 1, task)
    # 运行任务
    scheduler.run()


# 定时任务
def task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    timedTask()