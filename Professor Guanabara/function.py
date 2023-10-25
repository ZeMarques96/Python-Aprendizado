# def divisoria(string):
#     print('-'*30)
#     print(f'{string:^30}')
#     print('-'*30)

# divisoria('TABELA')
# divisoria('CADASTRO DE JOGADORES')
# divisoria('CIRCO')


# def soma (*args):
#     tot = 0
#     print('Valores recebidos', *args)
#     for x in args:
#         tot += x
#     return tot

# print(soma(1,2,3,4,5))


def multiplica(x):
    def dobra(lista):
        dobrado = []
        for valor in lista:
            dobrado.append(valor * x)
        return dobrado
    return dobra



simples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobrado = multiplica(2)
print(dobrado(simples))
dobrado = multiplica(3)
print(dobrado(simples))
dobrado = multiplica(4)
print(dobrado(simples))

