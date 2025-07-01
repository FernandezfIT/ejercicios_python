# ir al kentuky y hacer un programa simple con menú
# que muestre los combos con control de usuario
# y con 2 metodo de pago posibles

# combos o promociones
# validacion de usuarios
# con 3 intentos
# validacion de exepciones
# con 
# combo1 pollo papa bibia   $5500
# combo2 crispy papa bibia  $3990
# combo3 deluxe papa bibia  $2990
# combo4 trozo de pollo papa bebia $6990

# Puede pagar con efectivo o debito
# Emitir la boleta por el total

intentos       = 3
combo1_detalle = "Pollo + Papas + Bebida"
combo2_detalle = "Pechuga Crispy + Papas + Bebida"
combo3_detalle = "Box Deluxe + Papas + Bebida"
combo4_detalle = "Tiras de Pollo + Papas + Bebida"
contador_combo1 = 0
contador_combo2 = 0
contador_combo3 = 0
contador_combo4 = 0
combo1_precio  =  5500
combo2_precio  =  3990
combo3_precio  =  2990
combo4_precio  =  6990
menu_Combo     =  1
menu_pago      =  1
total_final    =  0



print("Bienvenido al Kentucky!")
print("_" * 20) 
while intentos > 0:  ### >>>> 1er while valida usuario y contraseña
    usuario     = input("Ingrese su usuario: ")
    clave       = input("Ingrese su contraseña: ")
    print(usuario, "-", clave)
    if (usuario == "Felipe" and clave == "felipe"):
        ### Si usuario y contraseña es correcto se ejecuta esta parte
        ### Que muestra el nobre del usuario y las opciones dispoibles junto a su precio.
        print(f"Bienbenido {usuario}!!")
        print("¿Que desea ordenar?:")
        print(f"Combo 1: {combo1_detalle} \t\t/\t VALOR: ${combo1_precio}")
        print(f"Combo 2: {combo2_detalle} \t/\t VALOR: ${combo2_precio}")
        print(f"Combo 3: {combo3_detalle} \t\t/\t VALOR: ${combo3_precio}")
        print(f"Combo 4: {combo4_detalle} \t/\t VALOR: ${combo4_precio}")
        print(f"Ingrese 1, 2, 3 o 4 para elegir Combo.")
        print(f"Ingrese 0 cuando esté listo para realizar el pago.")

                ### MENU COMBO ###

        while menu_Combo != 0: ### >>> Este while permite que se pueda elegir más de una opcion
                               ### >>> y se vayan agregando al final
            try:  ### Este try valida el ingreso de la opcion de combo
                menu_Combo = int(input("> "))
                if menu_Combo == 1:
                    total_final += combo1_precio
                    contador_combo1 += 1 ### Este cnotador permite que en el detalle de la boleta aparezca
                                         ### Cuantas veces se eligio el combo indicado.
                    print(f"Subtotal: ${total_final}")
                    print("Agregue otra Opción o presione 0 para pasar a pagar.")
                elif menu_Combo == 2:
                    total_final += combo2_precio
                    contador_combo2 += 1
                    print(f"Subtotal: ${total_final}")
                    print("Agregue otra Opción o presione 0 para pasar a pagar.")
                elif menu_Combo == 3:
                    total_final += combo3_precio
                    contador_combo3 += 1
                    print(f"Subtotal: ${total_final}")
                    print("Agregue otra Opción o presione 0 para pasar a pagar.")
                elif menu_Combo == 4:
                    total_final += combo4_precio
                    contador_combo4 += 1
                    print(f"Subtotal: ${total_final}")
                    print("Agregue otra Opción o presione 0 para pasar a pagar.")
                else:
                    print("Opción inválida.")
                    print(f"Subtotal: ${total_final}")
                    print("Agregue otra Opción o presione 0 para pasar a pagar.")
            except ValueError:
                print("Opción Inválida.")
        print("Pasar a pagar.")
        print(f"SUBTOTAL: ${total_final}")
        print("Elija método de pago: ")
        print("1.-Tarjeta.")
        print("2.-Efectivo.")
        print("0.- Para cancelar venta.")
        intentos = 0  ### Cambia la cant de intentos a 0 para no volver a iniciar el ingreso de usuario

            ### MENU PAGO ###

        while menu_pago != 0: ### While para que en caso de ingresar una opcion inválida vuelva a preguntar
            try:
                menu_pago = int(input("> "))
                if menu_pago == 1:
                    ##### FORMATEO DE BOLETA #####
                    print("\t\t###KFC###")
                    print("_"*40)
                    print("\t\t###DETALLE###")
                    if(contador_combo1 > 0):
                        print(f"Combo 1: {combo1_detalle} \t\t/\t VALOR: ${combo1_precio}")
                        print(f"\t\t\t\t\t X {contador_combo1}\tSUBTOTAL\t ${contador_combo1 * combo1_precio}")
                    if(contador_combo2 > 0):
                        print(f"Combo 2: {combo2_detalle} \t/\t VALOR: ${combo2_precio}")
                        print(f"\t\t\t\t\t X {contador_combo2}\tSUBTOTAL\t ${contador_combo2 * combo2_precio}")
                    if(contador_combo3 > 0):
                        print(f"Combo 3: {combo3_detalle} \t\t/\t VALOR: ${combo3_precio}")
                        print(f"\t\t\t\t\t X {contador_combo3}\tSUBTOTAL\t ${contador_combo3 * combo3_precio}")
                    if(contador_combo4 > 0):
                        print(f"Combo 4: {combo4_detalle} \t/\t VALOR: ${combo4_precio}")
                        print(f"\t\t\t\t\t X {contador_combo4}\tSUBTOTAL\t ${contador_combo4 * combo4_precio}")
                    print("_" * 40)
                    print("Método de pago:\t\t Débito")
                    print(f"TOTAL:\t\t\t\t\t${total_final}")
                    print("\n\n\n\n")
                    menu_pago = 0
                    
                elif menu_pago == 2:
                    print("\t### KFC ###")
                    print("_"*40) ### El *40 hace que _ se repita 40 veces
                    print("\t### DETALLE###")
                    if(contador_combo1 > 0):
                        print(f"Combo 1: {combo1_detalle} \t\t/\t VALOR: ${combo1_precio}")
                        print(f"\t\t\t X {contador_combo1}\tSUBTOTAL\n ${contador_combo1 * combo1_precio}")
                    if(contador_combo2 > 0):
                        print(f"Combo 2: {combo2_detalle} \t/\t VALOR: ${combo2_precio}")
                        print(f"\t\t\t X {contador_combo2}\tSUBTOTAL\t ${contador_combo2 * combo2_precio}")
                    if(contador_combo3 > 0):
                        print(f"Combo 3: {combo3_detalle} \t\t/\t VALOR: ${combo3_precio}")
                        print(f"\t\t\t X {contador_combo3}\tSUBTOTAL\t ${contador_combo3 * combo3_precio}")
                    if(contador_combo4 > 0):
                        print(f"Combo 4: {combo4_detalle} \t/\t VALOR: ${combo4_precio}")
                        print(f"\t\t\t X {contador_combo4}\tSUBTOTAL\t ${contador_combo4 * combo4_precio}")
                    print("_" * 40) 
                    print("Método de pago:\t\t Efectivo")
                    print(f"TOTAL:\t\t\t\t\t${total_final}")
                    print("\n\n\n\n")
                    
                    menu_pago = 0
                elif menu_pago == 0:
                    print("FINALIZANDO.")
            except ValueError:
                total_final = 0
                print("Opción Invalida")
        


    else:   ##### >>>> Si se equivoca en usuario o contraseña se ejecuta este código
        print("Usuario o Contraseña Incorrectos")
        intentos = intentos - 1
        if(intentos > 0):
            print(f"Quedan {intentos} intentos!!")
        else:
            print("Usuario no identificado, transaccion inválida.")

if total_final == 0:
    print("Has Cancelado la compra.")


