print("verificando si era apto para ser policia")

edad = int(input("ingresa su edad: "))
altura = int(input("ingresa su altura: "))
nacionalidad = input("ingresa su nacinalidad: ")

if edad >= 18 and altura >= 160 and nacionalidad == "dominicano":
    print("Usted es apto para entrar al policia")

else:
    print("Usted no es apto")