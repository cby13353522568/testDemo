# -*- coding: UTF-8 -*-
# @Time: 2021/2/10 21:16
# @File: mysql调用.py
from .executeSql import ExecuteSql


s = ExecuteSql("localhost","root","123456","c_test")
str = s.execute("select version()")
str2 = s.execute("INSERT INTO EMPLOYEE(ID,FIRST_NAME,AGE, CREATE_TIME, gender) VALUES (5, 'd', 20, '2000-12-01',1)")
print(str2)

