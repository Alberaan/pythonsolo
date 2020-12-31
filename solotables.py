#! python
# -*- coding: utf-8 -*-
import random
import re
import os
from dice import roll

tablesPath = "./Tablas"

def rt(system, filename):
    table = filename.replace(".txt", "")
    validstring = re.search("^[a-zA-Z_\s]*$", table)

    if not validstring:
        print("Invalid string")
        return None

    table = tablesPath + "/" + system + "/" + table + ".txt"

    with open(table, encoding="utf-8") as f:
        elements = [line.rstrip() for line in f]


    return random.choice(elements)

def getTables(path=tablesPath):
    directories = os.listdir(path)
    cont = 0

    tablesToReturn = []

    for directory in directories:
        tables = os.listdir(path + "/" + directory)
        for table in tables:
            if ".txt" in table:
                tablesToReturn.append([cont, directory.split("/")[-1], table.replace(".txt", "")])
                cont +=1

    return tablesToReturn

def lt(filterstring=""):
    tables = getTables(tablesPath)
    for table in tables:
        if filterstring.lower() in table[1].lower() or filterstring.lower() in table[2].lower():
            print(str(table[0]) + ":\t" + "(" + table[1] + ")\t" + table[2])

    print("")

def rtn(tableNumber):
    tables = getTables(tablesPath)
    table = tables[tableNumber]
    
    print(rt(table[1], table[2]))
    print("")

def rts(searchString):
    tables = getTables(tablesPath)

    matches = [s for s in tables if searchString.lower() in s[2].lower()]

    if len(matches) == 0:
        print("No tables found")
        return

    if len(matches) > 1:
        print("Multiple tables found: ")
        for table in matches:
            print(str(table[0]) + "\t(" + table[1] + ")\t" + table[2])
        return

    if len(matches) == 1:
        print("Table found: " + matches[0][2])
        print(rt(matches[0][1],matches[0][2] + ".txt"))

def r(string):
    results = roll(string)
    minimum = None
    maximum = None
    total = 0

    if isinstance(results, int):
        print(results)
        return

    for dice in results:
        if minimum == None and maximum == None:
            minimum = dice
            maximum = dice
        
        if dice < minimum:
            minimum = dice
        if dice > maximum:
            maximum = dice

        total += dice

    print(results)
    print("\nMinimum=" + str(minimum) + ", Maximum=" + str(maximum) + ", total=" + str(total))

def help():
    print("Available commands:\n")
    print("rt(system,filename): rolls in a random table of the specified system")
    print("lt([filter]): lists all tables included. If filter is specified, it will only show tables/system that include the filter.")
    print("rtn(number): rolls in the random table with the index number. This number can be found when listing tables or searching tables.")
    print("rts(searchname): searches for tables containing the searchname parameter. If there is only one table found, it will roll on it.")
    print("")
