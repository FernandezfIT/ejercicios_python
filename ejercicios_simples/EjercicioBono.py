## Escribe un programa que reciba la edad de un usuario y su nivel socioeconomico NSE:
# Bono Base $350.000

#•	Si el usuario es niño/a o adolescente: +0%
#•	Si el usuario es adulto/a: +5%
#•	Si el usuario es anciano/a: +10%

# Bono2: El Bono1 se incrementa:
#•	Si el usuario pertenece al NSE A: +0%
#•	Si el usuario pertenece al NSE B: +5%
#•	Si el usuario pertenece al NSE C: +10%
#•	Si el usuario pertenece al NSE D: +15%
#•	Si el usuario pertenece al NSE E: +20%

bonoBase            = 350000
edad                = 0
totalBono           = 0
input_nse           = " "
rangoEtareo         = " "
nse                 = " "


print("Bienvenido al calculo de Bono:")
edad                 = int(input("Ingrese Edad: "))
input_nse         = input("Ingrese NSE: ")

if edad < 18 and edad >= 0:
    totalBono = bonoBase
    rangoEtareo = "Niño/a o Adolecente"
elif edad >= 18 and edad < 59:
    totalBono = bonoBase * 1.05
    rangoEtareo = "Adulto/a"
elif edad >=60:
    totalBono = bonoBase * 1.1
    rangoEtareo = "Anciano/a"
else: 
    print("Edad incorrecta, no se aplica bono.")
    


match input_nse:
    case 'A':
        totalBono = totalBono
    case 'B':
        totalBono = totalBono * 1.05
    case 'C':
        print(totalBono)
        totalBono = totalBono * 1.1
    case 'D':
        totalBono = totalBono * 1.15
    case 'E':
        totalBono = totalBono * 1.2
    case _:
        print("NSE Incorrecto, no se aplica bono.")


print(f"Usted es {rangoEtareo} del NSE {input_nse}, le corresponde ${int(totalBono)}")







