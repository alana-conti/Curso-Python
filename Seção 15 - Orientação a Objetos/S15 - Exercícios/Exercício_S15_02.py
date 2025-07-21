"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

# MEU

class Contato:
    
    def __init__(self, nome: str, email: str, telefone: str) -> None:
        if not '@' in email:
            raise ValueError('E-mail inválido!')
        else:        
            self.email: str = email
        self.nome: str = nome
        self.telefone: str = telefone
    
    def __str__(self):
        return f'|  {self.id}  |  {self.nome}  |  {self.email}  |  {self.telefone}  |'
    
        
class Agenda:

    def __init__(self):
        self._contatos = []

    def armazenar_contato(self, contato: Contato) -> None:
        if isinstance(contato, Contato):
            self._contatos.append(contato)
            print(f"Contato '{contato.nome}' armazenado com sucesso.")
        else:
            print("Erro: Apenas objetos da classe Contato podem ser armazenados.")

    def remover_contato(self, contato_para_remover: Contato) -> None:
        try:
            self._contatos.remove(contato_para_remover)
            print(f"Contato '{contato_para_remover.nome}' removido com sucesso.")
        except ValueError:
            print(f" Contato '{contato_para_remover.nome}' não encontrado na agenda para remoção.")

    def buscar_contato(self, nome: str) -> int:
        for indice, contato in enumerate(self._contatos):
            if contato.nome.lower() == nome.lower():
                print(f"Contato '{nome}' encontrado na posição {indice}.")
                return indice
        
        print(f"Contato '{nome}' não foi encontrado na agenda.")
        return -1

    def imprimir_agenda(self):
        if not self._contatos:
            return 'Agenda vazia!'
        else:
            print("--- Lista de Contatos ---")
        for contato in self._contatos:
            print(contato)
        print("-------------------------")

    def imprimir_contato(self, indice: int):
        if 0 <= indice < len(self._contatos):
            contato = self._contatos[indice]
            print(f"Dados do contato no índice {indice}:")
            print(f"  - {contato}")
        else:
            print(f"Erro: Índice {indice} é inválido ou não existe na agenda.")   

if __name__ == '__main__':
    contato1 = Contato("Alice Silva", "alice.s@email.com", "47 91111-1111")
    contato2 = Contato("Beto Rocha", "beto.r@email.com", "47 92222-2222")
    contato3 = Contato("Carla Matos", "carla.m@email.com", "47 93333-3333")
    
    minha_agenda = Agenda()

    minha_agenda.armazenar_contato(contato1)
    minha_agenda.armazenar_contato(contato2)
    minha_agenda.armazenar_contato(contato3)

    minha_agenda.imprimir_agenda()

    id_beto = minha_agenda.buscar_contato("Beto Rocha")
    minha_agenda.buscar_contato("Fernando")

    if id_beto != -1:
        minha_agenda.imprimir_contato(id_beto)

    minha_agenda.imprimir_contato(5) 
    print("-" * 30)

    print("Tentando remover o contato de Beto Rocha...")
    minha_agenda.remover_contato(contato2)

    minha_agenda.imprimir_agenda()


# Professor

from datetime import date
from Exercício_S15_01 import Pessoa

class Agenda:

    def __init__(self):
        self.__contatos: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos

    def armazenar_contato(self, contato: Pessoa) -> None:
        self.contatos.append(contato)

    def remover_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)

    def buscar_contato(self, nome:str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} está na posição {indice}.')
    
    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()
    
    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir

if __name__ == '__main__':
    contato1: Pessoa = Pessoa('Felicity Jones', date(1987, 7, 22), 'felicity@gmail.com')
    contato2: Pessoa = Pessoa("Angelina Jolie", date(1984, 3, 6), "angelina@gmail.com")
    contato3: Pessoa = Pessoa("Ray Sychev", date(1981, 8, 18), "ray@gmail.com")

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    agenda.imprimir_agenda()

    agenda.buscar_contato("Ray Sychev")

    agenda.imprimir_contato(2)

    agenda.remover_contato(contato3)

    agenda.imprimir_agenda()
