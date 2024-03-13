import pickle


class AgendaContatos:
    def __init__(self, nome_agenda="contatos.pkl"):
        """
        Inicializa a classe AgendaContatos.

        Parâmetros:
        - nome_agenda (str): Nome do arquivo de agenda. Padrão é "contatos.pkl".
        """
        self.contatos = {}
        self.nome_agenda = nome_agenda
        self.carregar_contatos()

    def adicionar_contato(self, nome, telefone):
        """
        Adiciona um novo contato à agenda.

        Parâmetros:
        - nome (str): Nome do contato.
        - telefone (str): Número de telefone do contato.
        """
        self.contatos[nome] = telefone
        self.salvar_contatos()
        print(f"Contato {nome} adicionado com sucesso.")

    def editar_contato(self, nome, novo_telefone):
        """
        Edita o número de telefone de um contato existente na agenda.

        Parâmetros:
        - nome (str): Nome do contato a ser editado.
        - novo_telefone (str): Novo número de telefone para o contato.
        """
        if nome in self.contatos:
            self.contatos[nome] = novo_telefone
            self.salvar_contatos()
            print(f"Número de telefone de {nome} editado com sucesso.")
        else:
            print(f"Contato {nome} não encontrado na agenda. Não foi possível editar.")

    def remover_contato(self, nome):
        """
        Remove um contato da agenda pelo nome.

        Parâmetros:
        - nome (str): Nome do contato a ser removido.
        """
        if nome in self.contatos:
            del self.contatos[nome]
            self.salvar_contatos()
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado na agenda. Não foi possível remover.")

    def visualizar_contatos(self):
        """
        Exibe a lista de contatos na agenda.
        """
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            print("Lista de Contatos:", end="\n\n")
            for nome, telefone in self.contatos.items():
                print(f"{nome}: {telefone}")

    def buscar_contato(self, nome):
        """
        Busca um contato na agenda pelo nome e exibe o telefone, se encontrado.

        Parâmetros:
        - nome (str): Nome do contato a ser buscado.
        """
        if nome in self.contatos:
            print(f"Telefone de {nome}: {self.contatos[nome]}")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

    def salvar_contatos(self):
        """
        Salva os contatos no arquivo de agenda usando pickle.
        """
        with open(self.nome_agenda, "wb") as arquivo:
            pickle.dump(self.contatos, arquivo)

    def carregar_contatos(self):
        """
        Carrega os contatos do arquivo de agenda usando pickle.
        Se o arquivo não existe, a agenda é iniciada vazia.
        """
        try:
            with open(self.nome_agenda, "rb") as arquivo:
                self.contatos = pickle.load(arquivo)
        except FileNotFoundError:
            self.contatos = {}
