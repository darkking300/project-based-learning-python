from urllib.request import Request, urlopen, URLopener  
from html.parser import HTMLParser
import os
import traceback
from sys import argv
import subprocess

baseUrl = argv[1]

class LinkParse(HTMLParser):
	linkStore = set()
	folderName = ''
	def handle_starttag(self,tag,attrs):
		if tag == 'title' and not(os.path.exists('title')):
			createFolder(attrs)
			folderName = tag
		elif tag == 'img':
			for (param,value) in attrs:
				if param == 'src':
					self.linkStore.add(value)

	def __init__(self):
		super().__init__()
		
	def error(self):
		print('An error has occured')



def createFolder(folderName):
	os.makedirs(folderName)
	
def urlEdit(imgUrl):
#function to remove the small s in the file name which causes smaller size image to download
	sliced = imgUrl.split('.')
	sliced[-2] = sliced[-2][0:-1]
	return '.'.join(sliced)
	
	
def downloadFile(linkStore):
	for imgUrl in linkStore:
		try:
			#removing double slash from the start of url
			imgUrl = urlEdit(imgUrl[2:])
			fileName = imgUrl.split("/")[-1]
			print('Downloading file: '+fileName+'\tURL: '+imgUrl+'\n')
			image = URLopener()
			image.retrieve(imgUrl,fileName)
			# above line may create error due to 403 forbidden response
		except:
			print("Error occured while downloading")
			traceback.print_exc()	
		print("\n")	
		continue

def theCoreFunction():
	try:
		req = Request(baseUrl,headers={'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'none'})
		# above header is to avoid 403 forbidden error message
		response = urlopen(req, timeout=20).read()
		f = LinkParse()
		f.feed(str(response))
		downloadFile(f.linkStore)
		#subprocess.check_call('mv','*.jpg','*.png','*.webm','./'+f.folderName)
	except:
		print("Excpetion Occured\n")
		traceback.print_exc()
		
		
theCoreFunction()		