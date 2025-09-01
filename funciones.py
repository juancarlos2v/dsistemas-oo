# Realizar una función que se llame area_rectangulo() que devuelva el área del rectángulo a partir de su base y altura.

def area_rectangulo (base, altura):
    return base*altura

area= area_rectangulo(2,3)
print(f"El area del rectangulo con base 3 y altura 2 es {area}")

# Realizar una función que se llame relacion() que a partir de dos nros realice lo siguiente:
# a. Si el primer nro es mayor que el segundo, devuelve 1
# b. Si el primer nro es menor que el segundo, devuelve -1
# c. Si ambos nros son iguales, devuelve 0

def relacion(a,b):
    if a>b:
        return 1
    if a<b:
        return -1
    if a==b:
        return 0

rel=relacion(2,2)
print(rel)