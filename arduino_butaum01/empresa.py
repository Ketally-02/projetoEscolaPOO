class Pessoa:
    def __init__(self, nome=None, tipo=None):
        if nome is None:
            nome = input("Digite o seu nome: ")
        if tipo is None:
            tipo = input("Digite 1 se você é nosso cliente e 2 se você é nosso funcionário: ")
        self.nome = nome
        self.tipo = 'Cliente' if tipo == '1' else 'Funcionário'

    def apresentar(self):
        return f"Meu nome é {self.nome}. Sou {self.tipo}."


class Funcionario(Pessoa):
    def __init__(self, nome=None, setor=None):
        if nome is None:
            nome = input("Digite o nome do funcionário: ")
        if setor is None:
            setor = input("Digite o setor do funcionário: ")
        super().__init__(nome, '2')
        self.setor = setor

    def apresentar(self):
        return f"Meu nome é {self.nome}. Sou {self.tipo}. Meu setor é {self.setor}."


class Cliente(Pessoa):
    def __init__(self, nome=None, cpf=None, email=None):
        if nome is None:
            nome = input("Digite o nome do cliente: ")
        if cpf is None:
            cpf = input("Digite o CPF do cliente: ")
        if email is None:
            email = input("Digite o seu email: ")
        super().__init__(nome, '1')
        self.cpf = cpf
        self.email = email

    def apresentar(self):
        return f"Meu nome é {self.nome}. Sou {self.tipo}. Meu CPF é {self.cpf}. Meu email é {self.email}."


if __name__ == '__main__':

    pessoa = Pessoa()
    print(pessoa.apresentar())

    if pessoa.tipo == 'Cliente':
        cliente = Cliente(nome=pessoa.nome)
        print(cliente.apresentar())
    elif pessoa.tipo == 'Funcionário':
        funcionario = Funcionario(nome=pessoa.nome)
        print(funcionario.apresentar())
    else:
        print('A pessoa não é cliente nem funcionário — programa encerrado.')

    



    