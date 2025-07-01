# Haz un programa que pida dos números y muestre la división del primero entre el segundo. Maneja estos errores:
# 
# División por cero
# 
# Entrada que no sea número


try:
    numero1 = int(input("Ingresa el 1er número"))
    numero2 = int(input("Ingresa el 2do número"))
    resultado = numero1/numero2
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("No puedes dividir por cero.")
except ValueError:
    print("Debes ingresar un número válido.")