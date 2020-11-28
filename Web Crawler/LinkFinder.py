from html.parser import HTMLParser  
from urllib import parse

class LinkFinder(HTMLParser):

    def handle_starttag(self,tag,attrs):
        if tag == 'href':
            for (param,value) in attrs:
                if param == 'href':
                    print(value)


    def __init__(self):
        super().__init__()
    def error(self,message):    
        pass