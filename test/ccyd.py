#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

r = redis.StrictRedis(host="10.88.0.195", port=6379, db=3)
# 给redis 的 db3 结点，插入 ZSET 格式的数据
# redisHash值
dbHashStr = 'ZSJ:ccyd:606d0b243b898128db7afde6:ranking:selfScore:info'
index = 1
for userid in range(100300, 100520):
    r.zadd(dbHashStr, {str(userid): index})
    index = index + 1
    print("num:", index)
print("============================================\n")

""" 
需要安装redis模块，请在命令窗口执行下面的安装命令：
 pip install redis


账号列表： 
henry1   100513
henry2   100514
henry3   100520
henry4   100521
henry5   100561
henry6   100562
henry7   100609
henry8   100610
henry9   100611
henry10  100612

"""
