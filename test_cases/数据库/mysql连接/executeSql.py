# -*- coding: UTF-8 -*-
# @Time: 2021/2/10 21:06
# @File: executeSql.py
import pymysql


class ExecuteSql():
    def __init__(self,net,user,password,dbName):
        self.net = net
        self.user = user
        self. password = password
        self.dbName = dbName

    def connect(self):
        self.db = pymysql.Connect(self.net,self.user,self.password,self.dbName)
        self.cursor = self.db.cursor()
        print("数据库{}已连接".format(self.dbName))

    def close(self):
        self.db.close()

    def execute(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.db.commit()
            dataList = self.cursor.fetchall()
            self.close()
            print("sql执行完毕")
            return dataList
        except:
            self.db.rollback()
            print("sql语句错误")






