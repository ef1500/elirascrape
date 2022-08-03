# tellonym scraper base classes
# ef1500
# UNFINISHED

from dataclasses import dataclass
import json

API_URL = "https://api.tellonym.me/profiles/name/"
# Known Issues: Does not get all posts, only the first 10

class tellonym_post:
    
    def __init__(self, jsonObj):
        self.type = jsonObj["type"]
        self.postType = jsonObj["postType"]
        self.id = jsonObj["id"]
        self.answer = jsonObj["answer"]
        self.likesCount = jsonObj["likesCount"]
        self.created_at = jsonObj["createdAt"]
        self.tell = jsonObj["tell"]
        self.isLiked = jsonObj["isLiked"]
        self.userId = jsonObj["userId"]
        self.sender = jsonObj["sender"]
        self.isCurrentUserTellSender = jsonObj["isCurrentUserTellSender"]
        self.media = jsonObj["media"]
        self.pointsKarma = jsonObj["pointsKarma"]
        self.rtType = jsonObj["rtType"]
        self.rtVariance = jsonObj["rtVariance"]
        
        self.likeCount = jsonObj["likes"]["count"]
        self.like_isLiked = jsonObj["likes"]["isLiked"]
        self.isLikedBySender = jsonObj["likes"]["isLikedBySender"]
        self.previewUsers = jsonObj["likes"]["previewUsers"] # This is the form of a list
        
@dataclass
class tellonym_links:
    link_id: int
    status: int
    linktype: int
    link: str
    
@dataclass
class tellonym_avatars:
    avatarFileName: str
    position: int
        
class tellonym_profile:
    
    def __init__(self, jsonObj):
        self.avatar = jsonObj["avatarFileName"]
        self.followerCount = jsonObj["followerCount"]
        self.anonymousFollowerCount = jsonObj["anonymousFollowerCount"]
        self.followingCount = jsonObj["followingCount"]
        self.userId = jsonObj["id"]
        self.display_name = jsonObj["displayName"]
        self.username = jsonObj["username"]
        self.aboutMe = jsonObj["aboutMe"]
        self.likesCount = jsonObj["likesCount"]
        self.answerCount = jsonObj["answerCount"]
        self.tellCount = jsonObj["tellCount"]
        self.isAbleToChat = jsonObj["isAbleToChat"]
        #self.pinnedPosts = jsonObj["pinnedPosts"] # This is also a list
        self.tintColor = jsonObj["tintColor"]
        self.badge = jsonObj["badge"]
        self.statusEmoji = jsonObj["statusEmoji"]
        self.followNotificationType = jsonObj["followNotificationType"] # Data Exposure Vulner
        self.isVerified = jsonObj["isVerified"]
        self.isBlockedBy = jsonObj["isBlockedBy"]
        self.countryCode = jsonObj["countryCode"]
        self.isActive = jsonObj["isActive"]
        
        self.linkData = list(map(lambda id, status, link_type, link: tellonym_links(id, status, link_type, link), jsonObj["linkData"]))
        self.pinnedPosts = list(map(lambda jsonobj: tellonym_post(jsonobj), jsonObj["pinnedPosts"]))
        self.avatars = list(map(lambda avatarfilename, position: tellonym_avatars(avatarfilename, position), jsonObj["avatars"]))
        