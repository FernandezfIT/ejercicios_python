# El almacén, “Diego’s” en su afán de incorporar nuevas tecnologías en sus procesos de negocio, le solicita un prototipo de sistema que le per-mita ingresar los datos de 3 ventas del almacén.
# 
# Antes de usted, el almacén le había pedido a un informático comenzar a hacer el sistema, pero este lo dejó botado.
# Ahora los dueños desean que usted siga con el desarrollo.
# 
# 
print("Ingresar los datos de la venta")
cantidad    = 0
bruto       = 0
nombre      = input("Ingrese el nombre del cliente: ")
producto1   = int(input("Ingrese el precio del producto 1: "))
cantidad    = int(input("Ingrese la cantidad del producto 1: "))
bruto       = (producto1 * cantidad) + bruto
producto2   = int(input("Ingrese el precio del producto 2: "))
cantidad    = int(input("Ingrese la cantidad del producto 2: "))
bruto       = (producto2 * cantidad) + bruto
producto3   = int(input("Ingrese el precio del producto 3: "))
cantidad    = int(input("Ingrese la cantidad del producto 3: "))
bruto       = (producto3 * cantidad) + bruto
descuento   = int(input("Ingrese Descuento: "))

print(f"Cliente:\t\t{nombre}")
print(f"Total Bruto:\t\t{bruto}")
totalDesc   = bruto - ((bruto * descuento)/ 100)
print(f"Total desc.:\t\t{totalDesc}")
iva         = (totalDesc * 19) / 100
totalFinal  = totalDesc + iva
print(f"Total:\t\t{totalFinal}")






