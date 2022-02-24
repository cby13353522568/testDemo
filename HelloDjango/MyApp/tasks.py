from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(10)
    print("异步处理")
    return x + y


def report():
    return "报告"
