# -*- coding: UTF-8 -*-
# @Time: 2020/12/28 22:20
# @File: tpymysql.py

import pymysql
import cryptography

db = pymysql.Connect("localhost", "root", "123456", "c_test")  # 链接数据库
# db=pymysql.Connect("192.168.3.26","root","123456","c_test")  #链接数据库
cursor = db.cursor()  # 创建游标对象
cursor.execute("select version()")  # 执行sql语句
data = cursor.fetchone()  # fetchone()方法获取单条数据, fetchall()返回全部数据，列表类型
print("DB version:{}".format(data[0]))

name = 'd'
insert = "INSERT INTO EMPLOYEE(ID,FIRST_NAME,\
         AGE, CREATE_TIME, gender) \
         VALUES (4, 'd', 20, '2000-12-01',1)"
# \ 换行，如果不需要用变量可以使用""" """
try:
    cursor.execute(insert)
    db.commit()
except:
    db.rollback()
    print("sql语句错误")

db.close()
