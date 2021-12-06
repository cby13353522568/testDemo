# -*- coding: UTF-8 -*-
# @Time: 2021/1/25 19:07
# @File: readWord.py

import win32com
import win32com.client

def readWord(path):
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.open(path)
    for paragraph in doc.paragraphs:
        line = paragraph.Range.Text
        print(line)
    doc.Close()
    word.Quit()


path=r"E:\cui\C_TEST\test_cases\办公文件读取\待办.doc"
readWord(path)