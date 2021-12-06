# -*- coding: UTF-8 -*-
# @Time: 2021/1/12 21:42
# @File: 读取音乐文件.py

import pygame
import time


def playMp3(path):
    pygame.mixer.init()  #初始化
    pygame.mixer.music.load(path)   #加载音乐
    pygame.mixer.music.play()  #开始播放
    time.sleep(60)
    pygame.mixer.music.stop()



file = r"E:\\cui\\C_TEST\\test_cases\\读取各类文件\\Last_Stop.mp3"
playMp3(file)

