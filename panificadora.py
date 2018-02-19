# Escreva um código que, dada a receita e os ingredientes, fale quantas unidades 
# são possíveis de serem feitas
# Exemplo: 
# receita = {"farinha": 500, "acucar": 200, "ovos": 1}
# ingredientes = {"farinha": 1200, "acucar": 1200, "ovos": 5, "leite": 200}
# assar(receita, ingredientes) == 2
# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def assar(receita, ingredientes):
    return None



receita = {"farinha": 500, "acucar": 200, "ovos": 1}
ingredientes = {"farinha": 1200, "acucar": 1200, "ovos": 5, "leite": 200}
assert assar(receita, ingredientes) == 2

receita = {"peras": 3, "farinha": 300, "acucar": 150, "leite": 100, "olho": 100}
ingredientes = {"acucar": 500, "farinha": 2000, "leite": 2000}
assert assar(receita, ingredientes) == 0