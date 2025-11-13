class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        return f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}"
        
    def bonus(self):
        return 0
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def exibir_informacoes(self):
        return f"Gerente: {self.nome}, Salário: R${self.salario:.2f}, Setor: {self.setor}"
    
    def bonus(self):
        return self.salario * 0.20
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario, vendas=None):
        super().__init__(nome, salario)
        self.vendas = float(vendas) if vendas is not None else 0.0

    def exibir_informacoes(self):
        return f"Vendedor: {self.nome}, Salário: R${self.salario:.2f}, Vendas: R${self.vendas}"
    
    def bonus(self):
        return self.vendas * 50


def main():
    funcionarios = [
        Gerente("Alice", 8000, "Vendas"),
        Vendedor("Bob", 3000, 150),
        Vendedor("Carlos", 3200)
    ]

    for funcionario in funcionarios:
        print(funcionario.exibir_informacoes())
        print(f"Bônus: R${funcionario.bonus():.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()