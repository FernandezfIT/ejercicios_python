# Pide al usuario que ingrese 5 números y guárdalos en una lista. 
# Si se ingresa un valor no numérico, muestra un mensaje y repite la solicitud para ese número.
#
# Sugerencia: usa un bucle for con range(5).


cantNumeros = 0
numero = 0
while cantNumeros < 5:
    try:
        numero = int(input("Ingrese un numero: "))
        cantNumeros = cantNumeros + 1
    except ValueError:
        print("Ingrese un número válido")
