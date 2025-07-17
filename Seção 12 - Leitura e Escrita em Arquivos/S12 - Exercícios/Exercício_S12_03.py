"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este arquivo possui.
"""

# PROFESSOR

arquivo: str = input('Informe o nome do arquivo para abrir: ')

with open(f'/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/{arquivo}', 'r') as arq:
    linhas = arq.readlines()

print(f'Exeiste(m) {len(linhas)} linha(s) no arquivo.')


# MEU - IGNORAR - FALTA DE ENUNCIADO

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/letras.txt', 'w') as arquivo:
    while True:
        texto = input('Informe um nome de arquivo ou digite sair: ')
        if texto != 'sair':
            arquivo.write(texto)
            arquivo.write('\n')
        else:
            break

print("\n--- Analisando o Arquivo ---")

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/letras.txt', 'r') as arquivo:
    print(f'O arquivo possui {len(arquivo.readlines())} linhas.')
