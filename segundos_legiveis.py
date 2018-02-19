# Escreva uma função que receba o numero de segundos em um inteiro, e retorne
# o tempo em uma forma legível para seres humanos
# Ex: hora_legivel(5) == "00:00:05", hora_legivel(60) == "00:01:00"
# O número é inteiro acima de 0 e abaixo de 359999 (99:59:59)
# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def hora_legivel(segundos):
    return None

assert hora_legivel(0) == "00:00:00"
assert hora_legivel(5) == "00:00:05"
assert hora_legivel(60) == "00:01:00"
assert hora_legivel(86399) == "23:59:59"
assert hora_legivel(359999) == "99:59:59"
