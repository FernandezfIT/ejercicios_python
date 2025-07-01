# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), 
# los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1


user    = input("Ingrese su usuario: ")
pwd     = input("Ingrese su contraseña: ")

if (user == "pedro" and pwd == "1234") or (user == "angel" and pwd == "a4s1"):
    print("Contraseña Correcta")
else:
    print("Usuario o contraseña Incorrectos.")