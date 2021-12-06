# -*- coding = UTF-8 -*-
# @Time = 2021/5/6 20:46
# @File = server.py
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options    # 全局参数的定义，存储，转换
import config

# 定义全局参数
'''
tornado.options.define(
    name = "port",   # 参数名，保证唯一性
    default = 8000,  # 默认为None
    type = int,     # 设置变量类型，从命令行或配置文件导入参数时，tornado会根据类型转换输入的值。
    help = "设置端口号",
    multiple = False,   # 设置变量是否可以为多个值
)
tornado.options.define(name="list",default=[],multiple=True)
'''

class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello tornado")

if __name__ == '__main__':
    # 转换命令行参数， 并保存到tornado.options.options ， 启动命令行 python server03.py --port=9000 --list=good,nice
    #tornado.options.parse_command_line()

    # 从配置文件导入参数, 不支持字典
    # tornado.options.options.logging = None  # 关闭日志
    #tornado.options.parse_config_file("config")
    #port = tornado.options.options.port
    #print(tornado.options.options.list, tornado.options.options.port)

    # config.py 设置参数, 一般用这个，不需要参数定义
    port = config.options["port"]
    print(config.options["port"],config.options["list"])

    app = tornado.web.Application([
        (r"/" , indexHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(port = port)  # 全局参数使用，所有定义的变量均作为options对象的属性

    # 多进程启动， httpServer.start(1)相当于httpServer.listen(8000)
    #httpServer.bind(8000)
    #httpServer.start(5)

    tornado.ioloop.IOLoop.current().start()


