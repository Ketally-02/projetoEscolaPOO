def professores():
    print("\n---Lançar Notas---")
    n1 = float(input("Digite a nota do primeiro bimestre:"))
    n2 = float(input("Digite a nota do segundo bimestre:"))

    media = (n1+n2)/2

    if media >= 6:
        print("O aluno está aprovado com a nota:", media)
    else:
        print("O aluno está reprovado com a nota:", media)

def biblioteca():
    print("\n---Alugar Livros---")
    senha = input("Crie uma senha que deve ter pelo menos 8 caracteres:")

    while len(senha) < 7 :
        senha = input("A senha deve ter pelo menos 8 caracteres1!!!")
        senha = input("Crie uma senha que deve ter pelo menos 8 caracteres:")

    nome = input("Digite seu nome:")
    turma = input("Digite sua turma:")
    livro = input("Digite o livro que você deseja:")

def secretaria():
    print("\n---Criar Matrícula---")
    nome = input("Digite seu nome:")
    cpf = input ("Digite seu cpf:")
    endereco = input ("Digite seu endereço:")
    email = input("Digite seu email:")

def laboratorio():
    print("\n---Reservar Sala---")
    nome = input("Digite seu nome:")
    turma = input("Digite sua turma:")
    hora = float(input("Qual horário você deseja?"))
    horas = ["10:00", "14:00", "16:00"]
    lista.pop()

def cantina():
    print("\n---Visualizar cardápio---")
    menu = input("Olá alunos! Aqui vocês podem visualizar o cardápio da semana de maneira rápida. \n Digite 1 para visualizar o cardápio de segunda-feira! \n Digite 2 para visualizar o cardápio de terça-feira! \n Digite 3 para visualizar o cardápio de quarta-feira! \n Digite 4 para visualizar o cardápio de quinta-feira! \n Digite 5 para visualizar o cardápio de sexta-feira!" )

    escolha = int(input("Escolha 1,2,3,4 ou 5:"))

    if escolha == 1:
        print("Café da manhã: Pão com margarina + Café com leite \n Almoço: Arroz branco + Feijão carioca + Salada de repolho refogado + Carne cozida")

    if escolha == 2:
        print("Café da manhã: Pão com margarina + Café \n Almoço: Macarrão + Feijão carioca + Salada verde + Frango")

    if escolha == 3:
        print("Café da manhã: Pão com patê + Suco \n Almoço: Arroz branco + Feijão mulata + Carne cozida")

    if escolha == 4:
        print("Café da manhã: Bolo + Vitamina \n Almoço: Arroz parboilizado + Feijão mulata + Salada de repolho refogado + Ovo cozido")

    if escolha == 5:
        print("Café da manhã: Pão com margarina + Suco \n Almoço: Arroz branco + Feijão carioca + Salada verde + Mistão")
        
    else:    
        print("Opção invalida!")

professores()
biblioteca()
secretaria()
laboratorio()
cantina()