class Pessoa:
    def __init__(self, nome=None):
        if nome is None:
            nome = input("Digite o nome da pessoa: ")
            super().__init__(nome)

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}."
    
class Aluno(Pessoa):
    def __init__(self, nome=None, matricula=None, cpf=None):
        if nome is None:
            nome = input("Digite o nome do aluno: ")
        if matricula is None:
            matricula = input("Digite a matrícula do aluno: ")
        if cpf is None:
            cpf = input("Digite o CPF do aluno: ")

        super().__init__(nome)
        self.matricula = matricula
        self.cpf = cpf

        def apresentar(self):
            return f"meu nome {self.nome} minha matricula {self.matricula} meu cpf {self.cpf}."

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula} e meu CPF é {self.cpf}."
    
class Professor(Pessoa):
    def __init__(self, nome=None, disciplina=None, matricula=None):
        if nome is None:
            nome = input("Digite o nome do professor: ")
        if disciplina is None:
            disciplina = input("Digite a disciplina do professor: ")
        if matricula is None:
            matricula = input("Digite a matrícula do professor: ")

        super().__init__(nome)
        self.matricula = matricula
        self.disciplina = disciplina
    
    def apresentar(self):
        return f"meu nom é{self.nome} sou professor de {self.disciplina} minha matricula {self.matricula}."
    

pessoa = Pessoa()
aluno = Aluno()
professor = Professor()

print(pessoa.apresentar())
print(aluno.apresentar())
print(professor.apresentar())
