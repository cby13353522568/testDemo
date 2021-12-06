# -*- coding: UTF-8 -*-
# @Time: 2021/5/18 10:13
# @File: server.py
from tornado import web, ioloop, httpserver, options
import config
from application import Application


if __name__ == "__main__":
    options = config.options
    settings = config.settings

    app = Application()

    app.listen(options["port"])

    ioloop.IOLoop.current().start()