# Texto Inicial
texto = " Hola, Mundo! Bienvenido a Python. Python es increible "

# Aplicando métodos.
texto_procesado     = texto.strip() # Elimina espacios inicialesy finales
texto_min           = texto_procesado.lower() # Convierte todo el texto a minúsculas
texto_may           = texto_procesado.upper() # Convierte todo el texto mayúsculas
texto_reemplazado   = texto_min.replace("python", "Programación") # Reemplaza "python" por "programación"
posicion_mundo      = texto_reemplazado.find("mundo") # Encuentra la posición de la palabra "mundo"
palabras_lista      = texto_reemplazado.split() # Divide el texto en una lista de palabras

# Resultados
print("Texto original: ")
print(texto)
print("\n Texto sin espacios iniciales y finales:")
print(texto_procesado)
print("\nTexto en minúsculas")
print(texto_min)
print("\nTexto en mayúsculas")
print(texto_may)
print("\n Texto con 'Python' reemplazado por 'programación:'")
print(texto_reemplazado)
print("\nPosicion palabra 'Mundo'")
print(posicion_mundo)
print("\nLista Palabras")
print(palabras_lista)