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