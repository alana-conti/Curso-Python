"""
Optimizações
"""
import collections
from timeit import timeit
import sys

Pessoa = collections.namedtuple('Pessoa', 'nome email')

felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

print(timeit('felicity.email', globals=globals()))

# Globals -> mostra todos os componentes presentes no contexto do programa

# 0.025384982000105083

print(sys.getsizeof(list(range(29082020))))

# 232656216
