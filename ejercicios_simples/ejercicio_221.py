# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor ingresa tu nombre: ")

# imprimir un saludo personalizado
print("Hola,", nombre, "! Bienvenido a Python")


###### TIPOS DE DATOS PRIMITIVOS #######
edad        = 25

#Flotantes o numeros decimales
pi              = 3.141519
valor_uf        = 36088.46

# Cadenas de texto
nombre          = "Juan"
mensaje         = "Hola, ¿cómo estás Juan?, me gustaría conversar contigo...."

# Booleans
juan_mayor_edad = True


########### CONCEPTOS BASE #############
            # INPUT
    # Para solicitar una entrada de caracteres, utilizaremos la función input(), que nos permite dar un valor ingresado por la temrinal a una variable

nombre  = input("Ingrese su nombre: ")
        ## Cuando necesitemos guardar variables numéricas, usaremos int(input())

edad    = int(print("Ingese su edad: "))

        ## Imprimir por pantalla: Esta acción permite que los resultados almacenados en una variable o constante puedan ser
        ## impresos o mostrados por la pantalla. EJEMPLO: 

nombre  = "juan"
edad    = 25
print("la persona se llama: " + nombre + " y tiene " + edad + " años")


############# Strings ##########
    ## Strings = secuancia de caracteres encerrada entre comillas simples (') o dobles (").add()
    ## Es un tipo de dato muy común en la programación, usado para almacenar texto.

mensaje     = "hola, mundo"
nombre      = "César"

## Operaciones de strings
# Concatenación de 1 o varios Strings

saludo      = "Hola"
nombre      = "Pedro"
apellido    = "Pascal"
print(saludo + " " + nombre + " " + apellido)

# Repeticion: Repite el String las veces que necesites con el símbolo *
print("Hola Ignacia" * 3)

# Idexación: Accede a un carácter por su indice (lugar dentro de la cadena de texti >> van desde 0 hacia adelante dependiendo
# del largo de la cadena -- incluye espacios)
palabra     = "Antonia"
print(palabra[0])  # Accede a la primera letra
print(palabra[-2]) # Accede a la penultima letra

## SubStrings: Obtiene una parte del string indicando el inicio y el termino de captura
texto       = "Llanos Juan"
print(texto[7:11]) # obtiene la palabra juan

