# Ingreso de liquidacion de Sueldo
nom             = input("Ingrese nombre Empleado: ")
rut             = input("Ingrse RUT Empleado: ")
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
valorHora       = int(input("Ingrese el valor hroa del empleado: "))

colacion        = 5500
movilizacion    = 3000
resultado       = (valorHora * horasTrabajadas) + colacion + movilizacion

print(f"-----LIQUIDACION EMPLEADO-----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACION: {movilizacion}")
print(f"ALIMENTACION: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")

