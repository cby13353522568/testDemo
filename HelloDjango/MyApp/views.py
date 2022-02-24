from django.shortcuts import render
from .models import User
from django.http import JsonResponse
import time
from MyApp import tasks

# Create your views here.


def showStudent(request):
    students = User.objects.all()
    res = tasks.add.delay(3, 5)  # 启动celery： celery -A HelloDjango worker -l info -P eventlet
    # res.get()
    return render(request, 'MyApp/Hello.html', {'students': students, 'task_id': res.task_id, 'task_result': res.result})
