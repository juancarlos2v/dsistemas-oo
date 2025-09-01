# Pedir al usuario que ingrese un nro impar. Mientras que el usuario no ingrese un nro impar se
# volverá a pedir que ingrese un nro impar. Deberá indicar por pantalla si es impar

a=int(input("Ingresar un numero impar: "))

while a%2==0 :
    a=int(input("¡Ingrese un numero impar!\n"))

print("El numero es impar")