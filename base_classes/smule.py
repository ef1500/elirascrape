# Smule Song Scraper Base Classes
# ef1500

import json
import requests
from dataclasses import dataclass

# API calls
# https://www.smule.com/p/{performance key}/json -> Performance Key JSON
# https://www.smule.com/s/performance/{performance key}/comments -> Comments JSON
# https://www.smule.com/s/performance/{perfKey}/loves -> Loves JSON
# 


@dataclass
class smule_user:
    account_id: int
    handle: str
    pic_url: str
    url: str
    verified_type: str
    lat: int
    lon: int
    
# For resolving a user's device
DeviceMap = {
    'sing' : 'iOS',
    'sing_google' : 'android',
    'sing_amazon' : 'amazon',
    'minipiano' : 'iOS',
    'minipiano_android' : 'android',
    'minipiano_amazon' : 'amazon',
    'autorap_goog' : 'android',
    'mg2_ios' : 'iOS'
}
    
class smule_performance: # ["list"] key
    def __init__(self, jsonObj):
        self.rec_id = jsonObj.get("rec_id")
        self.poi = jsonObj.get("poi")
        self.performance_key = jsonObj.get("performance_key")
        self.join_link = jsonObj.get("join_link")
        self.type = jsonObj.get("type")
        self.title = jsonObj.get("title")
        self.artist = jsonObj.get("artist")
        self.message = jsonObj.get("message")
        self.created_at = jsonObj.get("created_at")
        self.ensemble_type = jsonObj.get("ensemble_type")
        self.app_uid = jsonObj.get("app_uid")
        self.arr_type = jsonObj.get("arr_type")
        self.arr_key = jsonObj.get("arr_key")
        self.song_id = jsonObj.get("song_id")
        self.song_length = jsonObj.get("song_length")
        self.perf_status = jsonObj.get("perf_status")
        self.artist_twitter = jsonObj.get("artist_twitter")
        self.media_url = jsonObj.get("media_url")
        self.video_media_url = jsonObj.get("video_media_url")
        self.video_mp4_url = jsonObj.get("video_mp4_url")
        self.cover_url = jsonObj.get("cover_url")
        self.web_url = jsonObj.get("web_url")
        self.song_info_url = jsonObj.get("song_info_url")
        self.performed_by = jsonObj.get("performed_by")
        self.performed_by_url =jsonObj.get("performed_by_url")
        self.owner = smule_user(jsonObj["owner"]["account_id"], jsonObj["owner"]["handle"], jsonObj["owner"]["pic_url"], jsonObj["owner"]["url"], jsonObj["owner"]["verified_type"], jsonObj["owner"]["price"], jsonObj["owner"]["discount"])
        self.other_performers = list(map(lambda performerJSON: smule_user(performerJSON["account_id"], performerJSON["handle"], performerJSON["pic_url"], performerJSON["url"], performerJSON["verified_type"], performerJSON["price"], performerJSON["discount"]), jsonObj["other_performers"]))

class smule_user_api:
    def __init__(self, jsonObj): #also in the form of list (use this with a map function)
        self.account_id = jsonObj["account_id"]
        self.handle = jsonObj["handle"]
        self.pic_url = jsonObj["pic_url"]
        self.url = jsonObj["url"]
        self.followers = jsonObj["followers"]
        self.followees = jsonObj["followees"]
        self.num_performances = jsonObj["num_performances"]
        self.verified_type = jsonObj["verified_type"]
        self.sfam_count = jsonObj["sfam_count"]
        self.blurb = jsonObj.get("blurb")