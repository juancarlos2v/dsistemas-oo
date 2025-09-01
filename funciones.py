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

# Realizar una función que se llame intermedio() que a partir de dos nros devuelva el punto intermedio. 
# Ej. El punto intermedio entre 10 y 24 = 17; entre 12 y 50 = 31.

def intermedio(a,b):
    return (a+b)/2

punto_intermedio=intermedio(10,12)
print(f"El punto intermedio entre 10 y 4 es {punto_intermedio}")
