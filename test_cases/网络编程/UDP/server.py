# -*- coding: UTF-8 -*-
# @Time: 2021/2/1 23:07
# @File: server.py


# 不需要连接，只需要有ip和端口号，但是不保证是否可以接收到数据。多用于 广播
import socket

UDPServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServer.bind(("192.168.2.6", 8080))

while True:
    data, addr = UDPServer.recvfrom(1024)
    print("客户端：",data.decode("utf-8"))
    info = input("请输入返回：")
    UDPServer.sendto(info.encode("utf-8"),addr)