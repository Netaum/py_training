# Escreva um método que valide se um IP é válido
# Valido: 1.2.3.4, 123.321.67.9
# Invalido: 1.2.3, 1.2.3.4.5, A.2.3.4

def ip_valido(ip):
    return None


assert ip_valido("1.2.3.4") == True
assert ip_valido("123.456.789.0") == True
assert ip_valido("12.34.56") == False
assert ip_valido("abc.def.ghi.jkl") == False
