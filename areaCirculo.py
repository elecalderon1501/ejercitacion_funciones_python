"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función. 
areaCirculo = π r 2 

"""

PI = 3.1415926535
radio = float (input ("Ingrese el radio:\n"))
altura = float (input("Ingrese la altura del cilindro:\n"))

def CalculoAreaCirculo ():
    return PI * (radio**2)
    

def CalculoVolCilindro ():
    return CalculoAreaCirculo () * altura

print ("El area del circulo es:") 
print (CalculoAreaCirculo())

print ("El volumen del cilindro es:") 
print (CalculoVolCilindro())




