# metodos de Strings en Python con ejemplos:

texto   = "prueba metodos strings"
texto2  = "PRUEBA METODOS STRINGS5"
texto3  = "prueba{ }metodos{ }strings"
texto4  = "\tprueba  metodosstrings"

# .capitalize()
print(texto.capitalize())
    ## Transforma el 1er caracter del String a Mayúscula
    # OUTPUT: Prueba metodos strings

# .casefold()
print(texto.casefold() == texto2.casefold())
    ## Permite comparar 2 cadenas de texto ignorando minusculas y mayusculas
    # OUTPUT: TRUE

# .center()
print(texto.center(10))
    ## Permite centrar la cadena de texto dentro de un ancho especifico rellenando a la izquierda y a la derecha
    ## con espacios o un caracter especificado
    # OUTPUT:    prueba metodos strings

# .count()
print(texto.count("s"))
    ## Permite contar la cantidad de veces que se repite un caracter
    # OUTPUT: 3 => la "s" se repite 3 veces dentro de la cadena

# .encode()
encode = texto.encode()
print(encode)
    ## Codifica la cadena de texto con el metodo indicado

# .endswith()
print(texto.endswith("x"))
    ## Verifica que la cadena termine con el caracter indicado
    # OUTPUT Ejemplo: FLASE => no termina en x

# .expandtabs()
print(texto4.expandtabs(12))
    ## Indicado dentro del texto una tabulacion, la expande en los espacios indicados
    # output: ____________prueba  metodosstrings => El espacio normal de una tabulacion \t es de 8
    # esta tiene 12

# .find()
print(texto.find("s"))     
    ## Indica el lugar en el que primero se encuentra (de izq a der) el carácter indicado.

# .format()
nombre  = "Fefe"
edad    = 50
texto5  = "Me llamo {} y tengo {} años".format(nombre, edad)
print(texto5)
    ## Siguiendo la sintaxis del ejemplo, permite reemplazar dentro de la cadena de texo los simbolos {} por los datos
    # almacenados en las variables indicadas
    # OUTPUT: Me llamo Fefe y tengo 50 años => Fefe y 50 no estaban en el texto original pero
    # eran los valores almacenados en las variables nombre y edad que posteriormente se agregan
    # al metodo .format()

# .format_map()
texto5  = "Me llamo {nombre} y tengo {edad} años"
valores = {"nombre": "Juli", "edad": "1" } 
print(texto5.format_map(valores))

# .index()
print(texto.index("e"))
    ## Devuelve el indice del caracter indicado dentro de la cadena de texto
    # OUTPUT: en este ejemplo 3

# .isalnum()
print(texto.isalnum())

textoAlpha = "3asdsdasdasdasd"
print(textoAlpha.isalnum())
    ## devuelve TRUE si la cadena indicada es alfanumerica o falso si no
    #OUTPUT 1 : FALSE
    #OUTPUT 2 : TRUE

# .
