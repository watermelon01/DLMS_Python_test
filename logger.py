import time 
from datetime import datetime, timedelta

def getTimestamp(): 
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Logger:
    def __init__(self,fileName,tsEnable=True,clearFile=True):
        self.tsEnable = tsEnable 
        self.filename = fileName
        if clearFile == True:
            with open(fileName, "w") as f:
                f.write("")

    def write(self,message):        
        prefix = ""
        if self.tsEnable == True:
            prefix = getTimestamp() + " : "
        with open(self.filename, "a") as f: 
            f.write(prefix + message + "\n")