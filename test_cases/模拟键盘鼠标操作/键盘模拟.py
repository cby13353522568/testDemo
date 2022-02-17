# -*- coding: UTF-8 -*-
# @Time: 2021/1/12 23:32
# @File: 键盘模拟.py

import win32api

import win32con
import time

win32api.keybd_event(20, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # 按下CAPSlock
win32api.keybd_event(20, 0, win32con.KEYEVENTF_KEYUP, 0)  # 抬起


# win32api.keybd_event(18, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
# win32api.keybd_event(65, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
