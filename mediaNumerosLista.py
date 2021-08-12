"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.

"""


def mediaLista (listaNum = [], contador=0, sumatoria=0):
    contador = int(input("Ingrese la cantidad de elementos que tendra la lista de numeros:\n"))
    for x in range(contador):
        valor = int (input("Ingrese un valor entero:"))
        listaNum.append(valor)
        sumatoria += valor
    return sumatoria/contador

print (mediaLista())
    

    