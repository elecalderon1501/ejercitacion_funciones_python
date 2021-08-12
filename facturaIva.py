"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""


def calculoFact(montoFact=0, iva = 21): 
    montoFact = float(input("Ingrese el monto de la factura:\n"))
    iva = float(input("Ingrese el porcentaje del IVA a aplicar:\n"))
    if iva == 21:
        return montoFact + (montoFact * (21/100))
    else:
        return montoFact + (montoFact * (iva/100))


print (f'El total de la factura con IVA es: {calculoFact()}')



