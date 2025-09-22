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
# Agregación: Crea una clase Universidad que contenga múltiples Facultades, y una clase Facultad que tenga un nombre y una lista de Carreras. Muestra cómo agregar facultades a una universidad y carreras a una facultad.
   
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
    
    def agregar_universidad(self,universidad):
        pass