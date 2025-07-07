
"""
RECEBENDO DADOS DO USUÁRIO

input() -> Todo dado recebido via input é do tipo String

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

EXEMPLO:
- Aspas simples -> 'Angelina Jolie';
- Aspas duplas -> "Angelina Jolie";
- Aspas triplas -> '''Angelina Jolie''';
"""
# - Aspas duplas triplas -> """Angelina Jolie""";

# Entrada de dados
# print("Qual seu nome?")
# nome = input() # input -> Entrada
nome = input('Qual seu nome? ')

# Exemplo de print "antigo" 2.x
# print("Seja bem-vindo(a) %s" % nome# )

# Exemplo de print "moderno" 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print "mais atual" 3.7
print(f'Seja bem-vindo(a) {nome}.')

# print("Qual sua idade? ")
# idade = input()
idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print "antigo" 2.x
# print("A %s tem %s anos." % (nome, idade))

# Exemplo de print "moderno" 3.x
# print("A {0} tem {0} anos.".format(format.(nome, idade))

# Exemplo de print "mais atual" 3.7
print(f'A {nome} tem {idade} anos.')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
# print(f'A {nome} nasceu em {2025 - int(idade)}.')
print(f'A {nome} nasceu em {2025 - idade}.')