"""
O comando With

Passos para se trabalhar com um arquivo:

# 1 - Abrir o arquivo;
# 2 - Trabalhar o arquivo;
# 3 - Fechar o arquivo;

O bloco With é utilizado para criar um contexto de trabalho onde os recursos 
utilizados são fechados após o bloco with

arquivo = open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/text.txt')
"""

# O bloco with - Forma Pythônica de manipular arquivos

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/text.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)

# print(arquivo.readlines())
