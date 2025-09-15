# Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def suma_enteros(numero):
    if numero==0:
        return 0
    else:
        return numero + suma_enteros(numero-1)

total=suma_enteros(5) 
print(f"La suma entre los numeros 0 a 3 es {total}")

# Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

def atras_vector(numeros):
    tamaño=len(numeros)

    if tamaño>0:
        print(numeros[tamaño-1])
        numeros.pop()
        atras_vector(numeros)

atras_vector([2,5,6,7])

# Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores

def mostrar_valores(matriz):
    pass