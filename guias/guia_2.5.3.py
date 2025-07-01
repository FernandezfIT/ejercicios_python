# Descripción de la Actividad:
# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
#   Las opciones disponibles deben estar construidas de la siguiente forma:
#       1. Pago de Tarjeta de Crédito:
#           a. El usuario comienza con una deuda de $100.000
#           b. El usuario puede ingresar un monto para realizar un pago en la
#              tarjeta de crédito.
#           c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
#           d. Se debe verificar que el monto a pagar no exceda el saldo actual de
#              la tarjeta.
#           e. Al pagar el sistema debe descontar de la deuda total
#           f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
#              saldo de la tarjeta.
#       2. Simulación de Compras:
#           a. El usuario puede simular realizar un número ilimitado de compras.
#           b. Para cada compra, se solicita al usuario ingresar el monto de la
#              compra. El programa suma los montos de cada compra.
#           c. Se verifica que el monto de la compra sea mayor o igual a cero.
#           d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
#              iteración del bucle for.
#       3. Salir:
#           a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
#   A considerar:
#       1. Manejo de Errores:
#           a. Se utilizan bloques try y except para manejar posibles errores al
#              ingresar datos, validar valores no numéricos y errores inesperados.

deuda = 100000
sw = 1
print("Bienvenido al banco.")
while sw == 1:
    try:
        print("\n\n\n")
        print("########## Menú Principal ##########:")
        print("1.- Pago tartjeta de Crédito.")
        print("2.- Simulación Compra.")
        print("3.- Salir")
        opcion = int(input("Seleccione una Opción >"))
        if opcion == 1:
            print("\n\n\n")
            print("########## PAGO DE TARJETA DE CRÉDITO ##########")
            print(f"Tu deuda actual es: ${deuda}.")
            abono = int(input("¿Cuanto desea abonar?\n>> $"))
            if abono > 0 and abono < deuda:
                deuda -= abono
                print(f"El mondo adeudado acutualmente es de: ${deuda}")
            else:
                print("No se puede abonar el saldo indicado. Valor Incorrecto.")
        elif opcion == 2:
            print("\n\n\n")
            print("########## SIMULACIÓN de COMPRA ##########")
            cant_compras = int(input("Ingrese cantidad de compras a simular: \n>>>"))
            for i in range(cant_compras):
                monto_compras = int(input(f"Ingrese el monto de la compra {i+1}: $"))
                if monto_compras > 0:
                    deuda += monto_compras
                    print(f"Tu deuda total es: ${deuda}")
                else:
                    print("Monto inválido. Intente nuevamente")
                    i -=1
        elif opcion == 3:
            print("\n\n\n")
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida")

    except ValueError:
        print("Ha ingresado una opción inválida.")

        