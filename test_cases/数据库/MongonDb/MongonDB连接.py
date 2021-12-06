# -*- coding: UTF-8 -*-
# @Time: 2021/2/13 20:25
# @File: MongonDB连接.py
import pymongo
from bson.objectid import ObjectId   #用于Id查询
# 连接服务
myclient = pymongo.MongoClient("localhost",27017)

mydb = myclient["cby"]
print(myclient.list_database_names()) # 返回数据库信息
mytable = mydb["student"]
#mytable.insert_one({"name":"cby3","age":19})    # insert_many 插入数组，元素都是字典{[],[],[]}
#querys = mytable.find({"age":19},{"_id": 0,"name":1}).sort("name",-1)  # 0 不返回，1返回
querys = mytable.find({"_id":ObjectId("602e21c788750b0370cb457b")})
for query in querys:
    print(query)
#mytable.update_one({"name":"cby"},{"$set":{"age":22}})
#mytable.delete_one({"name":"cby3","age":19})
#mytable.delete_one({"age":18})
