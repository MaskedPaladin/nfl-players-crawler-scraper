from urllib.request import urlopen
import time
import os
from encodings.aliases import aliases

letterSearch = ord('A')
toSearchPlayers = []
searching = False
for i in range(26):
    urlToSearch = "https://www.pro-football-reference.com/players/"+chr(letterSearch)+"/"
    print(urlToSearch)
    pageToSearch = urlopen(urlToSearch)
    htmlToSearch = str(pageToSearch.read())
    for x in range(len(htmlToSearch)):
        if '<p><a href="' in htmlToSearch[x:x+12] and htmlToSearch[x+32:x+35] == "htm":
            toSearchPlayers.append(htmlToSearch[x+11:x+36])
    position = 0
    playerData = []
    for j, element in enumerate(toSearchPlayers):
        print("Players: "+str(j))
        print(element[:-1])
        urlPlayer = "https://www.pro-football-reference.com"+str(element[1:-1])
        print(urlPlayer)
        pagePlayer = urlopen(urlPlayer)
        htmlPlayer = pagePlayer.read()
        isExist = os.path.exists(".\\htm\\"+chr(letterSearch)+"\\")
        if isExist == False:
            os.makedirs(".\\htm\\"+chr(letterSearch)+"\\")
        fileName=".\\htm\\"+chr(letterSearch)+"\\"+element[12:-1]
        print(fileName)
        with open(fileName, 'wb') as f:
            try:
                f.write(htmlPlayer)
            except:
                print("Cannot write")
        f.close()
    letterSearch+=1