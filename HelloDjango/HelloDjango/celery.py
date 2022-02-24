from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloDjango.settings')  # 设置django环境

app = Celery('HelloDjango')

app.config_from_object('django.conf:settings', namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks()  # 发现任务文件每个app下的task.py

from celery.schedules import crontab    # 定时任务  pip install django_celery_beat
# 启动定时任务  celery -A 你的应用 beat
from datetime import timedelta

app.conf.update(
    CELERYBEAT_SCHEDULE={'sum-task': {'task': 'MyApp.tasks.add', 'schedule': timedelta(seconds=20), 'args': (5, 6)},
                         'send-report': {'task': 'MyApp.tasks.report', 'schedule': crontab(hour=4, minute=30, day_of_week=1), }})
