# Un sistema que consulte la edad, y de acuerd a ella indique si la persona es mayor de edad o no

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
elif edad < 18 and edad >= 0:
    print("Usted es menor de edad")
else:
    print("Edad ingresada no es valida")