# smule runner.py
from base_classes.smule import *

def getPerformances(handle):
    API_URL = f"https://www.smule.com/s/profile/performance/{handle}/sing"
    userProfile = requests.get(API_URL)
    userProfile = userProfile.json()["list"]
    performances = list(map(lambda performanceJSON: performanceJSON["performance_key"], userProfile))
    return performances

def getPerformanceJson(perf_key):
    API_URL = f"https://www.smule.com/p/{perf_key}/json"
    performanceJSON = requests.get(API_URL)
    performanceJSON = performanceJSON.json()
    return(smule_performance(performanceJSON))
    
def getUserInfoFromAPI(username):
    API_URL = f"https://www.smule.com/s/user_profiles/{username}/json"
    userJson = requests.get(API_URL)
    userJson = userJson.json()
    userProfile = list(map(smule_user_api, userJson))[0]
    return userProfile

def userLookupAPI_Print(user_id):
    userinfo = getUserInfoFromAPI(user_id)
    userinfostring = f"""
account_id: {userinfo.account_id}
handle: {userinfo.handle}
pfp_url: {userinfo.pic_url}
blurb: {userinfo.blurb}
    """
    print(userinfostring)

def userLookup_Print(username):
    perfs = getPerformances(username)
    perfdata = list(map(getPerformanceJson, perfs))
    for data in perfdata:
        info = generateTextInfo(data)
        for j in info:
            print(j)
            
def generateTextInfo(obj):
    performance_info = f"""
performance key: {obj.performance_key}
type: {obj.type}
title: {obj.title}
artist: {obj.message}
message: {obj.message}
created_at: {obj.created_at}
ensemble_type: {obj.ensemble_type}
app_uid: {obj.app_uid} [{DeviceMap[obj.app_uid]}]"""
    
    yield performance_info
    
    owner_info = f"""
account_id: {obj.owner.account_id}
handle: {obj.owner.handle}
pic_url: {obj.owner.pic_url}
verified_type {obj.owner.verified_type}
coords: {obj.owner.lat}, {obj.owner.lon}"""
    yield owner_info
    
    users_info = list(map(lambda userObj: f"""
account_id: {userObj.account_id}
handle: {userObj.handle}
pic_url: {userObj.pic_url}
verified_type {userObj.verified_type}
coords: {userObj.lat}, {userObj.lon}""", obj.other_performers))
    
    for userinfo in users_info:
        yield userinfo 