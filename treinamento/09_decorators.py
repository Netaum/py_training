# Decoradores são formas de se extender métodos existentes em python
# Bem parecidos com os extension methods do C#

#antes de falarem algo: https://duvidas.dicio.com.br/cumprimentar-ou-comprimentar/
def cumprimentar(nome):
    return f'Olá {nome}!'

# Em python, métodos podem ser atribuídos à variáveis
ola = cumprimentar
print(ola('Neto'))

# Podemos, inclusive, declarar métodos dentro de métodos

def cumprimentar2(nome):
    def mensagem():
        return 'Olá'
    
    return f'{mensagem()} {nome}!'

print(cumprimentar2('Joseph'))

# Funções podem ser passadas por parametros para outras funções

def chamada_func(func):
    outro_nome = 'Mira'
    return func(outro_nome)

print(chamada_func(cumprimentar))

# Funções podem retornar outras funções 

def cumprimentar_composto():
    def mensagem():
        return 'Olá !!!'

    return mensagem

ola = cumprimentar_composto()
print(ola())

# Funções internas conseguem acessar o escopo das funções externas

def cumprimentar3(nome):
    def mensagem():
        return f'E ai {nome}, tudo bom ?'

    return mensagem

ola = cumprimentar3('Gordin')
print(ola())

# Decoradores são simplesmente wrappers que colocamos em uma função

def get_text(nome):
    return f'lorem ipsum, {nome} dolor sit amet'

def f_decorate(func):
    def func_wrapper(nome):
        return f'<p>{func(nome)}</p>'

    return func_wrapper

texto = f_decorate(get_text)
print(texto('Maria'))

# Usando um pouco de syntax sugar

@f_decorate
def get_text2(nome):
    return f'At vero eos et accusamus et iusto odio {nome}'

print(get_text2('Ronaldo'))