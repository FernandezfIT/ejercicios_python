#
# 
#  Reordenar los códigos con el fin que el sistema valide:
#   Rango de edad entre 0 y menor 18 años. Descuento de 50%
#   Rango de edad 18 y menor que 30 años. Descuento de 20%
#   Mayor o igual a 60 años. Descuento de 90%
# 
# #

# Descuento por edad
edad = int(input("Ingrese su edad."))

if edad > 0 and edad < 18:
    print(f"Edad {edad} tiene 50% de descuento ")
elif edad >= 18 and edad < 30:
    print(f"Edad {edad} tiene 20% de descuento ")
elif edad >= 60:
    print(f"Edad {edad} tiene 90% de descuento ")
else:
    print(f"Edad {edad} No aplica descuento ")