
import os
import shutil
import time
def main (): 

    days=30
    path="F:/Documents/Zoom"
    seconds=time.time()-days*24*60*60
    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds>= getfileorfolderage(rootfolder):
                removefolder(rootfolder)
                break
            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)
                    if seconds>= getfileorfolderage(folderpath):
                        removefolder(folderpath)

                for file in files:
                    filepath=os.path.join(rootfolder,file)
                    if seconds>= getfileorfolderage(filepath):
                        removefile(filepath)
    else:
        print("path not found")

def removefolder(path):
    shutil.rmtree(path)
    print("path deleted sucessfully")

def removefile(path):
    os.remove(path)
    print("file removed sucessfully")

def getfileorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime

  
                        
             