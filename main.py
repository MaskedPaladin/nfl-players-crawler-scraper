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
                name = crawling.obtainValue(playerURL,"<strong>")
                position = crawling.obtainValue(playerURL,"</strong>")
                print(name[1][0])
                print(position[3][0][2:])
        characterNumber+=1
main()
