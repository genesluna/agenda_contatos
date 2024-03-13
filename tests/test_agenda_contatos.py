from agenda_contatos import AgendaContatos
from io import StringIO
import unittest
import os


class TestAgendaContatos(unittest.TestCase):
    def setUp(self):
        # Cria uma instância da AgendaContatos antes de cada teste
        self.nome_agenda = "contatos_test.pkl"
        self.agenda = AgendaContatos(self.nome_agenda)

    def tearDown(self):
        # Remove o arquivo de contatos após cada teste
        if os.path.exists(self.nome_agenda):
            os.remove(self.nome_agenda)

    def test_deve_adicionar_contato(self):
        """
        Testa se a função adicionar_contato adiciona corretamente um contato à agenda.
        """
        self.agenda.adicionar_contato("Joao", "123456789")
        self.assertIn("Joao", self.agenda.contatos)
        self.assertEqual(self.agenda.contatos["Joao"], "123456789")

    def test_deve_editar_contato_existente(self):
        self.agenda.adicionar_contato("Fernanda", "555666777")
        self.agenda.editar_contato("Fernanda", "999999999")
        self.assertEqual(self.agenda.contatos["Fernanda"], "999999999")

    def test_dever_retornar_msg_ao_editar_contato_inexistente(self):
        self.agenda.adicionar_contato("Pedro", "222333444")

        # Redireciona a saída padrão para uma string para verificar a impressão
        with StringIO() as mock_output:
            import sys

            sys.stdout = mock_output

            self.agenda.editar_contato("Inexistente", "987654321")

            sys.stdout = sys.__stdout__
            output_str = mock_output.getvalue()

        self.assertIn("Contato Inexistente não encontrado na agenda. Não foi possível editar.", output_str)

    def test_deve_remover_contato(self):
        """
        Testa se a função remover_contato remove corretamente um contato da agenda.
        """
        self.agenda.adicionar_contato("Maria", "987654321")
        self.agenda.remover_contato("Maria")
        self.assertNotIn("Maria", self.agenda.contatos)

    def test_dever_retornar_msg_ao_remover_contato_inexistente(self):
        """
        Testa se a função remover_contato retorna a mensagem correta ao tentar remover um contato inexistente.
        """
        self.agenda.adicionar_contato("Pedro", "222333444")

        # Redireciona a saída padrão para uma string para verificar a impressão
        with StringIO() as mock_output:
            import sys

            sys.stdout = mock_output

            self.agenda.remover_contato("Inexistente")

            sys.stdout = sys.__stdout__
            output_str = mock_output.getvalue()

        self.assertIn("Contato Inexistente não encontrado na agenda. Não foi possível remover.", output_str)

    def test_deve_mostrar_visualizacao_de_contatos(self):
        """
        Testa se a função visualizar_contatos exibe corretamente a lista de contatos na agenda.
        """
        self.agenda.adicionar_contato("Maria", "987654321")
        self.agenda.adicionar_contato("Carlos", "111222333")

        # Redireciona a saída padrão para uma string para verificar a impressão
        with StringIO() as mock_output:
            import sys

            sys.stdout = mock_output

            self.agenda.visualizar_contatos()

            sys.stdout = sys.__stdout__
            output_str = mock_output.getvalue()

        self.assertIn("Maria: 987654321", output_str)
        self.assertIn("Carlos: 111222333", output_str)

    def test_deve_buscar_contato(self):
        """
        Testa se a função buscar_contato encontra corretamente um contato na agenda.
        """
        self.agenda.adicionar_contato("Fernanda", "555666777")
        self.agenda.adicionar_contato("Ricardo", "999000111")

        # Redireciona a saída padrão para uma string para verificar a impressão
        with StringIO() as mock_output:
            import sys

            sys.stdout = mock_output

            self.agenda.buscar_contato("Fernanda")
            self.agenda.buscar_contato("Ricardo")

            sys.stdout = sys.__stdout__
            output_str = mock_output.getvalue()

        self.assertIn("Telefone de Fernanda: 555666777", output_str)
        self.assertIn("Telefone de Ricardo: 999000111", output_str)

    def test_dever_retornar_msg_ao_buscar_contato_inexistente(self):
        """
        Testa se a função buscar_contato retorna a mensagem correta ao tentar buscar um contato inexistente.
        """
        self.agenda.adicionar_contato("Pedro", "222333444")

        # Redireciona a saída padrão para uma string para verificar a impressão
        with StringIO() as mock_output:
            import sys

            sys.stdout = mock_output

            self.agenda.buscar_contato("Inexistente")

            sys.stdout = sys.__stdout__
            output_str = mock_output.getvalue()

        self.assertIn("Contato Inexistente não encontrado na agenda.", output_str)

    def test_deve_persistir_contatos(self):
        """
        Testa se a função salvar_contatos persiste corretamente os contatos no arquivo.
        """
        self.agenda.adicionar_contato("Ana", "444555666")

        # Cria uma nova instância da AgendaContatos para simular um reinício do programa
        nova_agenda = AgendaContatos(self.nome_agenda)

        self.assertIn("Ana", nova_agenda.contatos)
        self.assertEqual(nova_agenda.contatos["Ana"], "444555666")


if __name__ == "__main__":
    unittest.main()
