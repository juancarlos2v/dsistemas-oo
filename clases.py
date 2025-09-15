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
