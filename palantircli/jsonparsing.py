import json
from responseline import *

def toTextList(data):
    lines = []

    for node in data["data"]:
        mynode = node.replace(".yml", "")
        line = responseline()
        line.lineType = "normal"
        line.text = mynode
        lines.append(line)

    return lines


def jsonToTextGen(data):
    node = data["data"][0]

    lines = []
    response = formatJSON(lines, node, None, 0)
    return response

def formatJSON(lines, node, parent, level):

    if "children" not in node:
        line = responseline()
        line.indent = level
        line.lineType = "attribute"
        line.attribute = node["title"]
        line.attributeValue = node["text"]
        lines.append(line)
    else:
        line = responseline()
        line.indent = level
        line.lineType = "table"
        line.text = node["title"]
        lines.append(line)
        for children in node["children"]:
            lines += formatJSON([], children, node, level+1)

    return lines
