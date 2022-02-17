"""
移除 job 也有两种方法：remove_job() 和 job.remove()。
remove_job() 是根据 job 的 id 来移除，所以要在 job 创建的时候指定一个 id。
job.remove() 则是对 job 执行 remove 方法即可

scheduler.add_job(job_func, 'interval', minutes=2, id='job_one')
scheduler.remove_job(job_one)

job = add_job(job_func, 'interval', minutes=2, id='job_one')
job.remvoe()
"""

'''
修改 job
如果你因计划改变要对 job 进行修改，可以使用Job.modify() 或者 modify_job()方法来修改 job 的属性。但是值得注意的是，job 的 id 是无法被修改的。
scheduler.add_job(job_func, 'interval', minutes=2, id='job_one')
scheduler.start()
# 将触发时间间隔修改成 5分钟
scheduler.modify_job('job_one', minutes=5)

job = scheduler.add_job(job_func, 'interval', minutes=2)
# 将触发时间间隔修改成 5分钟
job.modify(minutes=5)
'''

'''
默认情况下调度器会等待所有正在运行的作业完成后，关闭所有的调度器和作业存储。如果你不想等待，可以将 wait 选项设置为 False。
scheduler.shutdown()
scheduler.shutdown(wait=false)
'''