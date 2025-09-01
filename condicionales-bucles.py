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