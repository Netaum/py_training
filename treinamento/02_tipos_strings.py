from datetime import datetime
# Os objetos em python são tipados fortemente (ou seja, os objetos possuem um tipo) mas as 
# variáveis criadas não, ou seja, as restrições de tipo são feitas em tempo de execução
# e não compilação. 
# É comum dizer que o python é "duck typed" --> "Se anda como um pato e grasna como um pato, deve ser um pato"

# Existem 7 (sete) tipos sequenciais em python
# str, unicode, list, tuple, bytearray, buffer, xrange

# strings
str_test = 'Teste de string com aspas simples'
print(str_test)
str_test = "Teste de string com aspas duplas"
print(str_test)
str_test = "String contendo aspas simples 'aqui'"
print(str_test)
str_test = 'String contendo aspas duplas "aqui"'
print(str_test)
str_test = 'String contendo alguns caracteres de escape: \" \a \t tab'
print(str_test)
str_test = r'String contendo alguns caracteres de escape, mas com string fixa (equivalente ao @ do c#): \" \a \t tab'
print(str_test)

# Concatenação de strings
str_text = "Formato simples"
int_text = 10
float_text = 3.141560054923

str_test = "%s %d" % (str_text, int_text)       #derivado do C
print(str_test)
str_test = "{} {}".format(str_text, int_text)   #novo modo
print(str_test)
str_test = f"{str_text} {int_text}"             #string interpolation
print(str_test)

# Formatação string
str_test = '"{:>20}"'.format(str_text) # 20 caracteres completados com espaços à esquerda
print(str_test)
str_test = '"{:20}"'.format(str_text) # 20 caracteres completados com espaços à direita
print(str_test)
str_test = '"{:-<20}"'.format(str_text) # 20 caracteres completados com traços à esquerda
print(str_test)
str_test = '"{:^20}"'.format(str_text) # 20 caracteres completados com a string ao meio
print(str_test)

# Formatação numeros
str_test = "'{:4d}'".format(int_text) # int com 4 characteres
print(str_test)
str_test = "'{:06.2f}'".format(float_text) # float com 6 caracteres e 2 casas decimais
print(str_test)

# Formatação de datas
str_data = datetime.now()
print(str_data)
str_test = "'{:%Y/%m/%dT%H-%M-%S}'".format(str_data) # int com 4 characteres
print(str_test)

