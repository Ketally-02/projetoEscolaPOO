class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}."
    
class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula}."
        
class Professor(Pessoa):
    def __init__(self, nome: str, disciplina: str) -> None:
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        return f"Professor {self.nome} de sou professor de {self.disciplina}."
    
class BolsaMixin:
    def calcular_bolsa(self) -> float:
        return 1200.0
    
class AlunoBolsista(Aluno, BolsaMixin):
    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e recebo bolsa de R$ {self.calcular_bolsa():.2f}"
    
def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
    return [p.apresentar() for p in pessoas]

def main() -> None:
    p = Pessoa ("Ana")
    a = Aluno("Bruno", "2023001")
    pr = Professor("Carla", "Matemática")
    ab = AlunoBolsista("Daniel", "2023002")

    resultados = apresentar_todos([p, a, pr, ab])
    for r in resultados:
        print(r)

    print("", 
          f"isinstance(ab, Pessoa): {isinstance(ab, Pessoa)}",
          f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}",
          f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}",
          sep="\n")
    
    print("MRO AlunoBolsista:")
    for cls in AlunoBolsista.__mro__:
        print(f" - {cls.__name__}")

if __name__ == "__main__":
    main()



    
    
