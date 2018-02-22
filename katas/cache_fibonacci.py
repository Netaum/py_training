# A função abaixo representa a solução de fibonacci de maneira simples.None
# Entretanto, para numeros grandes (> 50) a função leva tempo demais, uma vez que ela calcula valores
# que já foram computados.
# Reescreva a função de forma que ela utilize de alguma forma de cache para numeros já calculados.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

assert fibonacci(70) == 190392490709135
assert fibonacci(60) == 1548008755920
assert fibonacci(50) == 12586269025