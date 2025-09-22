#Asociación Básica: Modela una relación entre un Doctor y Paciente, donde un Doctor tiene múltiples Pacientes.
#Implementa una clase Doctor y Paciente, y muestra cómo se relacionan.

class Doctor:
    def __init__(self,nombre):
        self.nombre=nombre
        self.__pacientes=[]
    
    def agregar_paciente(self,paciente):
        if paciente not in self.__pacientes:
            self.__pacientes.append(paciente)
        else:
            print("El paciente ya se encuentra registrado.")

    def ver_paciente(self):
        for paciente in self.__pacientes:
            print(paciente.nombre, end=" | ")    

class Paciente:
    def __init__(self,nombre):
        self.nombre=nombre

doctor=Doctor("Andres")
paciente=Paciente("Carlos")
paciente_nuevo=Paciente("Jose")

doctor.agregar_paciente(paciente)
doctor.agregar_paciente(paciente_nuevo)
print(f'Doctor: {doctor.nombre}')
print('-------------------')
print('Pacientes:')
doctor.ver_paciente()

print("============================================================")
# Agregación: Crea una clase Universidad que contenga múltiples Facultades, y una clase Facultad que tenga un nombre y una lista de Carreras. 
# Muestra cómo agregar facultades a una universidad y carreras a una facultad.
   
class Universidad:
    def __init__(self):
        self.facultades=[]
    
    def agregar_facultades(self,facultad):
        if facultad not in self.facultades:
            self.facultades.append(facultad)   

class Facultad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.carreras=[]
    
    def agregar_universidad(self,carrera):
        if carrera not in self.carreras:
            self.carreras.append(carrera)

#Composición: Modela un Ordenador que tiene un Procesador, RAM, y Disco Duro. 
# Implementa las clases correspondientes y muestra cómo un Ordenador puede estar compuesto por estos elementos.

class Ordenador:
    def __init__(self,procesador,ram,disco_duro):
        self.procesador=procesador
        self.ram=ram
        self.disco_duro=disco_duro

class Procesador:
    def __init__(self,frecuencia,nucleos):
        self.frecuencia=frecuencia
        self.nucleos=nucleos
    
class Ram:
    def __init__(self,capacidad, velocidad):
        self.capacidad=capacidad
        self.velocidad=velocidad

class Disco_Duro:
    def __init__(self,capacidad,tipo):
        self.capacidad=capacidad
        self.tipo=tipo

procesador=Procesador("1hz","4")
ram=Ram("32GB","100Ghz")
disco_duro=Disco_Duro("1TB","HDD")
ordenador=Ordenador(procesador,ram,disco_duro)

print("============================================================")
# Encapsulamiento Simple: Crea una clase CuentaBancaria con atributos saldo (privado) y métodos para depositar, retirar, y mostrar_saldo. 
# Implementa un control de acceso para evitar que el saldo sea negativo.
class Cuenta_bancaria:
    def __init__(self,saldo):
        self.__saldo=saldo
    
    def depositar(self,monto):
        self.saldo=self.saldo+monto
    
    def retirar(self, monto):
        if self.saldo<monto:
            print("NO CUENTA CON SALDO SUFICIENTE PARA ESTA OPERACION")
        else:
            self.saldo=self.saldo-monto
    
    def mostrar_saldo(self):
        print(f"SU SALDO ES {self.saldo} pesos.")

print("============================================================")

#Encapsulamiento Avanzado: Diseña una clase Biblioteca que tenga una lista de Libros. 
# Los libros deben ser accesibles solo mediante métodos de la Biblioteca, como agregar_libro, remover_libro, y mostrar_libros.

class Biblioteca:
    def __init__(self):
        self.libros=[]
    
    def agregar_libros(self,libro):
        if libro not in self.libros:
            self.libros.append(libro)
        else:
            print("EL LIBRO YA SE ENCUENTRA EN LA BIBLIOTECA")
    
    def mostrar_libros(self):
        for index,libro in enumerate(self.libros):
            print(f"{index+1}: {libro.titulo}")

    def remover_libro(self):
        self.mostrar_libros()
        index=int(input("Elija que libro quiere eliminar: "))
        if index > len(self.libros) :
            print("⚠️ LIBRO NO ENCONTRADO")
        else: 
            self.libros.pop(index-1)

class Libro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor

libro_1=Libro("Pandemia","Alan Holan")
libro_2=Libro("Sociedad y Estado", "Weber")
libro_3=Libro("Tecnologia XXI","Cesar Portland")

biblioteca= Biblioteca()
biblioteca.agregar_libros(libro_1)
biblioteca.agregar_libros(libro_2)
biblioteca.agregar_libros(libro_3)

# biblioteca.mostrar_libros()

biblioteca.remover_libro()