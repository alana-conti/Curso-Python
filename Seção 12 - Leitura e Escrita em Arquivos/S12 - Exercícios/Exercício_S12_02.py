"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.
"""

# PROFESSOR


vogais: int = 0
consoantes: int = 0
arquivo: str = input('Informe o nome do arquivo para abrir: ')

with open(f'/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/S12 - Exercícios/{arquivo}', 'r') as arq:
    linhas = arq.readlines()

for linha in linhas:
    if linha.replace('\n', '').lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1

if vogais > 0:
    print(f'Existe(m) {vogais} vogais no arquivo.')
else:
    print(f'Não existem vogais no arquivo.')

if consoantes > 0:
    print(f'Existe(m) {consoantes} consoantes no arquivo.')
else:
    print(f'Não existem consoantes no arquivo.')




# MEU - IGNORAR - FALTA DE ENUNCIADO
with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/letras.txt', 'w') as arquivo:
    while True:
        texto = input('Informe um nome de arquivo ou digite sair: ')
        if texto != 'sair':
            arquivo.write(texto)
            arquivo.write('\n')
        else:
            break

print("\n--- Analisando o Arquivo ---")

VOGAIS = "aeiouáéíóúàâêôãõ"
CONSOANTES = "bcdfghjklmnpqrstvwxyzç"

vogais_total = 0
consoantes_total = 0

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/letras.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
    for caracter in conteudo_completo:
            letra = caracter.lower()
            if letra in VOGAIS:
                vogais_total += 1
            elif letra in CONSOANTES:
                consoantes_total += 1


print(f'Os nomes informados possuem {vogais_total} vogais e {consoantes_total} consoantes.')

