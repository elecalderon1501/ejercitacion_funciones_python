"""
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
Var (X) = (x1 – x’)2 + (x2 – x’)2 + … + (xn – x’) / N
"""
from statistics import mean, variance
import statistics


def mediaLista (listaNum = [], contador=0, sumatoria=0, media = 0):
    contador = int(input("Ingrese la cantidad de elementos que tendra la lista de numeros:\n"))
    for x in range(contador):
        valor = int (input("Ingrese un valor entero:"))
        listaNum.append(valor)
    media = statistics.mean (listaNum)
    varianza = statistics.variance (listaNum)
    desvTipica = statistics.stdev(listaNum)

    diccionario = {
        'Media' : media,
        'Varianza' : varianza,
        'Desviacion' : desvTipica

    }
    print (diccionario) 

mediaLista(listaNum =[])