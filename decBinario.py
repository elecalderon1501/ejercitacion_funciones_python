"""
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

"""



def decBinario (numero=0, cociente=0, numBinario=0, listaBin=[]):
    numero = int(input ("Ingrese un numero:\n"))
    while numero != 0:
        cociente = numero // 2
        numBinario = numero % 2
        listaBin.append(numBinario)
        numero = cociente
    return listaBin

print (f'El numero binario es:{decBinario()}')

def binDec (num_bin="", num_dec=0):
    num_bin= input ("Ingrese un numero binario:\n")

    for posicion, digito_bin in enumerate(num_bin[::-1]): 
        num_dec += int(digito_bin)*2**posicion
    return num_dec

print (f'El numero decimal es:{binDec()}')







