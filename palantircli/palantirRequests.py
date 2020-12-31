import requests
from jsonparsing import *

def processCommand(command):

    response = ""

    if command.startswith("/rpglist"):
        response = listRequest(command)
    elif command.startswith("/help"):
        response = helpRequest()
    elif command.startswith("/start"):
        response = helpRequest()
    else:
        pass

    return response

def listFunction(url):

    r = requests.get(url = url)
    lines = []

    try:
        data = r.json()

        if ("success" in data and data["success"] == True):
            lines = toTextList(data)
        else:
            line = responseline()
            line.lineType = "normal"
            line.text = "No available data"
            lines.append(line)

    except ValueError:
            line = responseline()
            line.lineType = "normal"
            line.text = "Could not process your request"
            lines.append(line)

    return lines

def genFunction(url):

    url = url.replace("/api/types/", "/api/random/")
    r = requests.get(url)
    lines = []

    try:
        data = r.json()
        if ("success" in data and data["success"] == True):
            lines = jsonToTextGen(data)
        else:
            line = responseline()
            line.lineType = "normal"
            line.text = "No available data."
            lines.append(line)

    except ValueError:
        line = responseline()
        line.lineType = "normal"
        line.text = "Could not process your request."
        lines.append(line)

    return lines

def listRequest(msg):
    command = msg
    basicurl = "https://hall.herokuapp.com/api/types"

    arguments = command.replace("/rpglist", "")

    if command == "":
        options = []
    else:
        options = arguments.split(" ")

    listOrGenerate = "list"

    if len(options) == 3:
        listOrGenerate = "generate"

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"

    if listOrGenerate == "list":
        lines = listFunction(url)
    elif listOrGenerate == "generate":
        lines = genFunction(url)

    return lines
