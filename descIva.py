"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

"""



def artDescuento (precio, descuento):
    precioConDescuento = precio - precio * descuento/100
    return precioConDescuento

def precioIva (precio, iva):
    precioConIva = precio + precio * iva/100
    return precioConIva

def cesto (dic_art, funcion, total = 0):
    for precio, descuento in dic_art.items():
        total += funcion (precio, descuento)
    return total

print (f"Monto total de la compra con Iva:\n {cesto({1000:10, 2000: 10, 3000:21 }, precioIva)}")
print (f"Monto total de la compra con descuentos:\n {cesto({1000:10, 2000: 10, 3000:21 }, artDescuento)}")

