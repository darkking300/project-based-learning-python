from html.parser import HTMLParser  
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self):
        super.__init__()
    def error(self,message):    
        pass