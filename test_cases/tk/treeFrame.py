# -*- coding: UTF-8 -*-
# @Time: 2021/1/5 23:31
# @File: treeFrame.py
import tkinter
from tkinter import ttk
import os

class TreeFrame(tkinter.Frame):
    def __init__(self,parent,path,infoFrame):
        frame = tkinter.Frame(parent)  #左侧frame显示目录树
        frame.grid(row=0,column=0)
        self.infoFrame=infoFrame

        self.tree=ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT,fill=tkinter.Y)
        #根目录
        root = self.tree.insert("","end",text=self.getLastpath(path),values=(path))
        print(root,path)
        #树结构--递归
        self.loadTree(root,path)
        #滚动条
        self.scroll=tkinter.Scrollbar(frame)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.scroll.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scroll.set)

        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self,event):
        self.click = event.widget.selection()   # 触发时间的小构件对象
        for clickable in self.click:
            file= self.tree.item(clickable)["text"]
            self.infoFrame.fileName.set(file)
            apath=self.tree.item(clickable)["values"]
            print(apath)


    def loadTree(self,parent,parentPath): #父节点，父节点的路径
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            treeNext=self.tree.insert(parent,"end",text=self.getLastpath(absPath),values=(absPath))
            if  os.path.isdir(absPath):
                self.loadTree(treeNext,absPath)




    def getLastpath(self,path):
        res=path.split("\\")
        return res[-1]



