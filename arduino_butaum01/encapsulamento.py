class Conta:
    def __init__(self, saldo=0):
        self.__saldo = saldo 
    
    @property
    def saldo(self):
        return self.__saldo 

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Erro: saldo não pode ser negativo!")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor 

    
conta2 = Conta(500)
print("Saldo inicial:", conta2.saldo)

conta2.saldo = - 300    # Tentativa invalida
print("Saldo após tentativa externa:", conta2.saldo)

conta2.depositar(300)
print("Saldo após depósito:", conta2.saldo)