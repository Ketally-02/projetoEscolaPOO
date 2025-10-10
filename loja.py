class Loja:
    def __init__(self, nome=None, ramo=None):
        self.nome = nome
        self.ramo = ramo
        self.produtos = []

    def configurar_loja(self):
        self.nome = input("Digite o nome da loja: ")
        self.ramo = input("Digite o ramo da loja: ")
        print(f"Loja '{self.nome}' do ramo '{self.ramo}' configurada com sucesso!")

    def adicionar_produto(self):
        produto = input("Digite o nome do produto a ser adicionado: ")
        self.produtos.append(produto)
        print(f"Produto '{produto}' adicionado com sucesso!")

    def descrever_inventario(self):
        if not self.produtos:
            return "O inventário está vazio."
        else:
            lista_produto = ", ".join(self.produtos)
            return f"Inventário da loja {self.nome} contém os produtos: {lista_produto}"


if __name__ == '__main__':
    minha_loja = Loja()

    minha_loja.configurar_loja()

    minha_loja.adicionar_produto()
    minha_loja.adicionar_produto()
    minha_loja.adicionar_produto()

    print("\nRELATÓRIO DA LOJA")
    print(minha_loja.descrever_inventario())
