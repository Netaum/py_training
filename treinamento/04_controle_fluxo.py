# Todo o controle de fluxo no python é feito por 3 tipos
# if, for e while
# Pode parecer estranho, mas a tabulação é parte da linguagem

int_var = 10

if int_var > 5:
    print('maior que cinco') #apenas um tab

if int_var > 10:
    print('maior que 10')
elif int_var > 5:
    print('maior que 5')
else:
    print('menor')

while int_var < 30:
    int_var += 1
    if int_var % 3 == 0:
        continue
    print(int_var)
    if int_var > 20:
        break

lista_var = [1,2,3,4,5,6,7]
for i in lista_var:
    print(i)

for index, value in enumerate(lista_var):
    print(f'Indice {index} e valor {value}')

for i in range(10):
    print(i)

for i in range(10,20):
    print(i)

for i in range(0,9,2):
    print(i)

# checando variaveis
var_null = None
if var_null:
    print('Variavel existe')
else:
    print('Variavel nula ou vazia')

var_lista = [1,2,3,4,5]
if 1 in var_lista:
    print('lista contem o numero 1')

var_string = 'um novo mundo'
if 'mundo' in var_string:
    print(var_string)
