"""
Dunder Main e Dunder Name

Dunder -> significa Double Under

__main__ -> Dunder Main

__name__ -> Dunder Name

Em Python são utilizados dunder para criar funções, propriedades, atributos e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){

    return 0;
} 

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){
}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, inteiramente
o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o 
módulo de execução principal.

Main -> Significa principal.

from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7]))
"""

import primeiro
import segundo