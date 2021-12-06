# -*- coding: UTF-8 -*-
# @Time: 2021/2/20 11:29
# @File: redis连接.py
import redis


# 连接redis
re = redis.StrictRedis(host="localhost",port=6379,password="123456")

re.set(name="name",value="cby")
print(re.get("name").decode("utf-8"))

# 管道 缓冲多条命令，然后依次执行，减少客户端服务器之前的TCP数据包
pipe = re.pipeline()
pipe.set("p2","ccc")
pipe.set("p3","ddd")
pipe.execute()
# set时候一般用，get 直接取就行
