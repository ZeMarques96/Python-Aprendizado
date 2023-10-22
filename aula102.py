# Variáveis livres + nonlocal (locals, globals) 


# def fora(x):
#     a = x

#     def dentro():
#         return a
#     return dentro


# dentro = fora(5)

# print(dentro())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')



print(c('b'))
print(c('c'))
print(c('d'))
print(c('e'))
