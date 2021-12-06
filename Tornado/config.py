import os

BASE_DIR = os.path.dirname(__file__)  # __file__ 属性查找该模块（或包）文件所在的具体存储位置, dirname 去掉文件，显示路径
'''
秘钥生产方式
import base64
import uuid
base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
'''


# 参数
options = {
    "port": 9080,
    "list": ["good", "nice"],
}
#mysql 配置。在application 初始化时使用
mysql = {
    "host": "localhost",
    "user": "root",
    "password":"123456",
    "dbName":"jd"
}


# 配置 ，在application继承时使用
settings = {
    "static_path": os.path.join(BASE_DIR, "static"),
    "template_path": os.path.join(BASE_DIR, "templates"),
    # 更改完代码，自动重启服务。 默认False,生产模式
    "debug": True,
    #"autoescaape": None, # 配置中关闭自动转义，不安全，多在模板中关闭
    "cookie_secret": "KfUB+aqTRGyS7DBgE3GevnVAxVWTAEveh8kgPoS2Cmw=",
    "xsrf_cookies": True,   #开启xsrf，此时post请求都会被拦截。在模板中用{% module xsrf_form_html() %}，则为表单开启隐藏域
    "login_url":"/login",  # 和装饰器方法共同使用，fail时需要这个参数
}
