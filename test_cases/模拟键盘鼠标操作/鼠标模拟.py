# -*- coding: UTF-8 -*-
# @Time: 2021/1/12 23:32
# @File: 鼠标模拟.py

import win32api
import win32con
import time

win32api.SetCursorPos([712, 83])

time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 110, 110, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 40, 40, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
