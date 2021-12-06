# -*- coding: UTF-8 -*-
# @Time: 2021/1/12 23:23
# @File: 同时进行修改和播放音乐.py

import pygame
import win32api
import win32con
import win32gui
import time
import threading

def playMp3(path):
    pygame.mixer.init()  #初始化
    pygame.mixer.music.load(path)   #加载音乐
    pygame.mixer.music.play()  #开始播放
    time.sleep(60)
    pygame.mixer.music.stop()

def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)  #打开注册表
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"0")  #设置背景的排列
    #win32api.RegSetValueEx(reg_key,"WallPaper")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)

th=threading.Thread(target=playMp3(r"E:\cui\C_TEST\test_cases\读取各类文件\Last_Stop.mp3"),name="playMp3")
th.start()

path=r"E:\cui\C_TEST\test_cases\读取各类文件\f75f718f88eb6790542b3848634f06c5.jpeg"
setWallPaper(path)