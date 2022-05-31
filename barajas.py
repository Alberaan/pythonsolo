#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import random

tables_path = "Barajas"

def rt(table_name):

    valid_string = re.search(r"^[a-zA-Z_\sñ0-9]*$", table_name)

    if not valid_string:
        return "Invalid string"

    table_path= tables_path + "/" + table_name + ".txt"

    elements = []
    with open(table_path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            elements.append(line)

    curatedElements = [x for x in elements if "*" not in x]
    chosen = random.choice(elements)

    index = elements.index(chosen)
    elements[index] = "*" + elements[index] 

    with open(table_path, "w", encoding="utf-8", errors="ignore") as f:
        for element in elements:
            f.write(element)

    return "Resultados para '" + table_name + "': " + chosen 

def reset(table_name):
    table_path= tables_path + "/" + table_name + ".txt"
    elements = []

    with open(table_path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            elements.append(line)

    with open(table_path, "w", encoding="utf-8", errors="ignore") as f:
        for element in elements:
            f.write(element.replace("*", ""))

def listado(table_name):
    table_path= tables_path + "/" + table_name + ".txt"

    elements = []
    with open(table_path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            elements.append(line)

    curatedElements = [x for x in elements if "*" in x]

    returnString = ""

    for element in curatedElements:
        returnString += element

    return returnString

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Error\n" + sys.argv[0] + " [nombre de la baraja] para robar una carta\n" + sys.argv[0] + " [nombre de la baraja] '-l' para listar descartes\n" + sys.argv[0] + " [nombre de la baraja]'-r' para barajar de nuevo")
    exit()

if "-r" in sys.argv[1]:
    reset(sys.argv[2])
    print("Barajada la baraja " + sys.argv[2])
    exit() 

if "-l" in sys.argv[1]:
    print(listado(sys.argv[2]))
    exit()

print(rt(str(sys.argv[1])))

