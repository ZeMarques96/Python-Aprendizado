# pessoas = []
pessoas = [
    {
        'nome': 'José',
        'sexo': 'M',
        'idade': 35,
    },
    {
        'nome': 'Paula',
        'sexo': 'F',
        'idade': 35,
    },
    {
        'nome': 'Maria',
        'sexo': 'F',
        'idade': 15,
    },
    ]
# while True:
#     pessoa = {}
#     pessoa['nome'] = str(input('Nome: '))
#     pessoa['sexo'] = str(input('Sexo: [M/F]'))
#     pessoa['idade'] = int(input('idade:'))
#     pessoas.append(pessoa)
#     while True:
#         resposta = str(input('Quer continuar? '))
#         if resposta in 'Nn':
#             break
#         if resposta in 'Ss':
#             break
#     if resposta in 'Nn':
#         break
tamanho_da_lista = len(pessoas)
tot_idade = 0
lista_de_mulheres = []
acima_da_media = []
print(f'- O grupo tem {tamanho_da_lista} pessoas.')
for valores in pessoas:
    if valores['sexo'] in 'Ff':
        lista_de_mulheres.append(valores['nome'])
    for chave, valor in valores.items():
        if chave == 'idade':
            tot_idade += valor
media_de_idade = tot_idade / tamanho_da_lista
print(f'- A média de idade é de {media_de_idade:.2f} anos.')
print('- As mulheres cadastradas foram: ', end=' ')
for mulheres in lista_de_mulheres:
    print(mulheres, end='; ')
for acima in pessoas:
    if acima['idade'] > media_de_idade:
        acima_da_media.append(acima)
print(f'\n- Lista de pessoas acima da média: ')
for acima in acima_da_media:
    for chave, valor in acima.items():
        print(chave, valor, end= '; ')
    print('\n')
