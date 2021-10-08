#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis
import json


# ZSJ:XJingCheng:20210621:1-2-3-4-5-6-8:qiangduo:list

r = redis.StrictRedis(host="10.88.0.195", port=6379, db=3)
viewListHash = "ZSJ:XJingCheng:20210621:1-2-3-4-5-6-8:qiangduo:list"

strAdd ={
    "fudiPos":{"mainID":5,"subID":2},
    "group":"20210621:1-2-3-4-5-6-8",
    "type":0,
    "ts":1624433154389,
    "uidA":"100514",
    "uNameA":"henry_514-123456",
    "dressA":["110",3,""],
    "uidB":"100521",
    "uNameB":"到此一游",
    "success":1
}

# print(repr(strAdd))


for iStart in range(11, 100):
    iAddTs = 5*10000 * iStart
    strAdd["ts"] = int(strAdd["ts"]) + iAddTs
    strAdd["uidA"] = str( int(strAdd["uidA"])+iStart)
    print(json.dumps(strAdd))
    r.lpush(viewListHash, json.dumps(strAdd))

print("================ finished  ==============")
