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

# Realizar una función que se llame separar() que reciba una lista de nros y devuelva dos listas ordenadas.
# La primera con nros pares y la segunda con nros impares

def separar(numeros):
    pares=[]
    impares=[]

    for numero in numeros:
        if numero%2==0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares,impares

numeros=[5,6,7,1,2,3]
pares,impares=separar(numeros)
print(numeros)
print(f"Los numeros pares son {pares}")
print(f"Los numeros impares son {impares}")