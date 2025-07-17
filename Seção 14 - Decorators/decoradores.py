"""
Decoradores (Decorators)

O que são decoradores?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorator também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

|-----------------------------------------------------------|
|                     FUNÇÃO DECORATOR                      |
|-----------------------------------------------------------|

-------------------------------------------------------------
| |-----------------------------------------------------------| |
| |                     FUNÇÃO DECORADA                       | |
| |-------------------------------------------------------------|
| --------------------------------------------------------------

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja be-vindo(a) à Geek University')

# Testando

saudacao()

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()

--------------------------------------------------------
|    HOME    |  SERVIÇOS  |  PRODUTOS  | ADMINISTRATIVO|
--------------------------------------------------------

https://www.suaempresa.com.br/home

https://www.suaempresa.com.br/serviços

https://www.suaempresa.com.br/produtos

https://www.suaempresa.com.br/admin

# OBS.: Não é código funcional é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('https://www.suaempresa.com.br/login')

def home(request):
    return 'Pode acessar home'
    
def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'

# OBS.: Não confunda Decorator (@checa_login) com Decorator Function (a própria função decoradora)
"""
