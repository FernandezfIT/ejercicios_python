# Una empresa de IoT está desarrollando un sistema de control a
# través de internet de las luces de las viviendas. De esta forma las
# personas podrán controlar sus luces desde cualquier lugar.
# Para el desarrollo de este objetivo, usted es contratado tal de que
# programe una aplicación con dicha funcionalidad.
# 
# Usted programa un menú con las distintas opciones que se
# aprecian en la imagen.
# La particularidad de este sistema es que con la misma opción se
# puede encender o apagar la luz, si se trata de una luz en
# particular, puesto que así lo solicitó la empresa.

print("Bienvenido al control de Luces IOT")
sw = 1
patio = True
sala = True
pasillo = True
jardin = True
while sw == 1:
    try:
        print("######## Menú Principal ########\n")
        print("1.- Encender/Apagar luces Patio (Alternado)")
        print("2.- Encender/Apagar luces Sala (Alternado)")
        print("3.- Encender/Apagar luces Pasillo (Alternado)")
        print("4.- Encender/Apagar luces Jardín (Alternado)")
        print("5.- Encender todo (Alternado)")
        print("6.- Apagar Todo (Alternado)")
        print("7.- Salir del Sistema\n")
        opcion = int(input("Ingrese la opción deseada >>"))
        if opcion == 1:
            if patio:
                print("El patio está apagado.")
                patio = False
            else:
                print("El patio está encendido.")
                patio = True
        elif opcion == 2:
            if sala:
                print("La sala está apagada.")
                sala = False
            else:
                print("La sala está apagadfa.")
                sala = True
        elif opcion == 3:
            if pasillo:
                print("El pasillo está apagado.")
                pasillo = False
            else:
                print("El pasillo está encendido.")
                pasillo = True
        elif opcion == 4:
            if jardin:
                print("El jardin está apagado.")
                jardin = False
            else:
                print("El jardín está encendido.")
                jardin = True
        elif opcion == 5:
            patio   = True
            sala    = True
            pasillo = True
            jardin  = True
            print("Todo está encendido.")
        elif opcion == 6:
            patio   = False
            sala    = False
            pasillo = False
            jardin  = False
            print("Todo está Apagado.")
        elif opcion == 7:
            print("Hasta Prondo...")
            break
        else:
            print("Opción Inválida")

    except ValueError:
        print("Ha ingresado una opción de menú inválida")