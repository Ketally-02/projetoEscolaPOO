def cadastro():
    nome = input ("Digite seu nome: ")
    idade = int(input ("Digite sua idade: "))
    email = input ("Digite seu email: ")
    insta = input ("Digite seu instagram: ")
    zapzap = input ("Digite seu número: ")

    print ("\n---FICHA DE CADASTRO---")
    print ("nome:", nome)
    print ("idade:", idade)
    print ("email:", email)
    print ("insta:", insta)
    print ("zapzap:", zapzap)

    if idade < 18:
        print("Você é menor de idade!")

    else:
        print("Você é maior de idade \n Cadastro realizado!")

    

cadastro()
