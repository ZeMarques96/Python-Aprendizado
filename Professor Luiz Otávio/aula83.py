#Empacotamento e desempacotamento de dicionários
# a ,b = 1, 2
# a, b = b, a

# print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}


l1= [f for f in range(10)]

print(l1)
#print(pessoa_completa)

def argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)
    #return args, kwargs

#teste = argumentos_nomeados('aoba', nome='josé', idade= 26)

argumentos_nomeados(*l1, **pessoa_completa)
