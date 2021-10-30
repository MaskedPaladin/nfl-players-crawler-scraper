import requests

def obtainer(url):
    opened = False
    r = requests.get(url)
    text = r.text
    textToPut = ""
    allNodes = []
    node = [[],[]]
    nodeNumber = 0
    for seek, i in enumerate(text):
        if i == "<":
            nodeNumber+=1
            node[0] = textToPut.strip()
            node[1] = nodeNumber
            allNodes.append(node)
            opened=True
            node=[[],[]]
            textToPut=""
        if opened==True:
            textToPut+=i
            if i == ">":
                nodeNumber+=1
                node[0] = textToPut.strip()
                node[1] = nodeNumber
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
    for i, element in enumerate(feeder):
        for j, value in enumerate(comparable):
            if value[1]==element[1]:
                contentFinded.append(comparable[j+1])
    return contentFinded