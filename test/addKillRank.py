#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis
import json

r = redis.StrictRedis(host="10.88.0.194", port=6379, db=8)
# 要重置的字段
viewIdHash = "ZSJ:1:pvp:view:id"
viewListHash = "ZSJ:1:pvp:view:list"

# 时间戳很重要，要是当天时间，否则排行榜不显示
timeStamp = 1625215190373
#timeStamp = 1617964124000
fightUserId = "100023"

strAdd = {
  "userID": "",  # 战斗玩家的id
  "otherID": fightUserId,
  "type": 3,
  "count": 53,
  "time": 1625215190373,
  "heroName": "37",
  "way": 2,
  "score": 53,
  "state": 0,
  "id": "1625215424615_100013_3"
}

# print(repr(strAdd))


for iStart in range(10, 20):
    timeStamp = timeStamp+iStart
    viewIdKey = str(timeStamp) + "_100013_3"
    r.hset(viewIdHash, viewIdKey, fightUserId)  # 战斗玩家的id
    print(timeStamp)
    strAdd["time"] = int(timeStamp)
    strAdd["id"] = str(timeStamp)+"_100013_3"
    print(json.dumps(strAdd))
    r.lpush(viewListHash, json.dumps(strAdd))

print("================ finished  ==============")
