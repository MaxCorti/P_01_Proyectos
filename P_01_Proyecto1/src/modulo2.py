from datetime import datetime


def convertir_entero(numero):
    var = int(numero)
    return var

def convertir_float(numero):
    var = float(numero)
    return var

def covertir_fechas(fecha):
    var = datetime.strptime(fecha, "%d/%m/%Y").date()
    return var

def convertir_boole(respuesta):
    respuesta = False
    if respuesta == "SI":
        respuesta = True
    return respuesta