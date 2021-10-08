#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

r = redis.StrictRedis(host="10.88.0.195", port=6379, db=8)
# 要重置的字段
key1 = "|activity-1:XServerPvp-1|remainTime"
key2 = "|activity-1:XServerPvp-1|battleCount"
key3 = "|activity-1:XServerPvp-1|cdTime"
key4 = "|activity-1:XServerPvp-1|usedHero"
key5 = "|activity-1:XServerPvp-1|tsHero"
key6 = "|activity-1:XServerPvp-1|randHero"

# 重置的账号列表
arrlist = ["100513", "100514", "100520", "100521", "100561", "100562", "100609", "100610", "100611", "100612"]

# 重置跨服衙门战斗次数，修改的db8里面玩家子数据
for uid in arrlist:
    dbHashStr = "ZSJ:1:user:" + uid
    r.hset(dbHashStr, key1, 1000 * 60)
    r.hset(dbHashStr, key2, 0)
    r.hset(dbHashStr, key3, 0)
    r.hset(dbHashStr, key4, "[]")
    r.hset(dbHashStr, key5, "[]")
    r.hset(dbHashStr, key6, "[]")
print("================ finished 重置 跨服衙门战斗 成功 ==============")

# 重置玩家铲除异党的领奖次数
ccydKey1 = "|activity-1:ccyd-1|usedHeroID"
ccydKey2 = "|activity-1:ccyd-1|usedHeroID"
ccydKey3 = "|activity-1:ccyd-1|usedHeroID"
ccydKey4 = "|activity-1:ccyd-1|usedHeroID"
ccydKey5 = "|activity-1:ccyd-1|usedHeroID"
ccydKey6 = "|activity-1:ccyd-1|usedHeroID"
ccydKey7 = "|activity-1:ccyd-1|usedHeroID"
ccydKey8 = "|activity-1:ccyd-1|usedHeroID"

""" 

     this.data.iEnterNum = 0
        this.data.tansuoNum = 10
        this.data.box = [0, 0, 0]
        this.data.score = 0
        this.data.duiHuanNum = {}
        this.data.duiHuanNum = this.data.duiHuanNum
        this.data.shopNum = {}
        this.data.shopNum = this.data.shopNum
        this.data.usedHeroID = []
        this.data.recHeroID = []
        this.data.bShowJuqing = true
        
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
