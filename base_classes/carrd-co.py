# carrd.co scraper classes
# ef1500
#UNFINISHED

from bs4 import BeautifulSoup
from dataclasses import dataclass
# Make Sure to use soup = BeautifulSoup(page, "html.parser")

@dataclass
class carrd_meta:
    description: str
    site_name: str
    title: str
    image: str

class carrd_properties:
    
    @staticmethod
    def getCarrdMeta(pagedata):
        carrd_description = pagedata.find('meta', name="description")
    
    def __init__(self, pageData):
        self.carrdMeta = 