"""
Programação Orientada à Objetos - POO

- POO é um paradigma de programação que utiliza de mapeamento
de objetos do mundo real para modelos computacionais.

- Paradigma de programação é a forma/metodologia utilizada para
pensar/desenvolver sistemas.

- Paradigmas de programação -> como você vai pensar na forma de desenvolver seu programa;
    - Programação Estruturada (linguagem C);
    - Programação Orientada á objeto (linguagem java);
    - Programação Funcional.
- Cada uma depende da linguagem utilizada;
- Python é multiparadigma

-- FAZER UMA REPRESENTAÇÃO DO MUNDO REAL DE FORMA COMPUTACIONAL --

Principais elementos da Orientação a Objeto:
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
- Atributos -> Características do objeto;
- Métodos -> Comportamento do objeto (funções). Como esse objeto se comporta, o que ele faz/executa;
- Construtor -> Método especial utilizado para criar os objetos a partir da classe;
- Objetos -> Instâncias da classe, são criadas a partir da classe.
"""

numero = 10
print(numero)
print(type(numero))

nome = 'Geek'
print(nome)
print(type(nome))

class Produto:
    pass

ps4 = Produto()
print(ps4)
print(type(ps4))
