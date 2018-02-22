# O python possui uma forma muito peculiar de lidar com listas,
# chamado List Comprehensions
# Basicamente é possivel aplicar funções naturais à lista para gerar outras listas

var_lista = [1,2,3,4,5,6,7,8,9,10]
var_lista_par = []

for i in var_lista:
    if i % 2 == 0:
        var_lista_par.append(i)

print(var_lista)
print(var_lista_par)

var_lista_par = [i for i in var_lista if i % 2 == 0]
print(var_lista_par)

var_lista_par = [i*2 for i in var_lista if i % 2 == 0]
print(var_lista_par)

var_lista = [i for i in range(10)]
print(var_lista)

var_lista_par = [i for i in var_lista if i % 2 == 0]
var_lista_impar = [i for i in var_lista if i not in var_lista_par]
print(var_lista_impar)

var_string = 'Mirandamente, o sujeito inocente, se envolveu com pente, e foi se pentear'
var_palavras = var_string.split(',')
print(var_palavras)
var_complexo = [[w.upper(), w.lower(), len(w)] for w in var_palavras]
print(var_complexo)

var_lista1 = [i for i in range(1,10)]
var_lista2 = [i for i in range(30,40)]

var_cross = [(x,y) for x in var_lista1 for y in var_lista2]
print(var_cross)
