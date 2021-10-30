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
            node[0] = textToPut
            node[1] = seek
            allNodes.append(node)
            opened=True
            node=[[],[]]
            textToPut=""
        if opened==True:
            textToPut+=i
            if i == ">":
                node[0] = textToPut
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
    toSearchContent = []
    feeder = finder(url, search)
    comparable = obtainer(url)
    for value in comparable:
        if "<" not in value[0] and "/" not in value[0] and ">" not in value:
            toSearchContent.append(value)
    print(toSearchContent)
    for value in feeder:
        for element in toSearchContent:
            if element[1] == element[1]:
                contentFinded.append(value)
    return contentFinded