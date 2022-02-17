from datetime import datetime
import time
from threading import Timer


def timedTask():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    Timer(10, timedTask, ()).start()
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
