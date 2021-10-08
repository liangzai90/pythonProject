#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

r = redis.StrictRedis(host="10.88.0.195", port=6379, db=8)
# 要重置的字段
key1 = "|pvp-1|remainTime"
key2 = "|pvp-1|timeStamp"
key3 = "|pvp-1|times"
key4 = "|pvp-1|usedHero"
key5 = "|pvp-1|tsHero"
key6 = "|pvp-1|randHero"


# 重置的账号列表
arrlist = ["200013", "100513", "100514", "100520", "100521", "100561", "100562", "100609", "100610", "100611", "100612"]

for uid in arrlist:
    dbHashStr = "ZSJ:1:user:" + uid
    r.hset(dbHashStr, key1, 0)
    r.hset(dbHashStr, key2, 0)
    r.hset(dbHashStr, key3, 0)
    r.hset(dbHashStr, key4, "[]")
    r.hset(dbHashStr, key5, "[]")
    r.hset(dbHashStr, key6, "[]")
print("================ finished 重置衙门战斗次数成功 ==============")

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
