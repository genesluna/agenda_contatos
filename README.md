![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![CESMAC EAD](https://res.cloudinary.com/dxylve8nt/image/upload/v1709508355/cesmac_ead_downloaded_logo_r7qz3z.jpg)

# Agenda de Contatos

Código-fonte e testes unitários para o Projeto Integrador V-A do curso de Análise e Desenvolvimento de Sistemas EAD do CESMAC.

## Objetivo

O presente projeto tem como propósito principal a concepção e implementação de uma Agenda de Contatos utilizando a linguagem de programação Python. Adicionalmente, será aplicada uma abordagem sistemática de teste de software, utilizando a biblioteca unittest, a fim de assegurar a confiabilidade, robustez e eficácia do sistema desenvolvido.

## Requisitos

Criar testes unitários que assegurem que a Agenda de Contatos:

- Deve adicionar corretamente um contato.

- Deve editar o telefone de um contato existente.

- Deve, quando solicitado, remover um contato pelo nome.

- Deve mostrar o telefone de um contato pelo nome.

- Deve exibir lista com todos os contatos quando solicitado.

- Deve exibir mensagem adequada quando o usuário tentar editar um contato inexistente.

- Deve exibir mensagem adequada quando o usuário tentar remover um contato inexistente.

- Deve exibir mensagem adequada quando o usuário tentar visualizar um contato inexistente.

- Deve persistir corretamente os dados da agenda em um arquivo no formato pickle.

## Rodando o código

```shell
python main.py
```

## Rodando os testes

```shell
python -m unittest tests/test_agenda_contatos.py
```
