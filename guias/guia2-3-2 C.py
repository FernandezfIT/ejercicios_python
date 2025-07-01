# Devolucion Dinero

user    = input("Ingrese su user")
pwd     = input("Ingrese su pass")

if user == "duoc" and pwd == "123duoc":
    valorDev = int(input("Bienvenido, Ingrese el valor a devolver:"))
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolucion de dinero")
    else:
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print("Error de contraseña")