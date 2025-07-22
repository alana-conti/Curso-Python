"""
Tipagem de dados Dinâmica x Estática

# Tipagem de dados Implícita/Dinâmica (Python)
idade = 42

print(type(idade))

idade = 'Quarenta e dois'

print(type(idade))

# PEP 484 -> introduziu dicas de tipos.
"""

# O erro só aparece quando o código é executado
if True:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(resultado)

# Linguagem com Tipagem Estática (por exemplo Java, C, C#) compilam o código antes de 
# executarem, logo apresentam o erro antes da execução/nem executam-o.
