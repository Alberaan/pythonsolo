import pickle
from palantirRequests import *
from responseline import *

def indent(level):
    indentation = ""

    for i in range(0, level):
        indentation += "-"

    return indentation

def printResponse(response):
    text = ""

    for textLine in response:
        if textLine.lineType== "normal":
            if response != None:
                text += textLine.text + ", "
            else:
                text += textLine.text + "\n"
        if textLine.lineType == "table":
            text += indent(textLine.indent) + "[" + textLine.text + "]" + "\n"
        if textLine.lineType == "attribute":
            generated_result = True
            text += indent(textLine.indent) + textLine.attribute + ": " + textLine.attributeValue + "\n"

    print(text)

def askPalantir(query):
    response = listRequest(query)
    printResponse(response)
    return(response)

def cachePalantir():
    languages = listRequest("")
    returnTables = []

    languageIndex = 0
    for language in languages:
        returnTables.append([languageIndex, language.text])
        systems = listRequest(language.text)
        systemIndex = 0
        for system in systems:
            returnTables.append([languageIndex, systemIndex, language.text, system.text])
            tables = listRequest(language.text + " " + system.text)
            tableIndex = 0
            for table in tables:
                returnTables.append([languageIndex, systemIndex, tableIndex, language.text, system.text, table.text])
                tableIndex += 1
            systemIndex += 1
        languageIndex += 1

    binaryFile = open("palantirCache.bin", mode="wb")
    pickledReturnTables = pickle.dump(returnTables, binaryFile)
    binaryFile.close()

def searchPalantir(query):
    binaryFile = open("palantirCache.bin", mode="rb")
    tables = pickle.load(binaryFile)
    binaryFile.close()

    for table in tables:
        if len(table) == 2 and query.lower() in table[1].lower():
            print("[language] " + str(table[0]) + ": " + table[1])
        if len(table) == 4 and query.lower() in table[3].lower():
            print("[system] " + str(table[0]) + "." + str(table[1]) + ": " + table[2] + "/" + table[3])
        if len(table) == 6 and query.lower() in table[5].lower():
            print("[table] " + str(table[0]) + "." + str(table[1]) + "." + str(table[2]) + ": " + table[3] + "/" + table[4] + "/" + table[5])


#cachePalantir()

searchPalantir("maze")
