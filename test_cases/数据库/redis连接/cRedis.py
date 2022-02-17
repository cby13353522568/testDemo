# -*- coding: UTF-8 -*-
# @Time: 2021/2/20 13:42
# @File: cRedis.py
import redis


class CRedis:
    def __init__(self, password, host="localhost", port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=password)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return "不存在该key"
