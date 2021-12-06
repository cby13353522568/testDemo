# -*- coding: UTF-8 -*-
# @Time: 2021/1/6 21:11
# @File: infoFrame.py
import tkinter
from tkinter import ttk
import os

class InfoFrame(tkinter.Frame):
    def __init__(self,parent):
        frame = tkinter.Frame(parent)
        frame.grid(row=0,column=1)

        self.fileName = tkinter.Variable()
        self.entry=tkinter.Entry(frame,textvariable=self.fileName)
        self.entry.pack()

        self.txt=tkinter.Text(frame)
        self.txt.pack()

