

costo_compra    = 100000
bandera         = True
while bandera:
    print("************** MENÚ **************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con Paypal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except ValueError:
        print("Ha ingresado un dato inválido. Recuerde que debe ingresar un número entre 1 y 5")

    if opcion == 1:
        nro_tarjeta     = int("Ingrese número tarjeta de crédito: ")
        nombre          = input("Ingrese nombre Titular: ")
        mes_vencimiento = int(input("Ingrese mes de vencimiento: "))
        ano_vencimiento = int(input("ingrese año de vencimiento: "))

        print("Detalle de la compra")
        print(f"Costo de la compra: ${costo_compra}")
        print(f"Número de tarjeta: {nro_tarjeta}")
        print(f"Nombre del Titular: {nombre}")
        print(f"Mes y año de vencimiento: {mes_vencimiento}/{ano_vencimiento}")
    elif opcion == 2:
        usuario_paypal  = int("Ingrese nombre de usuario: ")
        contrasena      = "1234"
        if usuario_paypal == "Usuario" and contrasena == "1234":
            print("Detalle compra.")
            print(f"Costo de la compra: ${costo_compra}")
            print(f"Usuario: {usuario_paypal}")
            print("Contraseña correcta.")
        else:
            print("Usuario o contraseña incorrectos.")
    elif opcion == 3:
        print("Datos para trasnferencia:")
        print("Banco: Banco Santander")
        print("Tipo de cuenta: Corriente")
        print("Nro de cuenta: 1453- 90000")
        print("Titular: Dulce Confite Ltda.")
        print("RUT: 76.858.374-9")
        