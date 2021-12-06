# -*- coding: UTF-8 -*-
# @Time: 2021/1/12 22:05
# @File: 修改背景图片.py

import win32api
import win32con
import win32gui

def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)  #打开注册表
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"6")  #设置背景的排列
    #win32api.RegSetValueEx(reg_key,"WallPaper")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)

path=r"E:\cui\C_TEST\test_cases\读取各类文件\f75f718f88eb6790542b3848634f06c5.jpeg"
setWallPaper(path)