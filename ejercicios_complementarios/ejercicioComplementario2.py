# La empresa de seguridad “Seguronet” está desarrollando un sistema para facilitar la creación de contraseñas de sus usuarios.
# La idea central es pedir una cierta cantidad de letras o dígitos de información que maneja una persona y luego mezclarlas para generar opciones de contraseña.
# 
# 
# Un ejemplo de la utilización se visualiza en la siguiente imagen:
# 
# Elija la opción correcta:
# 
#

print("Por favor ingrese los siguientes datos: ")
nom = input("Las 2 primeras letras de su primer nombre: ")
ape = input("Las 2 primeras letras de su segundo apellido: ")
rut = input("Los 2 primeros numeros de su rut: ")
mes = input("Las 3 primeras iniciales del mes de su nacimiento: ")
ciu = input("Las 2 últimas letras de la ciudad donde vive: ")

opcion1 = nom + ape + rut + mes + ciu 
opcion2 = ape + rut + mes + ciu + nom
opcion3 = rut + mes + ciu + nom + ape 
opcion4 = mes + ciu + nom + ape + rut
opcion5 = ciu + nom + ape + rut + mes

print("")
print(f"La opción 1 de contraseña es: {opcion1}")
print(f"La opción 2 de contraseña es: {opcion2}")
print(f"La opción 3 de contraseña es: {opcion3}")
print(f"La opción 4 de contraseña es: {opcion4}")
print(f"La opción 5 de contraseña es: {opcion5}")



