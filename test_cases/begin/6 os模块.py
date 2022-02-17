# -*- coding: UTF-8 -*-
# @Time: 2020/12/17 20:08
# @File: 6 os模块.py

# os os 模块提供了非常丰富的方法用来处理文件和目录
import os

# 检测是否有访问权限的路径 os.access(path,mode)  mode: os.R_OK 是否可读 os.F_OK 是否存在 os.W_OK 是否可写 os.X_OK 是否可执行
print(os.access("file.txt", os.R_OK))

# 返回当前工作目录
print(os.getcwd())

# 返回path指定的文件夹包含的文件或文件夹的名字的列表
print(os.listdir("E:\cui\C_TEST"))

# 创建文件夹 如果已存在，报os错误
path = "/test_cases/testc.py"
# os.mkdir(path,777)

# 删除目录
# os.rmdir(path)
# os.removedirs(path)  --递归删除目录

# 删除文件  如果path是目录，报os错误
path2 = "file2.txt"
# os.remove(path2)

# 返回文件属性信息
print(os.path.exists(path2))

# 拼接目录
BASE_DIR = r"E:\cui\tools"
print(os.path.join(BASE_DIR, 'templates'))
