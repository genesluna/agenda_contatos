from os import system, name


def limpar_tela():
    # Verifica o sistema operacional e executa o comando apropriado para limpar a tela
    if name == "nt":  # Windows
        system("cls")
    else:  # Mac e Linux
        system("clear")


def voltar():
    input("\nPressione enter para voltar...")
    limpar_tela()
