# Para definir um método em python, simplesmente utilize a designação def

def funcao1():
    print('minha funcao')

def funcao2(param1, param2):
    print(f'{param1} -- {param2}')

def funcao3(param1, param2=4):
    funcao2(param1, param2)

funcao1()
funcao2(1, 'teste')
funcao3(5)
funcao3(6,'teste')


class NomeClasse(object):
    def __init__(self):
        self.id = 1

    def func(self, value):
        NomeClasse.func1(self.id + value)

    @staticmethod
    def func1(value):
        print(value)

    def __private(self, value):
        NomeClasse.func1(self.id + value)

var_classe = NomeClasse()
var_classe.func(10)
NomeClasse.func1('Teste')