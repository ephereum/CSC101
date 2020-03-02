# Coded by Ephraim Pillar G20P0425

import time 

def getCurrentTime():
    currentReceived = time.ctime()
    return currentReceived 

currentTime = getCurrentTime() 
print(currentTime[10:20])


    