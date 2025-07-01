#ValorNeto de un producto
producto        = input("Ingrese el nombre del Producto:")
valorProducto   = int(input("Ingrese valor del Producto: "))
valorNeto       = float(0.81)
valorSinIVA     = float(valorProducto * valorNeto)

print(f"----Detalle del Producto----")
print(f"NOMBRE PRODUCTO {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIVA}")

#
#   ¿POR QUE SE DEBE USAR TIPO FLOAT PARA CALCULAR EL IVA?
#           R: porque al calculo del iva genera resultados con decimales o de coma flotante (float)
