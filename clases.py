# Crea una clase Animal con atributos nombre y especie. Incluye un método hacer_sonido que imprima un sonido genérico. 
# Crea una subclase Perro que herede de Animal y sobreescriba el método hacer_sonido para imprimir "Guau".
class Animal:
    def __init__(self,nombre,especie):
        self.nombre=nombre
        self.especie=especie

    def hacer_sonido(self):
        print("sonido generico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")
 

animal= Perro("Bay","Perro")
animal.hacer_sonido()

print("============================================================")
#Crea una clase CuentaBancaria con los atributos titular y saldo. Incluye métodos depositar y retirar. 
# Crea una subclase CuentaAhorro que agregue un atributo interes y un método para aplicar el interés al saldo.

class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo

    def depositar(self,cantidad):
        self.saldo=self.saldo+cantidad
        print(f"El saldo actual es de {self.saldo}")

    def retirar(self,cantidad):
        self.saldo=self.saldo-cantidad
        print(f"El saldo actual es de {self.saldo}")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo,interes):
        super().__init__(titular, saldo)
        self.interes=interes
    
    def aplicarInteres(self):
        self.saldo=self.saldo+(self.saldo*self.interes)
        print(f"Su saldo mas intereses es {self.saldo}")

cuenta= CuentaAhorro("Juan Vilcherrez",100,0.1)
print(f"El saldo actual de {cuenta.titular} es ${cuenta.saldo}")
cuenta.aplicarInteres()
cuenta.depositar(300)

print("============================================================")

#Modela una clase Persona con atributos nombre y edad. Incluye un método presentarse. 
# Crea una subclase Alumno que herede de Persona y añada un atributo carrera y un método estudiar (debe imprimir que el alumno está estudiando su carrera). 
# Implementa un método adicional cambiar_carrera que permita al alumno cambiar su carrera, asegurándose de que la nueva carrera no sea igual a la anterior.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} tengo {self.edad} años")

class Alumno(Persona):
    def __init__(self, nombre, edad,carrera):
        super().__init__(nombre, edad)
        self.carrera=carrera

    def estudiar(self):
        print(f"El alumno {self.nombre} esta estudiando la carrera de {self.carrera}")

    def cambiar_carrera(self,carrera):
        if(self.carrera!=carrera):
            self.carrera=carrera
        else:
            print("La nueva carrera debe ser distinta a la anterior")

alumno= Alumno("Juan Carlos",25,"Arquitectura")
alumno.presentarse()
alumno.estudiar()
alumno.cambiar_carrera("Analisis de Sistemas")
alumno.estudiar()

print("============================================================")

#Diseña una clase Libro con atributos titulo y autor. Incluye un método leer (debe imprimir que el libro está siendo leído). 
#Crea una subclase Ebook que herede de Libro y añada un atributo formato y un método descargar (debe imprimir que el ebook está siendo descargado). 
#Implementa un método adicional cambiar_formato que permita cambiar el formato del ebook, verificando que el nuevo formato sea válido (por ejemplo, "PDF", "EPUB", "MOBI").

class Libro:
    def __init__(self,titulo, autor):
        self.titulo=titulo
        self.autor=autor
    
    def leer(self):
        print(f"Estas leyendo {self.titulo} de {self.autor}")

class Ebook(Libro):
    def __init__(self, titulo, autor,formato):
        super().__init__(titulo, autor)
        self.formato=formato

    def descargar(self):
        print(f"Se esta descargando el libro {self.titulo} de {self.autor}")

    def cambiar_formato(self,formato):
        if(formato!="PDF" and formato != "EPUB" and formato!="MOBI"):
            print("Formato no permitido")
        else:
            self.formato=formato
            print(f"¡Formato cambiado a {self.formato} con exito!")

libro=Ebook("Pandenomics","Javier Milei","PDF")
libro.leer()
libro.descargar()
libro.cambiar_formato("AAA")