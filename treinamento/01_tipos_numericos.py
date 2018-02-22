import math
# Os objetos em python são tipados fortemente (ou seja, os objetos possuem um tipo) mas as 
# variáveis criadas não, ou seja, as restrições de tipo são feitas em tempo de execução
# e não compilação. 
# É comum dizer que o python é "duck typed" --> "Se anda como um pato e grasna como um pato, deve ser um pato"

#Tipos numérico
int_var = 10      #int
float_var = 10.1  #float
complex_var = 10j #complex

#Operações simples

soma = 10 + 20
print(soma)
sub = soma - 200
print(sub)
mult = soma * 5
print(mult)
div = soma / 10
print(div)

#Operações complexas
negativo = -soma
print(negativo)
absoluto = abs(div)
print(absoluto)
quociente = soma // 4
print(quociente)
resto = soma % 4
print(resto)
exponencial = soma ** 2
print(exponencial)
exponencial = pow(soma, 2)
print(exponencial)
div_mod = divmod(soma, 4)
print(div_mod)

#Operações matemáticas
truncado = math.trunc(10.123331)
print(truncado)
arredondado = round(10.23455, 2)
print(arredondado)
n_teto = math.ceil(4.1)
print(n_teto)
n_base = math.floor(4.1)
print(n_base)
