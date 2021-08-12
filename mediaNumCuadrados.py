""" 
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

"""
def mediaCuadrados(listaNum = [], contador=0, sumatoria=0):
    contador = int(input("Ingrese la cantidad de elementos que tendra la lista:\n"))
    for i in range(contador):
        valor = int (input("Ingrese un valor:\n"))
        valor = valor**2
        listaNum.append(valor)
    return listaNum

print (f"Esta lista tiene los numeros al cuadrado: {mediaCuadrados()}")