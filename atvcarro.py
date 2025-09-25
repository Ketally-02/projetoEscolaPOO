class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velociade} km/h!")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velociade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.veelocidade} km/h.")

    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - "
                f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h.")
    
    carro1 = Carro1("Toyota", "Corolla", 2020, "Preto")
    carro1 = Carro2("Honda", "Civic", 2019, "Vermelho")

    print(Carro1.detalhes ())
    print(Carro2.detalhes ())

    Carro1.acelerar(50)
    Carro2.acelerar(30)

    Carro1.frear(20)
    Carro2.frear(15)

    print(Carro1.detalhes ())
    print(Carro2.detalhes ())