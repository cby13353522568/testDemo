# -*- coding: UTF-8 -*-
# @Time: 2021/1/5 23:04
# @File: treeFile.py
import tkinter
from tkinter import ttk
from treeFrame import TreeFrame
from infoFrame import InfoFrame


win = tkinter.Tk()
win.title("目录展示")
win.geometry("600x600+200+20")


path = "E:\\cui"
infoFrame=InfoFrame(win)
treeFrame=TreeFrame(win,path,infoFrame)


win.mainloop()

