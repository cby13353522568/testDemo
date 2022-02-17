import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler


def timedTask():
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

def job_func(text):
    print(text)

if __name__ == '__main__':
    # 创建后台执行的 schedulers
    #BlockingScheduler: 调度器在当前进程的主线程中运行，也就是会阻塞当前线程。
    # BackgroundScheduler: 调度器在后台线程中运行，不会阻塞当前线程。
    scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
    # 添加调度任务
    # 1. 触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler.add_job(timedTask, 'interval', seconds=2)
    # 2. date 触发器
    scheduler.add_job(job_func, 'date', run_date=datetime.datetime(2022, 2, 16, 20, 17, 0), args=['text'])
    # 3. cron 触发器
    '''
    year (int 或 str)	年，4位数字
    month (int 或 str)	月 (范围1-12)
    day (int 或 str)	日 (范围1-31
    week (int 或 str)	周 (范围1-53)
    day_of_week (int 或 str)	周内第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun)
    hour (int 或 str)	时 (范围0-23)
    minute (int 或 str)	分 (范围0-59)
    second (int 或 str)	秒 (范围0-59)
    start_date (datetime 或 str)	最早开始日期(包含)
    end_date (datetime 或 str)	最晚结束时间(包含)
    '''
    # # 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job_func 任务
    scheduler.add_job(job_func, 'cron', month='1-3,7-9', day='0, tue', hour='0-3')

    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(5)

