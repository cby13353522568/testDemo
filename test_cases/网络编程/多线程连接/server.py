# -*- coding: UTF-8 -*-
# @Time: 2021/2/1 22:18
# @File: server.py
import socket,threading


# 接受数据,1024为1k
def run(clientSocket, clientAddress):
    data = clientSocket.recv(1024)
    print("客户端信息："+data.decode("utf-8"))
    # sendToClient = input("输入发送给客户端的消息：")
    tName = threading.current_thread().name
    clientSocket.send(tName.encode("utf-8"))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP和端口
server.bind(("192.168.3.26", 8080))
# 监听
server.listen(5)
print("服务器启动成功")

while True:
    # 等待连接
    clientSocket, clientAddress = server.accept()
    th = threading.Thread(target=run, args=(clientSocket, clientAddress))
    print("{}{}连接成功".format(clientSocket, clientAddress))
    th.start()





