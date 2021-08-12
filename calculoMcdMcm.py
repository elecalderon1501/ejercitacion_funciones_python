"""
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

"""
num1 = int (input ("Ingrese el primer numero:\n" ))
num2 = int (input( "Ingrese el segundo numero:\n"))

def calculoMcd (num1, num2):   
        a=max (num1, num2)
        b=min (num1, num2)
        
        while b != 0:
            a,b = b, a % b
            return a


def calculoMcm (num1, num2):
    x = max(num1, num2)
    while True:
        if (x % num1 ==0) and (x % num2 ==0):
            return x
        x += 1 
    
try:
    print (f"El MCD es: {calculoMcd(num1, num2)}")
except ZeroDivisionError:
    print ("No se puede dividir por cero")
 
try:
    print (f"El MCM es: {calculoMcm(num1, num2)}")
except ZeroDivisionError:
    print ("No se puede dividir por cero")
