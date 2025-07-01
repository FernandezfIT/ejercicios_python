usuario="Tienda"
clave="ABC"
usuario_ok=False # Bandera que sirve para controlar si el usuario fue ingresado correctamente ingresa al menu. 
                 #De lo contrario pued usar una función exit(), que me saca del programa forzadamente, en la línea 30, en vez de break.
intentos = 1 # Control de intentos de ingreso de usuario y contraseña.

total1 = 0 # Variable que se utiliza para calcular el total de la compra de combo 1.
total2 = 0 # Variable que se utiliza para calcular el total de la compra de combo 2.
total3 = 0 # Variable que se utiliza para calcular el total de la compra de combo 3.
total4 = 0 # Variable que se utiliza para calcular el total de la compra de combo 4.
totalfinal = 0 # Variable que se utiliza para calcular el total final de la compra.
nro1 = 0 # Variable que se utiliza para controlar la cantidad de combos 1 que se compran.
nro2 = 0 # Variable que se utiliza para controlar la cantidad de combos 2 que se compran.
nro3 = 0 # Variable que se utiliza para controlar la cantidad de combos 3 que se compran.
nro4 = 0 # Variable que se utiliza para controlar la cantidad de combos 4 que se compran.
pago = 0 # Variable que se utiliza para controlar el medio de pago de la compra (1 Efectivo o 2 Tarjeta).

while intentos < 4:
    nombre = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    if (nombre == usuario and contraseña.upper() == clave): # Este método upper que convierte a mayúscula está demás, solo es una forma de mostrar que todo lo ingresado en variable string clave se convertirá a mayúscula.
        print("Usuario y contraseña correctos")
        usuario_ok=True # Si el usuario y contraseña son correctos, la bandera se convierte en mayúscula, y así permitimos que entre al menú
        intentos = 4 # Si el usuario y contraseña son correctos, el número de intentos queda en 4 para salir del ciclo en forma natural.
    else:
        print("Error de ingreso de usuario y/o contraseña")
        intentos += 1 
        if intentos == 4:
            print("Se le acabaron los intentos")
            break # Si se acaban los intentos, siendo el usuario y/o contraseña incorrectos, se sale del Ciclo forzadamente.

if usuario_ok: # Si la bandera (variable usuario_ok) es True, el usuario y contraseña son correctos, y se puede ingresar al menú.
    while True:
        print ("_"*80)
        print("\t\t\t\t\tMenu")
        print ("_"*80)
        print("1.combo pollo papas y bebida Valor                                    $ 5.500")
        print("2.Combo crispí papa fritas bebida Valor                               $ 3.990")
        print("3.Combo deluxe papas bebida Valor                                     $ 2.990")
        print("4.Combo box con 6 trozos de pollo papas bebida Valor                  $ 6.990")
        print("5.Medios de Pago Efectivo o Tarjeta")
        print("6.Emite Boleta")
        print("7.Salir")
        try:
            opcion = int(input("Ingrese la opcion que quiere comprar: "))
        except ValueError:
            print("Dato ingresado no es valido")
            continue
        match opcion:

                case 1:
                    nro1 += 1
                    total1 += 5500
                case 2:
                    nro2 += 1
                    total2 += 3990
                case 3:
                    nro3 += 1
                    total3 += 2990
                case 4:
                    nro4 += 1
                    total4 += 6990
                case 5:
                    while (pago != 1 and pago != 2): # Mientras el pago no sea 1 (Efectivo) o 2 (Tarjeta) no saldrá del ciclo while.
                        try:
                            pago = int(input("Ingrese metodo de pago. 1 EFECTIVO, O 2 TARJETA: "))
                        except ValueError:
                            print("Dato ingresado no Válido, vuelva a intentar")
                            pago = 0
                            continue # Si el dato ingresado no corresponde a un número entero, se vuelve al while, para pedir el pago.
                        if (pago < 1 or pago > 2): # Si el pago no es 1 o 2, se vuelve al while, para pedir el pago.
                            print("Metodo de pago incorrecto, vuelva a intentar.")


                case 6:
                    totalfinal = total1 + total2 + total3 + total4


                    print("\n------------------------------------------------------------------")
                    print("                               BOLETA                               ")
                    print("\n------------------------------------------------------------------")

                    print("                         \t⣿⣿⣿⣿⣿⣿⣿⡿⢟⣋⣭⣥⣭⣭⣍⡉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿") #Esta parte de la boleta me la envió un alumno.
                    print("                         \t⣿⣿⣿⣿⣿⡏⠁⠠⠶⠛⠻⠿⣿⣿⣿⣿⣷⡄⠄⠄⠄⠄⠉⠻⢿⣿⣿⣿⣿⣿")
                    print("                         \t⣿⣿⣿⣿⠟⠄⢀⡴⢊⣴⣶⣶⣾⣿⣿⣿⣿⢿⡄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿")
                    print("                         \t⣿⣿⡿⠁⠄⠙⡟⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣎⠃⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿")
                    print("                         \t⣿⡟⠄⠄⠄⠄⡇⠰⠟⠛⠛⠿⠿⠟⢋⢉⠍⢩⣠⡀⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿")
                    print("                         \t⣿⠁⠄⠄⠄⠄⠰⠁⣑⣬⣤⡀⣾⣦⣶⣾⣖⣼⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿")
                    print("                         \t⡏⠄⠄⠄⠄⠄⠄⠄⠨⣿⠟⠰⠻⠿⣣⡙⠿⣿⠋⠄⢀⡀⣀⠄⣀⣀⢀⣀⣀⢸")
                    print("                         \t⡇⠄⠄⠄⠄⠄⠄⠄⠄⣠⠄⠚⠛⠉⠭⣉⢁⣿⠄⢀⡿⢾⣅⢸⡗⠂⢿⣀⡀⢸")
                    print("                         \t⡇⠄⠄⠄⠄⠄⠄⠄⠄⠘⢧⣄⠄⣻⣿⣿⣾⠟⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸")
                    print("                         \t⣿⠄⠄⠄⠄⠄⠄⠄⠄⢠⡀⠄⠄⣿⣿⠟⢁⣴⣿⢸⡄⠄⢦⣤⣤⣤⣤⣄⡀⣼")
                    print("                         \t⣿⣧⠄⠄⠄⠄⠄⠄⢠⡸⣿⠒⠄⠈⠛⠄⠁⢹⡟⣾⡇⠄⠈⢿⣿⣿⣿⣿⣿⣿")
                    print("                         \t⣿⣿⣧⣠⣴⣦⠄⠄⢸⣷⡹⣧⣖⡔⠄⠱⣮⣻⣷⣿⣿⠄⠄⠘⣿⣿⣿⣿⣿⣿")
                    print("                         \t⣿⣿⣿⣿⣿⡇⠄⠄⠸⠿⠿⠚⠛⠁⠂⠄⠉⠉⡅⢰⡆⢰⡄⠄⠘⣿⣿⣿⣿⣿")
                    print("                         \t⣿⣿⣿⣿⣿⣷⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⣷⠘⣧⣠⣾⣿⣿⣿⣿⣿")
                    print("                         \t⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣄⣀⣀⡀⠄⣀⣀⣹⣦⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿")
                    print("\n------------------------------------------------------------------")
                    print("\n------------------------------------------------------------------")

                    if nro1 > 0:
                        print(f"{nro1} Pollo + Papas + Bebida               ${total1}")
                    if nro2 > 0:
                        print(f"{nro2} Crispy + Papas + Bebida              ${total2}")
                    if nro3 > 0:
                        print(f"{nro3} Combo Deluxe                         ${total3}")
                    if nro4 > 0:
                        print(f"{nro4} Combo Box                            ${total4}")

                    print("\n----------------------------------------------------")
                    if pago == 1:
                        print("\n\t\t\tPAGO : Efectivo")
                    elif pago == 2:
                        print("\n\t\t\tPAGO : Tarjeta")
                    
                    print("\n----------------------------------------------------")
                    print(f"\n Total Boleta ${totalfinal}")
                    print("\n GRACIAS POR PREFERIRNOS")
                case 7:
                    print("\n----------------------------------------------------")
                    print("       Saliendo del Programa... Gracias, hasta pronto  ")
                    break
                case _:
                    print("Por favor ingrese una opción entre 1 y 7")
else:
     print("       Saliendo del Programa... Gracias, hasta pronto  ")


