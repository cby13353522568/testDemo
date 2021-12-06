from views import index
import tornado.web
import config,os
from tornadoSql import TornadoSql


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            #(r"/", index.IndexHandler),
            (r"/home", index.HomeHandler, {"name": "cby"}),  # 传参
            (r"/write", index.WriteHandler),
            (r"/json", index.JsonHandler),  # 返回响应头
            (r"/status", index.StatusHandler),  # 状态码
            (r"/redirect", index.RedirectHandler),  # 重定向
            (r"/iserror", index.ErrorHandler),  # 错误处理
            tornado.web.url(r"/reverse",index.ReverseHandler, name="reverse"),  # 反向解析
            (r"/uri/(\w+)/(\w+)",index.UriHandler),   # 通过uri 获取多个参数
            (r"/getMethod",index.GetMethodHandler),   # 通过get 获取多个参数
            (r"/postMethod", index.PostMethodHandler),  # 通过post 获取参数,上传文件
            (r"/requestObj", index.RequestObjHandler),  # request对象方法
            (r"/interface", index.InterfaceHandler),  # 接口调用顺序
            (r"/trans", index.TransHandler),  # 自动转义，防止恶意攻击
            (r"/base", index.BaseHandler),  # 继承
            (r"/shop",index.ShopHandler),  # 数据库调用
            (r"/normalCookie",index.NormalCookie),  # 普通cookie
            (r"/getCookie",index.GetCookie),  # 获取cookie
            (r"/clearCookie",index.ClearCookie),  # 清除cookie
            (r"/safeCookie",index.SafeCookie),  # 安全cookie，需要在config中settings配置秘钥
            (r"/getSafeCookie",index.GetSafeCookie),  # 获取安全cookie
            (r"/countCookie",index.CountCookie),  # cookie计数，记录浏览器访问次数。post请求开启xsrf需要配置
            (r"/login",index.Login),  # 登录
            (r"/cart",index.Cart),  # 购物车,登录成功则展示页面，登录不成功，重定向回登录页面
            (r"/async",index.Async),  # 异步请求

            # 这个路由要放在最后，匹配首页的静态文件。（注意：第一个匹配/ 就不需要了） http://127.0.0.1:9080/index.html或http://127.0.0.1:9080
            (r"/(.*)$", tornado.web.StaticFileHandler,{"path":os.path.join(config.BASE_DIR,"static/html"),"default_filename":"index.html"}),
        ]
        super(Application, self).__init__(handlers, **config.settings)
        # 数据库配置，设置tornadoSql.py 文件
        self.db = TornadoSql(config.mysql["host"],config.mysql["user"],config.mysql["password"],config.mysql["dbName"])
