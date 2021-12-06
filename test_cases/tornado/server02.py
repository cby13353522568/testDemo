# -*- coding: UTF-8 -*-
# @Time: 2021/5/6 20:46
# @File: server.py
import tornado.web
import tornado.ioloop
import tornado.httpserver

class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello tornado")

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/" , indexHandler)
    ])

    # 手动实例化http服务器对象,相当于app.listen(8000).不需要手动启动服务器（区别于django runserver）
    httpServer = tornado.httpserver.HTTPServer(app)  # 告诉服务器要识别的路由
    httpServer.listen(8000)


    tornado.ioloop.IOLoop.current().start()


