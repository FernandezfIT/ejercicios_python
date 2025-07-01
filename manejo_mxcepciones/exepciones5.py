# 🧩 Ejercicio Final: Cajero Automático
# 🎯 Objetivo:
# Simular un cajero automático simple. El programa debe:
# 
# Mostrar un saldo inicial fijo (ej: $1000).
# 
# Permitir al usuario hacer retiros de dinero.
# 
# Validar que:
# 
# El monto ingresado sea un número entero positivo.
# 
# El monto no sea mayor al saldo disponible.
# 
# Si el usuario intenta ingresar algo no numérico, debe mostrar un error sin cerrar el programa.
# 
# El programa termina si:
# 
# El usuario ingresa 0 como monto a retirar.
# 
# El saldo llega a 0.
# 
# 🧠 Detalles y sugerencias:
# Usa un while para repetir mientras el saldo sea mayor que 0.
# 
# Usa try-except para validar entradas incorrectas.
# 
# Resta el monto al saldo solo si es válido.
# 
# Muestra el saldo restante después de cada retiro.

retiro = 0
saldo = 1000000
print("Bienvenido al super Cajeto Automático")
while saldo > 0:
    print(f"Saldo Disponible: {saldo}")
    try:
        retiro = int(input("Ingrese monto a retirar (0 para SALIR): "))
        if retiro > 0:
            if retiro < saldo:
                saldo = saldo - retiro
                print(f"Retiro exitoso. Saldo restante: ${saldo}")
            else:
                print("No tiene saldo Suficiente")
        else:
            print("Error, debe ingresar un número válido!!!.")
    except ValueError:
        print("Error, debes ingresar un número válido.")

