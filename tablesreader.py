#! python
# -*- coding: utf-8 -*-
import random
import re
import os
from dice import roll
import sys
import inspect

tablesPath = "./Tablas"

class Response:
    def __init__(self, message="", data=None):
        self.message = message
        self.data = data

class Table:
    def __init__(self, index, system, filename):
        self.index = index
        self.system = system
        self.filename = filename

def rt(chosen_table):

    table_name = chosen_table.filename.replace(".txt", "")
    validstring = re.search(r"^[a-zA-Z_\s]*$", table_name)

    if not validstring:
        return Response(message="Invalid string", data=None)

    table_path= tablesPath + "/" + chosen_table.system + "/" + table_name + ".txt"

    with open(table_path, encoding="utf-8", errors="ignore") as f:
        elements = [line.rstrip() for line in f]

    return Response(message="Result:", data=random.choice(elements))

def getTables(path=tablesPath):
    directories = os.listdir(path)
    cont = 0

    tablesToReturn = []

    for directory in directories:
        tables = os.listdir(path + "/" + directory)
        for table in tables:
            if ".txt" in table:
                tablesToReturn.append(Table(cont, directory.split("/")[-1], table.replace(".txt", "")))
                cont +=1

    return tablesToReturn

#lt [filtro]: lista todas las tablas. Si se especifica un filtro, solo se mostrarán aquellas tablas/sistemas cuyo nombre contenga el filtro especificado. Ejemplo: "lt" mostrará todas las tablas. "lt tarot" muestra todas las tablas o sistemas que contengan la palabra tarot
def lt(tables, filterstring=""):
    tables_to_return = []

    for table in tables:
        if filterstring.lower() in table.system.lower() or filterstring.lower() in table.filename.lower():
            tables_to_return.append(table)

    return Response(message="", data=tables_to_return)

#rtn número: obtén un elemento aleatorio de la tabla con el número especificado. Este número puede consultarse cuando se listan o buscan tablas. Ejemplo "rtn 1" hará una tirada en la tabla 1
def rtn(tables, tableNumber):

    validNumber = re.search(r"\d+", str(tableNumber))

    if not validNumber or int(tableNumber) < 0:
        return Response(message="Número no válido", data=None)

    if int(tableNumber) >= len(tables):
        return Response(message="No hay ninguna tabla con ese número", data=None)

    table = tables[int(tableNumber)]
    
    return rt(table)

#rts nombre: busca el nombre de la tabla o sistemas. Si solo hay una tabla con que contenga ese nombre, elegirá un elemento de ella. Ejemplo: "rts carta"
def rts(tables, searchString):

    matches = [s for s in tables if searchString.lower() in s.filename.lower()]

    if len(matches) == 0:
        return Response(message="No tables found", data=None)

    if len(matches) > 1:
        return Response(message="Multiple tables found", data=matches)

    if len(matches) == 1:
        response = rt(matches[0])

        if response.message == "":
            response.message = "Table found" + matches[0][2]

        return response

#r XdY: lanza X dados de Y caras cada uno. Ejemplo: "r 2d6" lanzará 2 dados de 6 caras
def r(tables, string):
    results = roll(string)
    minimum = None
    maximum = None
    total = 0

    if isinstance(results, int):
        return Response(message="", data=results)

    for dice in results:
        if minimum == None and maximum == None:
            minimum = dice
            maximum = dice
        
        if dice < minimum:
            minimum = dice
        if dice > maximum:
            maximum = dice

        total += dice

    return Response(message="", data=str(results) + "\n\nMinimum=" + str(minimum) + ", Maximum=" + str(maximum) + ", total=" + str(total))

#ayuda: Imprime esta ayuda
def ayuda():
    print("Comandos disponibles:\n")
    thismodule = sys.modules[__name__]
    funcionesModulo= inspect.getmembers(thismodule, inspect.isfunction)

    text = ""
    for funcion in funcionesModulo:
        ayuda = inspect.getcomments(funcion[1])
        if ayuda != None:
            text += "-" + ayuda.replace("#", "")

    return Response(message="", data=text)

def allowedFunction(my_function):
    allowed = inspect.getcomments(my_function) 
    
    if allowed != None:
        return True

    return False

def llamadaDinamica(tables, llamada):
    thismodule = sys.modules[__name__]
    funcionesModulo = inspect.getmembers(thismodule, inspect.isfunction)
    funcion = llamada.split(" ")[0]
    parametros = llamada.split(" ")[1:]
    parametros.insert(0, tables)

    if funcion in [x[0] for x in funcionesModulo]:
        try:
            to_be_executed = getattr(thismodule, funcion)

            if not allowedFunction(to_be_executed):
                raise TypeError

            return to_be_executed(*parametros)

        except TypeError:
            response = ayuda()
            response.message = "Orden incorrecta. Por favor, consulta la ayuda:"
            return response
    else:
        response = ayuda()
        response.message = "Orden no encontrada. Por favor, consulta la ayuda:"
        return response
