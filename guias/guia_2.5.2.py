#   EJERCICIO 2
#   Construir el siguiente programa con las siguiente reglas de negocio:
#       • Inicio del Programa:
#           o El programa comienza inicializando una variable sw en 1, indicando
#             que el sistema está activo, puede utilizar también “while true:”
#       • Menú Principal:
#           o Se presenta un menú al usuario con las siguientes opciones:
#             ▪ Ver mi Saldo
#             ▪ Retirar Dinero
#             ▪ Salir
#             • Selección de Opción:
#           o Se le pide al usuario que seleccione una opción ingresando un
#             número.
#             • Validación de Entrada:
#           o Se verifica que la opción ingresada esté en el rango de 1 a 3.
#             • Acciones según la Opción:
#             • Si la opción es 1:
#               a. Se imprime el mensaje "Tiene un saldo de $500000".
#               b. Se solicita al usuario que presione 1 para volver atrás o 2 para
#                  salir.
#               c. Si el usuario presiona 2, se imprime "Cierre de sesión exitoso,
#                  adiós" y se sale del sistema.
#             • Si la opción es 2:
#               a. Se imprime "Transferencia realizada".
#               b. Se solicita al usuario que presione 1 para volver atrás o 2 para
#                  salir.
#               c. Si el usuario presiona 2, se imprime "Cierre de sesión exitoso,
#                  adiós" y se sale del sistema.
#             • Si la opción es 3:
#               a. Se imprime "Cierre de sesión exitoso, adiós".
#               b. Se cambia el valor de sw a 0, saliendo así del bucle principal y
#                  terminando el programa, también se puede utilizar el comando
#                  “break”
#             • Manejo de Errores:
#           o Se utiliza un bloque try-except para manejar errores durante la
#             ejecución, mostrando un mensaje en caso de ingreso incorrecto.
#             • Salir del Programa:
#           o Cambiando el valor de sw a 0, se sale del bucle principal y termina el
#             programa.
#             • Confirmación del Usuario:
#           o Después de realizar ciertas acciones (ver saldo o transferir dinero),
#             se solicita al usuario que confirme si desea volver atrás o salir

saldo = 500000
sw = 1
print("Bienvenido al Banco.")
while sw == 1:
    try:
        print("Seleccione una opción:")
        print("1.- Ver mi Saldo")
        print("2.- Retirar Dinero.")
        print("3 .- Salir.")
        opcion = int(input("Selección de Opción >"))
        if opcion == 1:
            print(f"Tiene un saldo de ${saldo}")
            print("Presione \n1.- Para continuar.\n2.- Para Salir")
            continuacion = int(input(">"))
            if continuacion == 1:
                continue
            elif continuacion == 2:
                print("Cierre de sesión exitoso, adiós.")
                sw = 0
                break
        elif opcion == 2:
            print("Trasnferencia Realizada.")
            print("Presione \n1.- Para continuar.\n2.- Para Salir")
            continuacion = int(input(">"))
            if continuacion == 1:
                continue
            elif continuacion == 2:
                print("Cierre de sesión exitoso, adiós.")
                sw = 0
                break
        elif opcion == 3:
            print("Cierre de programa exitoso. Adiós")
            break
        else:
            print("Debe ingresar una opción dentro de los valores indicados (1 - 2 - 3)")       
    except ValueError:
        print("Ha ingresado un dato inválido al momento de elegir opción.")
