'''
Author: CollaalloC
Date: 2022-01-21 21:54:45
LastEditors: CollaalloC
LastEditTime: 2022-01-22 16:58:27
Description: file content
Algorithm: algorithm
apiducuments: https://lbs.amap.com/api/webservice/guide/api/georegeo
'''
import re
import requests
import json
#api 必要参数
geo_URL = "	https://restapi.amap.com/v3/geocode/geo?parameters"
regeo_URL = "https://restapi.amap.com/v3/geocode/regeo?parameters"


#geoapi
city = "Beijing"
address = "北京科技大学"
output = "json"

geoparams = {
    "city": city,
    "address": address,
    "key":key,
    "output": output
    }

#regeoapi
location ="116.359375,39.988717"  #经纬度  北京科技大学
radius = 1000 #单位为m
extensions = "base"  #为all时，poitype生效
#poitype =    #可选参考
batch = "false" #批量查询开关，默认为关
roadlevel = 0 #默认显示所有路段

regeoparams={
    "location": location,
    "radius": radius,
    #"poitype":
    "radius": radius,
    "extensions": extensions,
    "batch": batch,
    "roadlevel": roadlevel,
    "output":"json"
}

def readkey():

def getorigin(GPS_location):
    location = GPS_location
