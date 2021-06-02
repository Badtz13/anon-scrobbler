import os,time
from datetime import datetime

username="MiloCodes"

os.system('mpv --volume=40  http://anonradio.net:8000/anonradio > store.txt &')

title=''
recentLine = ''

while(True):
    time.sleep(2)
    with open("store.txt") as file_in:
        lines = []
        for line in file_in:
            if "icy-title" in line:
                recentLine = line.strip()

    songInfo = recentLine.split(':')[1].split(' - ')
    if len(songInfo) > 1:
        if title != songInfo[1]:
            print(recentLine)
            now = datetime.now().strftime('%Y-%m-%d.%H:%M')
            os.system('scrobbler scrobble ' + username + " \"" + songInfo[0] + "\" \"" + songInfo[1] + "\" " + now)
            title = songInfo[1]
