import os

#### Diccionarios ####
contactos = {}

#### FUNCIONES ####

# Imprimir menú

def imprimir_menu():
    print("Seleccione una Opción:")
    print("1.- Agregar Contacto.")
    print("2.- Buscar Contacto.")
    print("3.- Editar Contacto.")
    print("4.- Eliminar Contacto.")
    print("5.- Cerrar Agenda.")

# Salida

def salida(bandera):
    try:
        confirmacion = int(input("¿Seguro que desea Salir?\n1.-Si\n2.-No\n>> "))
    except:
        print("Opción ingresada incorrecta.\nVolviendo al menú principal")

    else:
        if confirmacion == 1:
            bandera = False
            print("Ha confirmado la salida")
            print("Cerrando la agenda...")
            print("Adiós.")
        elif confirmacion == 2:
            print("Ha cancelado la salida.\nVolviendo al menú principal.")
        else:
            print("Ha ingresado una opción fuera del rango permitido.\nVolviendo al menú principal.")

    return bandera

# 1.- Agregar Contacto

def agregar_contacto(contactos):
    nombre = input("Ingrese nombre de contacto: ")
    numero = input("Ingrese número de teléfono: ")
    correo = input("Ingrese correco de contacto: ")
    contactos.update({nombre:{numero:correo}})
    print(f"El contacto {nombre} ha sido agregado correctamente\n-Número: {numero}\n-Correo {correo}")

# 2.- Buscar Contacto

def buscar_contactos(contactos):
    busqueda = input("Ingrese nombre de contacto que desea Buscar:\n>>")
    for clave in contactos:
        if busqueda == clave:
            print(f"Datos de {busqueda}: ")
            if (len(contactos[clave]) > 1):
                for clave2 in (contactos[clave]):
# 3.- Editar Contacto

# 4.- Eliminar contacto

### Código MAIN ###

bandera = True

print("Bienvenido a tu Agenda Personal")
while bandera:
    print("\n")
    imprimir_menu()
    try:
        opcion = int(input(">> "))
    except ValueError:
        print("Ha ingresado una opcion Inválida.\nIntente Nuevamente.")
    else:
        if opcion == 1:
            print("Agregar Contacto")
            agregar_contacto(contactos)
        elif opcion == 2:
            print("Buscar Contacto")
        elif opcion == 3:
            print("Editar Contacto")
        elif opcion == 4:
            print("Eliminar Contacto")
        elif opcion == 5:
            print("Salir")
            bandera = salida(bandera)