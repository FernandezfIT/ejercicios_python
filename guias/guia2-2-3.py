#
nomAlum = input("Ingrese el nombre del alumno: ")
rut     = input("Ingrse RUT apoderado: ")
curso   = input("Ingrese curso al cual el alumno debe matricularse: ")

matricula   = 25000
mensualidad = 30000
resultadoAnual = (mensualidad * 10) + matricula

print("-----Detalle Anualidad Colegio----")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRICULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")