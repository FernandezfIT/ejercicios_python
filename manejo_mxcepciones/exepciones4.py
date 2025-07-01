# 🟪 Ejercicio 4: Adivina el número (con control de errores)
# 🎯 Objetivo:
# Haz un programa que:
# 
# Elija un número secreto entre 1 y 10 (puede estar fijo para este ejercicio, por ejemplo, 7).
# 
# Le pida al usuario que adivine el número.
# 
# Permita 3 intentos.
# 
# Si el usuario ingresa algo que no sea un número, debe mostrar un mensaje de error y no debe contar como intento.
# 
# Si adivina el número, felicítalo y termina el programa.
# 
# Si no lo adivina en 3 intentos válidos, dile que ha perdido.
# 
# 🧠 Recomendaciones:
# Usa una variable para contar intentos válidos.
# 
# Usa un bucle while para repetir hasta 3 intentos válidos.
# 
# Usa try-except para validar la entrada.
# 
# Usa if para comprobar si adivinó el número.

import random

numero_secreto = random.randint(1,10)
respuesta = 0
cantIntentos = 3


print("Bienvenido")
print("Hay un número secreto!!!")
while cantIntentos > 0:
    try:
        respuesta = int(input("Intenta adivinar: "))
        if respuesta != numero_secreto:
            cantIntentos = cantIntentos - 1
            if cantIntentos > 0:
                print(f"UY!! Has fallado. Te quedan {cantIntentos}")
            else:
                print("Has perdido")
                print(f"El número era {numero_secreto}")
        else:
            print("FELICIDADES, Has acertado.")
            cantIntentos = 0

    except ValueError:
        print("Debes ingresar un valor válido")







