class Pato:
    def quack(self):
        print("o pato faz quack!")

class Pessoa:
    def quack(self):
        print("a pessoa imita um pato: quack!")

    def comer(self):
        print("a pessoa está comendo")

def fazer_quack(obj):
    obj.quack()

p = Pato()
h = Pessoa()

fazer_quack(p)
fazer_quack(h)

class Gravação:
    def quack(self):
        print("Som gravado: Quack Quack!") 

class Robo:
    def quack(self):
        print("Robo: Q-U-A-C-K em um som metálico!")    

objetos = [Pato(), Pessoa(), Gravação(), Robo()]

for obj in objetos:
    obj.quack()