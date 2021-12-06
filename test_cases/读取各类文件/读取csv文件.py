# -*- coding: UTF-8 -*-
# @Time: 2021/1/11 22:19
# @File: 读取csv文件.py

import csv

def readCSV(path):
    listCSV=[]
    with open(path,"r") as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            listCSV.append(row)
    return listCSV


def writeCSV(path2, data):
    with open(path2,"a",newline='') as file:
        csv_writer=csv.writer(file)
        #csv_writer.writerow([])
        for rowData in data:
            csv_writer.writerow(rowData)

path=r"E:\cui\C_TEST\test_cases\读取各类文件\csv.csv"
listCSV=readCSV(path)
writeCSV(path,[[3,3,3],[4,4,4]])
listCSV2=readCSV(path)
print(listCSV,listCSV2)
