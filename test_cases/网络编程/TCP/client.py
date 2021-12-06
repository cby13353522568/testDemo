# -*- coding: UTF-8 -*-
# @Time: 2021/1/31 22:46
# @File: client.py

import socket

# AF_INET 协议IPV4  SOCK_STREAM TCP协议
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接 参数为元组
client.connect(("192.168.2.6", 8080))
# 网络传输不能直接传字符串
while True:
    data = input("输入发送给服务器的消息：")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器应答：" + info.decode("utf-8"))


