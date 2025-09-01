# Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def suma_enteros(numero):
    if numero==0:
        return 0
    else:
        return numero + suma_enteros(numero-1)

total=suma_enteros(5) 
print(f"La suma entre los numeros 0 a 3 es {total}")