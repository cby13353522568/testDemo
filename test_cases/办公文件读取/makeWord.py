# -*- coding: UTF-8 -*-
# @Time: 2021/1/25 20:53
# @File: makeWord.py

import win32com
import win32com.client
import os


def makeWord(path, name, content):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True
    doc = word.Documents.Add()
    r = doc.Range(0, 0)
    r.InsertAfter(path + str(name))
    r.InsertAfter(content)
    doc.SaveAs(path)
    doc.Close()
    word.Quit()


names = [1, 2]
content = "你好"
for name in names:
    path = os.path.join(os.getcwd(), str(name))
    print(path, name, content)
    makeWord(path, name, content)
