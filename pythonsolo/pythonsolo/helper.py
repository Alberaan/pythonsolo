#! python
# -*- coding: utf-8 -*-
import os
import random
import re

tablesPath = "./static/Tablas"


def rt(system, filename):
    table = filename.replace(".txt", "")
    validstring = re.search(r"^[a-zA-Z_\s]*$", table)

    if not validstring:
        print("Invalid string")
        return None

    table = tablesPath + "/" + system + "/" + table + ".txt"

    with open(table, encoding="utf-8") as f:
        elements = [line.rstrip() for line in f]

    return random.choice(elements)


def get_tables(path=tablesPath):
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


def rtn(table_number):
    tables = get_tables(tablesPath)
    table = tables[table_number]
    
    return rt(table[1], table[2])
