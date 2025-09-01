# Pedir al usuario que ingrese un nro impar. Mientras que el usuario no ingrese un nro impar se
# volverá a pedir que ingrese un nro impar. Deberá indicar por pantalla si es impar

a=int(input("Ingresar un numero impar: "))

while a%2==0 :
    a=int(input("¡Ingrese un numero impar!\n"))

print("El numero es impar")

# Pedir al usuario que ingrese dos nros. Luego imprimir 3 opciones (1. sumar, 2. restar y 3.multiplicar). 
# Pedir al usuario que ingrese una opción, ejecutar la operación y mostrar por pantalla el resultado.
print("===========INGRESE DOS NUMEROS===========")
b=int(input("> "))
c=int(input("> "))

print("===ELIJA UNA DE LAS SIGUIENTE OPCIONES===")
print("\n 1. Sumar \n 2. Restar \n 3. Multiplicar")
opcion=int(input("> "))

if opcion==1 :
    print(f"La suma es {b+c}")
elif opcion==2:
    print(f"La resta es {b-c}")
elif opcion==3:
    print(f"La multiplicación es {b*c}")

# Definir una lista de números y mostrar por pantalla el valor promedio. No utilizar funciones nativas sum() o len()

numeros=[1,3,4,6,8,9]
contador=0
suma=0

for numero in numeros:
    suma+=numero
    contador+=1

print(numeros)
print(f"El promedio de la lista es {suma/contador}")

# Definir una lista de números, encontrar el valor mínimo de la lista e imprimirlo. No utilizar la función nativa min().

valores=[89,5,4,7,9,2]
minimo=valores[0]

for valor in valores:
    if valor<minimo:
        minimo=valor

print(valores)
print(f"El valor minimo es {minimo}")