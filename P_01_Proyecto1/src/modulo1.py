from collections import namedtuple
import csv
from datetime import datetime
from modulo2 import convertir_entero, convertir_float, covertir_fechas, convertir_boole
Autobuses = namedtuple("autobus", "matricula,fabricante,inicio,capacidad,asientos,kilometros,articulado")

def lee_datos_del_fichero(ruta):
    res=[]
    with open(ruta, "rt", encoding="utf-8") as f:
        lector=csv.reader(f, delimiter=",")
        next(lector)
        for matricula, fabricante, inicio, capacidad, asientos, kilometros, articulado in lector:
            inicio = covertir_fechas(inicio)
            capacidad =convertir_entero(capacidad)
            asientos = convertir_entero(asientos)
            kilometros = convertir_float(kilometros)
            articulado =convertir_boole(articulado)
            tupla=Autobuses(matricula, fabricante, inicio, capacidad, asientos, kilometros, articulado)
            res.append(tupla)
            


            
    return res

