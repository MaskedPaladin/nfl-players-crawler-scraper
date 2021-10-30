import requests

def obtainer(url):
    opened = False
    r = requests.get(url)
    text = r.text
    textToPut = ""
    allNodes = []
    node = [[],[]]
    for seek, i in enumerate(text):
        if i == "<":
            node[0] = textToPut.rstrip()
            node[1] = seek
            allNodes.append(node)
            opened=True
            node=[[],[]]
            textToPut=""
        if opened==True:
            textToPut+=i
            if i == ">":
                node[0] = textToPut.rstrip()
                node[1] = seek
                allNodes.append(node)
                opened=False
                node=[[],[]]
                textToPut=""
        if opened==False and i != ">" and i != "<":
            textToPut+=i
    return allNodes
def finder(url, search):
    contentFinded = []
    feeder = obtainer(url)
    for value in feeder:
        if search in value[0]:
            contentFinded.append(value)
    return contentFinded
def obtainValue(url, search):
    contentFinded = []
    feeder = finder(url, search)
    comparable = obtainer(url)
    toPut = ""
    key = ""
    starter = []
    finisher = []
    toBePutted = []
    startKey = ""
    finishKey = ""
    init = False
    finish = False
    for element in comparable:
        for i, x in enumerate(element[0]):
            pass
    print(finisher)
    return contentFinded
    
    #Content in seek - length of content+1