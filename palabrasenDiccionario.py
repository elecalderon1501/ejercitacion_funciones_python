def palabrasDiccionario(dic_palabras = {}, list_palabra=[],):
    frase = input ("Ingrese la frase:\n")
    list_palabra = frase.split()
    for palabra in list_palabra:
        if palabra in dic_palabras:
            dic_palabras[palabra]+=1
        else:
            dic_palabras[palabra]=1
    for campo, valor in dic_palabras.items():
        print (campo, valor)

print(palabrasDiccionario())