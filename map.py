'''
Author: CollaalloC
Date: 2022-01-21 21:54:45
LastEditors: CollaalloC
LastEditTime: 2022-01-23 11:26:05
Description: file content
Algorithm: algorithm
apiducuments: https://lbs.amap.com/api/webservice/guide/api/georegeo
'''
import re
from tkinter import W
from unittest import result
import requests
import json

from sympy import content
#api 必要参数
#正编码接口
geo_URL = "	https://restapi.amap.com/v3/geocode/geo?parameters"
#逆编码接口
regeo_URL = "https://restapi.amap.com/v3/geocode/regeo?parameters"

#！！！以下导航接口均使用路劲规划v2.0接口

#步行导航接口
walking_URL = "https://restapi.amap.com/v5/direction/walking?parameters"
#公交接口
integrated_URL = "https://restapi.amap.com/v5/direction/transit/integrated?parameters"
key = ""

#geoapi  正编码参数
city = "Beijing"
address = "北京科技大学"
output = "json"

geoparams = {
    "city": city,
    "address": address,
    "key":key,
    "output": output
    }

#regeoapi 逆编码参数
origin ="116.359375,39.988717"  #经纬度  北京科技大学
radius = 1000 #单位为m
extensions = "base"  #为all时，poitype生效
#poitype =    #可选参考
batch = "false" #批量查询开关，默认为关
roadlevel = 0 #默认显示所有路段

regeoparams={
    "location": origin,
    "radius": radius,
    #"poitype":
    "radius": radius,
    "extensions": extensions,
    "batch": batch,
    "roadlevel": roadlevel,
    "output":output
}

#walking api  步行导航接口
isindoor = 0 #室内导航，默认关闭
origin= ""
destination= ""
alternative_route = "1" #第一条线路，不传参默认返回一条路线
#show_fields = "navi,polyline" #只传基本参数

walkingparams={
    "key" :key,
    "isindoor": isindoor,
    "origin": origin,
    "destination": destination,
    "alternative_route": alternative_route,
    #"show_fields":show_fields,
    "output": output
}


# 从user_key中读取key
def readkey():
    with open("user_key",encoding="utf-8") as f :
        key = f.read()
        #print(key)
    return key
    
# 文件读取经纬度
#暂定从文件读取，也许后面可以直接调用，直接传经纬度就好
def getorigin(GPS_location):
    #直接传参
    #location = GPS_location 
    with open("GPS_location",encoding="utf-8") as gps:
        location = gps.read()
    return location

#address 为结构化参数，中文
#正编码，获取经纬度
def getdestination(address):
    # 直接传参
    #address = address
    geoparams["address"]=address
    geoparams["key"]=readkey()
    result = json.loads(requests.get(geo_URL,geoparams).content)
    #print(result)
    if (result['status'] == 0):
        print("API接口请求失败")
    else:
        '''
        geocodes=result['geocodes']
        geocodes = geocodes[0]
        location = geocodes["location"]
        return location
        '''
        return result["geocodes"][0]["location"]

#getdestination("五道口购物中心")

def walkingnavigation(origin, destination):
    walkingparams["origin"]=origin
    walkingparams["destination"]=destination
    walkingparams["key"]=readkey()
    result = json.loads(requests.get(walking_URL,walkingparams).content)
    return result
    #print(result)

destination = getdestination("五道口购物中心")
result = walkingnavigation("116.359375,39.988717",destination)
result


