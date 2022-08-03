# ef1500
# foriio scraper base classes
# UNFINISHED

from dataclasses import dataclass
import json

API_URL = "https://api.foriio.com/api/v1/users/{username}/profile/" # For future refrence

class foriio_profile:
    
    def __init__(self, jsonObj):
        jsonProfile = jsonObj["profile"]
        jsonUser = jsonObj["profile"]["user"]
        
        self.image = jsonProfile["meta"]["image"] # full URL
        self.profileId = jsonProfile['id']
        self.locale = jsonProfile['locale']
        self.bio = jsonProfile["bio"]
        self.location = jsonProfile["location"]
        self.profession = jsonProfile["profession"]
        self.website = jsonProfile["website"]
        self.name = jsonProfile["name"]
        self.contact_email = jsonProfile["contact_email"]
        self.instagram_url = jsonProfile["instagram_url"]
        self.facebook_url = jsonProfile["facebook_url"]
        self.twitter_url = jsonProfile["twitter_url"]
        self.avatar_url = jsonProfile["avatar"]["phone"] # Full URL
        self.i_want_to_work_with = jsonProfile["i_want_to_work_with"]
        self.favorite_id = jsonProfile["favorite_id"]
        self.is_pro = jsonProfile["is_pro"]
        self.fcm_phone_number = jsonProfile["fcm_phone_number"]
        
        self.userId = jsonUser["id"]
        self.email = jsonUser["email"]
        self.screen_name = jsonUser["screen_name"]
        self.user_type = jsonUser["user_type"]
        self.seeking_status = jsonUser["seeking_status"] 