from agenda_contatos import AgendaContatos
from util import limpar_tela, voltar


def main():
    # Cria uma instância da AgendaContatos
    agenda = AgendaContatos()

    # Limpa a tela do console
    limpar_tela()

    while True:
        # Menu principal
        print("=" * 40)
        print(f'{"Agenda de Contatos":^40}')
        print("=" * 40)
        print("1. Adicionar Contato")
        print("2. Editar Contato")
        print("3. Remover Contato")
        print("4. Visualizar Contatos")
        print("5. Buscar Contato por Nome")
        print("0. Sair", end="\n\n")

        # Solicita a escolha do usuário
        escolha = input("Escolha uma opção: ")

        # Limpa a tela do console
        limpar_tela()

        # Executa a ação com base na escolha do usuário
        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            # Adiciona o contato à agenda
            agenda.adicionar_contato(nome, telefone)
            # Aguarda o usuário pressionar enter para continuar
            voltar()

        elif escolha == "2":
            nome = input("Digite o nome do contato a ser editado: ")
            novo_telefone = input("Digite o novo telefone: ")
            # Edita o telefone de um contato pelo nome
            agenda.editar_contato(nome, novo_telefone)
            # Aguarda o usuário pressionar enter para continuar
            voltar()

        elif escolha == "3":
            nome = input("Digite o nome do contato a ser removido: ")
            # Remove um contato pelo nome
            agenda.remover_contato(nome)
            # Aguarda o usuário pressionar enter para continuar
            voltar()

        elif escolha == "4":
            # Exibe a lista de contatos
            agenda.visualizar_contatos()
            # Aguarda o usuário pressionar enter para continuar
            voltar()

        elif escolha == "5":
            nome = input("Digite o nome do contato a ser buscado: ")
            # Busca e exibe um contato pelo nome
            agenda.buscar_contato(nome)
            # Aguarda o usuário pressionar enter para continuar
            voltar()

        elif escolha == "0":
            print("Saindo da Agenda de Contatos. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            # Aguarda o usuário pressionar enter para continuar
            voltar()


if __name__ == "__main__":
    # Chama a função main() quando o script é executado
    main()
