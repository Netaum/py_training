#Collection são classes que lidam com agrupamentos de dados (como listas, sets, dicionários, etc)

from collections import *
# Contador
# Coleção para operações com contadores
# Funciona como um dicionário com um contador interno
ct = Counter()
palavras = ['vermelho', 'azul','preto','vermelho','verde', 'verde', 'branco', 'preto']

for p in palavras:
    ct[p] += 1

print(ct)

# Iniciadores

# Padrão
ct = Counter()
print(ct)

# Contando caracteres em uma string
ct = Counter('Teste')
print(ct)

# Dicionario
ct = Counter({'Vermelho': 10, 'Azul': 5})
print(ct)

# Args
ct = Counter(Vermelho=4, Azul=10)
print(ct)

# Metodos
# Elementos
print(ct.elements())

# X mais comuns
print(ct.most_common(2))


####
# Named Tuple
# Usado para quando queremos um objeto simples com dois valores
# Se comporta como uma chave / valor de um dicionário

# O parametro verbose=True imprime a classe gerada 
Ponto = namedtuple('Ponto', ['x', 'y'], verbose=True)

p = Ponto(10, y=20)
print(p)
print(p[0] + p[1])


####
# Dicionários ordenados
# Se comportam como um dicionário normal, mas interam os elementos pela ordem em que
# foram inseridos
dic = {'banana':4, 'maça':5, 'pera':1, 'laranja':2, 'uva':0}
print(dic)

dic = OrderedDict(sorted(dic.items(), key=lambda t: t[1]))
print(dic)