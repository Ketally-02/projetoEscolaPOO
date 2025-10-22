class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}."
    
class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str, cpf: str) -> None:
        super().__init__(nome)
        self.matricula = matricula
        self.cpf = cpf

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula} e meu CPF é {self.cpf}."
    
pessoa = Pessoa("Bruna")
aluno = Aluno("Bruna", "2024001", "123.456.789-00")

print(pessoa.apresentar())
print(aluno.apresentar())