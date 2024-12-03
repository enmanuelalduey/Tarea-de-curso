def calcular_edad(dia, mes, año):
    dia_actual = int(input("Ingresa el día actual: "))
    mes_actual = int(input("Ingresa el mes actual: "))
    año_actual = int(input("Ingresa el año actual: "))
    
    if (dia_actual == dia and mes_actual == mes):
        print("¡Hoy es tu cumpleaños!")
        print(f"Tienes {edad} años.")
    else:
        edad = año_actual - año - ((mes_actual, dia_actual) < (mes, dia))
        print(f"Tienes {edad} años.")
        
dia = int(input("Introduce el día de tu nacimiento: "))
mes = int(input("Introduce el mes de tu nacimiento: "))
año = int(input("Introduce el año de tu nacimiento: "))

calcular_edad(dia, mes, año)
