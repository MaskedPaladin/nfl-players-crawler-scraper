import crawling

def main():
    characterNumber = ord('A')
    for i in range(26):
        character = chr(characterNumber)
        snippets = crawling.finder("https://www.pro-football-reference.com/players/",'<a href="/players/'+character+"/")
        for x in snippets:    
            urlSnippet = snippets[0][0]
            urlLetter = "https://www.pro-football-reference.com"+urlSnippet[9:20]
            players = crawling.finder(urlLetter,'<a href="/players/'+character)
            for player in players:
                playerSnippet = player[0][17:32]
                if "htm" not in playerSnippet[11:]:
                   playerSnippet = player[0][17:-2]
                print(playerSnippet)
                playerURL = "https://www.pro-football-reference.com/players"+playerSnippet
                playerPage = crawling.obtainer(playerURL)
                playerPageFinder = crawling.finder(playerURL,"<strong>")
                
                    
        characterNumber+=1
print(crawling.obtainValue("https://www.pro-football-reference.com/players/A/AaitIs00.htm","<p>"))


#main()