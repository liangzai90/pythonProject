#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

r = redis.StrictRedis(host="10.88.0.195", port=6379, db=3)
# 给redis 的 db3 结点，插入 ZSET 格式的数据
# redisHash值
dbHashStr = 'ZSJ:Xccyd20210519:60a5bde0b1d21c534b93a919:1-2-3-4-5-8:pre:selfRank:S1'
index = 1
for userid in range(100500, 100620):
    r.zadd(dbHashStr, {str(userid): index})
    index = index + 1
    print("num:", index)
print("============================================\n")
