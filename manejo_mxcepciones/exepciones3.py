# Objetivo: Pregunta al usuario cuántas horas trabajó esta semana y cuánto gana por hora. Luego muestra el sueldo. Pero:
# 
# Si el usuario escribe algo que no es número, muestra un error.
# 
# Si el número de horas es negativo o mayor a 168 (máximo en una semana), muestra otro error.
# 
# 💡 Sugerencia:
# Usa try-except para validar entradas.
# 
# Usa if para verificar si el número es válido (ej. horas >= 0 and horas <= 168).

horas = 0
valorHora = 0
sueldo = 0

try:
    horas = int(input("Igrese cantidad de horas trabajadas: "))
    if 0 <= horas <= 168:
        valorHora = int(input("Ingrese valor de la hora: $"))
        sueldo = horas * valorHora
        print(f"Su sueldo es: {sueldo}")
    else:
        print("Cantidad de horas inválidas")

except ValueError:
    print("Error al ingresar valor.")