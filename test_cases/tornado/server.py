# -*- coding: UTF-8 -*-
# @Time: 2021/5/6 20:46
# @File: server.py
import tornado.web  # 基础web模块
import tornado.ioloop   # 封装linux的epoll 和BSD的kqueue,是tornado高效的基础

# 业务逻辑处理类，给浏览器相应信息
class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello tornado")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/" , indexHandler)
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()


