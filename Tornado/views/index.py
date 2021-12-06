import tornado
from tornado.web import RequestHandler

import os,time
import config


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("reverse")  # 反向解析
        self.write("<a href='%s'>跳转</a>"%(url))

class HomeHandler(RequestHandler):
    def initialize(self,name):
        self.name = name
    def get(self):
        dict = {
            "age":19,
            "sex":"female"
        }
        flag = 1
        stus = [{"name":"a","age":15},{"name":"b","age":18}]
        def mySum(n1,n2):  # 自定义函数返回模板
            return n1+n2

        self.render("home.html", username = self.name,detail = dict,flag=flag,stus=stus,mySum=mySum)

class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("1")
        self.write("2")
        self.finish()  # 刷新缓冲区，关闭当前请求通道。下方不要在write
        #self.write("3")

import json
class JsonHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("cby", "good")  #设置自定义响应头字段
    def get(self):
        data = {
            "name": "cby",
            "age": 18
        }
        #jsonStr = json.dumps(data)

        self.write(data)  # 无需手动转换，而且返回的content-type 为application/json

class StatusHandler(RequestHandler):
    def get(self):
        #self.set_status(404)
        #self.set_status(601,"no data")
        self.set_status(999)

class RedirectHandler(RequestHandler):
    def get(self):
        self.redirect("/")

class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            reason = "服务器内部错误哦"
        elif status_code == 404:
            reason = "资源不存在"
        else:
            reason = "未知错误"
        #print(status_code, reason)
        self.set_status(status_code,reason)
    def get(self):
        flag = self.get_query_argument("flag")
        if flag == "0":
            self.send_error(601)
        else:
            self.write("ok")

class ReverseHandler(RequestHandler):
    def get(self):
        self.write("反向解析")

class UriHandler(RequestHandler):
    def get(self,arg1,arg2):
        self.write("c"+arg1+arg2)

class GetMethodHandler(RequestHandler):
    def get(self):
        a = self.get_query_argument("a",default="100",strip=True)  # strip 是否过滤掉参数左右两边的空格
        # http://127.0.0.1:9080/getMethod?a=1&a=2 多个a参数
        #aList = self.get_query_arguments("a")
        self.write(a)

class PostMethodHandler(RequestHandler):
    def get(self):
        self.render("register.html")
    def post(self,*args,**kwargs):
        username = self.get_body_argument("username")
        age = self.get_argument("age")   # get_argument get,post 都可以用
        hobbys = self.get_body_arguments("hobby")
        fileDict = self.request.files    # 获取上传文件
        print(fileDict) # 三个参数，filename，body，content-type。每个filename都是一个文件对象
        for names in fileDict:  # 上传多个文件的name不同
            fileArr = fileDict[names]
            for fileObj in fileArr:
                if fileObj.content_type == '': # 判断传入的文件格式是否合适
                    pass
                upfile_path = os.path.join(config.BASE_DIR,"upfile/"+fileObj.filename)
                with open(upfile_path,"wb") as f:
                    f.write(fileObj.body)

        self.write(username+age+hobbys[0])

class RequestObjHandler(RequestHandler):
    def get(self):
        self.write(self.request.method + self.request.remote_ip)

class InterfaceHandler(RequestHandler):
    def initialize(self):  # 初始化处理
        pass
    def prepare(self):  # 预处理函数， 可以放置反爬虫代码，信息码
        pass
    def get(self,*args,**kwargs):
        pass
    def set_default_headers(self):
        pass
    def write_error(self, status_code, **kwargs):
        pass
    def on_finish(self):   # 请求处理后调用,和客户端没啥关系了。 可以资源清理释放，日志处理，大数据分析
        pass

class TransHandler(RequestHandler):
    def get(self):
        str = "<h1>111</h1>"   # 页面会显示字符串，不会变成前端代码，防止js注入
        self.render("trans.html",str = str)

class BaseHandler(RequestHandler):
    def get(self):
        self.render("base1.html")

class ShopHandler(RequestHandler):
    def get(self):
        #shops = self.application.db.DBquery("select productid,productname from jdapp_goods","jdapp_goods","productid","productname")
        shops = self.application.db.DBquery("select * from jdapp_goods","jdapp_goods")
        print(shops)
        self.render("shop.html",shops = shops)

class NormalCookie(RequestHandler):
    def get(self):
        self.set_cookie("cby","123456",expires_days=1) # 原理和设置返回头中的Set-Cookie一样
        self.set_header("Set-Cookie","cby2=12345678; Path=/")
        self.write("ok")

class GetCookie(RequestHandler):
    def get(self):
        cookie = self.get_cookie("cby","未登录")
        self.write(cookie)

class ClearCookie(RequestHandler):
    def get(self):
        self.clear_cookie("cby",path="/",domain=None) # 防止cookieName一样，用域名和path来加以区分
        self.clear_all_cookies() # 清除所有cookie

class SafeCookie(RequestHandler):
    def get(self):
        self.set_secure_cookie("safeCookie","123")  # 防止cookie被伪造,设置出来的cookie内容进行过加密
        self.write("ok")

class GetSafeCookie(RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("safeCookie")
        self.write(cookie)

class CountCookie(RequestHandler):
    def get(self):
        count = self.get_cookie("count", "未登录")
        self.render("count.html",count = count)
    def post(self):
        count = self.get_cookie("count",None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count",str(count))
        self.render("count.html",count = count)

class Login(RequestHandler):
    def get(self):
        next = self.get_argument("next","/")
        url = "login?next="+next
        self.render("login.html", url=url)
    def post(self):
        username = self.get_body_argument("username")
        age = self.get_body_argument("age")
        password = self.get_body_argument("password")
        if username == "1" and password == "1":
            next = self.get_argument("next","/")
            print(next)
            self.redirect(next+"?flag=logined")
        else:
            next = self.get_argument("next", "/")
            self.redirect("/login?next="+next)

class Cart(RequestHandler):
    def get_current_user(self):
        flag = self.get_argument("flag",None)
        return flag
    @tornado.web.authenticated  # 装饰器，验证通过（get_current_user）才能进入get方法
    def get(self):
        self.render("cart.html")

from tornado.httpclient import AsyncHTTPClient
import tornado.gen
class Async(RequestHandler):   # 此时Handler作为请求的客户端，用来进行异步请求
    @tornado.gen.coroutine
    def get(self):
        client = AsyncHTTPClient()
        url="https://www.runoob.com/"
        response = yield client.fetch(url)
        # 异步响应一个tornado.httpclient.HTTPResponse。 request可以是url，也可以是tornado.httpclient.HTTPRequest对象
        return self.finish(response.body)
