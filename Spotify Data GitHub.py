# Import necessary modules
##################################################
import json
import csv
from itertools import zip_longest
import re
##################################################


# Load JSON File
##################################################
with open('StreamingHistory.json','r',encoding='utf8') as f:
    data = json.load(f)
##################################################


# Initialize Lists
##################################################
endTime = []
artistName = []
trackName = []
msPlayed = []
cnt = 0
##################################################


# Separate JSON file into lists, delete songs played for less than 10 seconds, delete "unknown artists"
##################################################
for i in range(len(data)):
    a = data[i]
    endTime.append(a['endTime'])
    artistName.append(a['artistName'])
    trackName.append(a['trackName'])
    msPlayed.append(a['msPlayed'])
    if ((re.search(r"Unknown",artistName[i-cnt])) or (msPlayed[i-cnt]<10000)):
        del endTime[i-cnt]
        del artistName[i-cnt]
        del trackName[i-cnt]
        del msPlayed[i-cnt]
        cnt = cnt+1
##################################################


# Prepare data for CSV file
##################################################
x = [endTime,artistName,trackName,msPlayed]
x_data = zip_longest(*x,fillvalue = '')
##################################################


# Write data to CSV file
##################################################
with open('SpotifyData.csv','w',encoding="utf8",newline='') as f2:
    wr = csv.writer(f2)
    wr.writerow(("Date","Artist","Track","ms Played"))
    wr.writerows(x_data)
f2.close()
##################################################
