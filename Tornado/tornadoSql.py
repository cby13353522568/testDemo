# -*- coding: UTF-8 -*-
# @Time: 2021/5/21 11:30
# @File: tornadoSql.py
import pymysql
import config

class TornadoSql():
    def __init__(self,host,user,password,dbName):
        self.host = host
        self.user = user
        self.password = password
        self.dbName = dbName

    def DBconnect(self):
        self.db = pymysql.Connect(self.host,self.user,self.password,self.dbName)
        self.cursor = self.db.cursor()
        print("数据库已连接")

    def DBclose(self):
        self.cursor.close()
        self.db.close()

    def DBexecute(self,sql):
        try:
            self.DBconnect()
            self.cursor.execute(sql)
            self.db.commit()
            dataList = self.cursor.fetchall()
            return dataList
        except:
            self.db.rollback()
            print("sql错误")
        finally:
            #self.DBclose()
            pass

    def DBquery(self, sql, tableName,*args):
        dataList = self.DBexecute(sql)
        self.cursor.execute("select column_name from information_schema.columns where table_schema='{}' and table_name='{}'".format(self.dbName,tableName))
        column_names = []
        if len(args)>0:
            for column_name in args:
                column_names.append(column_name)

        else:
            column_all = self.cursor.fetchall()
            for column_name in column_all:
                column_names.append(column_name[0])
        print(column_names)
        raws = []
        for raw in dataList:
            datas = {}
            i = 0
            for data in raw:
                datas[column_names[i]] = data
                i += 1
                if i == len(raw):
                    break
            raws.append(datas)
        return raws





'''
if __name__ == "__main__":
    db = TornadoSql("localhost","root","123456","jd")
    dataList = db.DBquery("select * from jdapp_goods","jdapp_goods")
'''
