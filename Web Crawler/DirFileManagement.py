#create all the necessary folder structure and files
import os

def create_project_dir(baseUrl):
    temp = '.'.split(baseUrl) # stripping off to get website name to set as baseDirectory name
    baseDir = temp[1]
    if not os.path.exists(baseDir):
        print('Creating Base Directory:')
        os.makedirs(baseDir)


def create_queue(baseUrl,baseDirectory):
    queue_file = baseDirectory + "/queue.txt"
    crawled_file = baseDirectory + "/crawled.txt"
    if not os.path.isfile(queue_file):
        print('Creating queue.txt at ', baseDirectory )
        writeFile(queue_file,baseUrl)
    if not os.path.isfile(crawled_file):
        print('Creating crawled.txt at ', baseDirectory)
        writeFile(crawled_file,"")    



def writeFile(filePath,param):
    f = open(filePath,'w')
    f.write(param)
    f.close()        

#add a new link to the file
def addToFile(filePath,param):
    with open(filePath,'a') as file:
        file.write(param + '\n')

#truncate the file
def truncFile(filePath):
    with open(filePath,'w'):
        pass

#Read a file and convert to set items
def fileToSet(fileName):
    results = set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n','')) 
    return results

def setToFile(saidSet,fileName):
    truncFile(fileName)
    for link in sorted(saidSet):
        addToFile(fileName,link)


        
