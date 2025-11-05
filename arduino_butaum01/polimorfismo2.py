class Transporte:
    def mover(self):
        print("O transporte está se movendo.")

class Carro(Transporte):
    def mover(self):
        print("O carro está dirigindo na estrada.")

class Bicicleta (Transporte):
    def mover(self):
        print("A bicicleta está pedalando no parque.")

class Avião (Transporte):
    def mover(self):
        print("O avião está se movendo no céu.")

def movendo_transporte(obj):
    obj.mover()

t = Transporte()
c = Carro()
b = Bicicleta()
a = Avião()

objetos = [Transporte(), Carro(), Bicicleta(), Avião()]

for obj in objetos:
    obj.mover()
