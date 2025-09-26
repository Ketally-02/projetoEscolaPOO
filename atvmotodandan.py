class Moto:
    def __init__ (self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.velocidade} km/h.")

    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - "
                f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h.")
    
moto1 = Moto("Yamaha", "Yamaha Fazer 250", 2025, "Preto")
moto2 = Moto("Honda", "Honda Accord", 2018, "Azul")

print("---ESTADO INICIAL---")
print(moto1.detalhes())
print(moto2.detalhes())

print("---A CORRIDA COMEÇOU---")
moto1.acelerar(90)
moto2.acelerar(40)
moto1.acelerar(50)
moto2.frear(30)
moto1.frear(40)
moto2.acelerar(80)

print("---ESTADO FINAL---")
print(moto1.detalhes())
print(moto2.detalhes())

print("---RESULTADO DA CORRIDA---")
if moto1.velocidade > moto2.velocidade:
    print(f"A vencedora é a {moto1.modelo} com {moto1.velocidade} km/h!")
elif moto2.velocidade >  moto1.velocidade:
    print(f"A vencedora é a {moto2.modelo} com {moto2.velocidade} km/h!") 
else:
    print(f"A corrida terminou em empate, ninguém venceu!")