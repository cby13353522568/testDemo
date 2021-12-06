# -*- coding: UTF-8 -*-
# @Time: 2021/1/12 23:32
# @File: 键盘模拟.py

import win32api
import win32con
import time


win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_EXTENDEDKEY,0)  #按下回车
#time.sleep(0.1)
win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)  #抬起