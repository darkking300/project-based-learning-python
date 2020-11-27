#create all the necessary folder structure and files
import os

def create_project_dir(baseUrl):
    temp = '.'.split(baseUrl) # stripping off to get website name to set as baseDirectory name
    baseDir = temp[1]
    if not os.path.exists(baseDir):
        print('Creating Base Directory:')
        os.makedirs(baseDir)


def create_queue(baseUrl,baseDirectory):
    queue_file = baseDirectory + "queue.txt"
    crawled_file = baseDirectory + "crawled.txt"
    if not os.path.isfile(queue_file):
        print('Creating queue.txt at ', baseDirectory )
        writeFile(queue_file,baseUrl)
    if not os.path.isfile(crawled_file):
        print('Creating crawled.txt at ', baseDirectory)
        writeFile(crawled_file,"")    



def writeFile(fileName,param):
    f = open(fileName,'w')
    f.write(param)
    f.close()        
