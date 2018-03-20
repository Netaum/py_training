# Os objetos em python são tipados fortemente (ou seja, os objetos possuem um tipo) mas as 
# variáveis criadas não, ou seja, as restrições de tipo são feitas em tempo de execução
# e não compilação. 
# É comum dizer que o python é "duck typed" --> "Se anda como um pato e grasna como um pato, deve ser um pato"

# Existem 7 (sete) tipos sequenciais em python
# str, unicode, list, tuple, bytearray, buffer, xrange
# ainda existem os tipos container: dicionarios, sets, collections

# listas

var_lista = [] #declaração simples
print(var_lista)
var_lista = [1,2,3,4,5]
print(var_lista)
var_lista = [0] * 10
print(var_lista)
var_lista.append(6)
var_lista.append(7)
print(var_lista)
var_lista = var_lista + [9,3,3,1]
print(var_lista)

# Slices
#a[inicio:fim]  itens do inicio ao fim -1 
#a[inicio:]     itens do inicio até o final da lista
#a[:fim]        itens do começo da lista até o fim -1
#a[:]           copia da lista inteira

var_lista = ['um','dois','tres','quatro','cinco','seis']
print(var_lista)
print(var_lista[0])
print(var_lista[2])
print(var_lista[5])
sub_lista = var_lista[1:4] # corte a lista a partir do indice 1 até o indice 3 (não incluso)
print(sub_lista)
sub_lista = var_lista[:-1] # todos menos a ultima posição
print(sub_lista)
sub_lista = var_lista[-1:] # apenas a ultima posição
print(sub_lista) 
sub_lista = var_lista[1:10:2] # corte a lista a partir do indice 1 até o indice 10, contando de 2 em 2 (não incluso)
print(sub_lista)

# dicionarios
var_dic = {}
print(var_dic)
var_dic = {1:'teste', 2:'outro teste'}
print(var_dic)
print(var_dic[1])
var_dic[4] = "mais um teste"
print(var_dic)
var_dic['isso e estranho'] = 1000
print(var_dic)
print(var_dic['isso e estranho'])
del var_dic[1]
print(var_dic)

# sets - um tipo de lista com elementos unicos
var_lista = [1,2,3,4,1,23,41,123,31,2,3,4,5,1,2,22,3]
print(var_lista)
var_set = set(var_lista)
print(var_set)

var_set.clear()
var_set1 = set([1,2,3,4,5])
var_set2 = set([1,3,4,6,7,8])

var_set = var_set1.union(var_set2)
print(var_set)

var_set = var_set1 - var_set2 # diferença
print(var_set)


var_set = var_set1 & var_set2 # intersect
print(var_set)
