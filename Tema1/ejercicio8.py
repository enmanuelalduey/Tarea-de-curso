
def area_rectangulo(ancho, alto):
    return ancho * alto

ancho = float(input("Por favor, ingresa el ancho del rectángulo: "))
alto = float(input("Por favor, ingresa el alto del rectángulo: "))

area = area_rectangulo(ancho, alto)
print(f"El área del rectángulo es: {area}")
