class Hospital:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
        self.__pacientes = []

    def adicionar_paciente(self, paciente):
        self.__pacientes.append(paciente)

    def listar_pacientes(self):
        return [paciente.get_nome() for paciente in self.__pacientes]
    
    @property
    def pacientes(self):
        return self.__pacientes
    
    @pacientes.setter
    def pacientes(self, valor):
        if isinstance(valor, list):
            self.__pacientes = valor
        else:
            print("Erro: atribuição inválida para pacientes — use uma lista de pacientes.")

    def admitir_paciente(self, quantidade):
        if isinstance(quantidade, int):
            if quantidade > 0:
                # cria pacientes placeholders com nomes automáticos
                for i in range(quantidade):
                    nome = f"Paciente_auto_{len(self.__pacientes) + 1}"
                    paciente = type('Paciente', (object,), {'get_nome': (lambda n: (lambda self: n))(nome)})()
                    self.__pacientes.append(paciente)
            else:
                print("Erro: quantidade inválida para admissão!")
        else:
            self.__pacientes.append(quantidade)

    def alta_paciente(self, quantidade):
        if isinstance(quantidade, int):
            if 0 < quantidade <= len(self.__pacientes):
                for _ in range(quantidade):
                    self.__pacientes.pop()
            else:
                print("Erro: quantidade inválida para alta!")
        else:
            try:
                self.__pacientes.remove(quantidade)
            except ValueError:
                print("Erro: paciente não encontrado para alta!")

hospital = Hospital("Hospital Central", "1234-5678")
hospital.adicionar_paciente(type('Paciente', (object,), {'get_nome': lambda self: 'João'})())
hospital.adicionar_paciente(type('Paciente', (object,), {'get_nome': lambda self: 'Maria'})())

hospital.pacientes = -5    # Tentativa inválida
print("Pacientes após tentativa externa:", hospital.listar_pacientes())

hospital.admitir_paciente(1)
print("Pacientes após admissão:", hospital.listar_pacientes())

hospital.alta_paciente(2)
print("Pacientes após alta:", hospital.listar_pacientes())
    
    
