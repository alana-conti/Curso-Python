"""
1. Crie um programa que:
a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere “0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""

# MEU

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/arq.txt', 'a') as arquivo:
    while True:
        caracter = input('Informe um caracter ou digite 0: ')
        if caracter != '0':
            arquivo.write(caracter)
            arquivo.write('\n')
        else:
            break

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/arq.txt', 'r') as arquivo:
    print(arquivo.read())

# PROFESSOR

with open ('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/arq.txt', 'a') as arquivo:
    while True:
        caracter: str = input('Informe um caractere ou 0 para sair: ')

        if caracter != 0:
            arquivo.write(f'{caracter}\n')
        else:
            break

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/arq.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linhas)