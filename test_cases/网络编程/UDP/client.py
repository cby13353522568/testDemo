# -*- coding: UTF-8 -*-
# @Time: 2021/2/1 23:10
# @File: client.py

import socket

UDPClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
    data = input("请输入：")
    UDPClient.sendto(data.encode("utf-8"), ("192.168.2.6", 8080))
    info = UDPClient.recv(1024).decode("utf-8")
    print(info)