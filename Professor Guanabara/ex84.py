import copy

pessoas = []
dados = []
pessoas_pesadas = []
pessoas_leves = []
maior = menor = 0

while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(int(input('Digite o seu peso: ')))
    if len(pessoas) == 0 or dados[1] < menor:
        menor = copy.copy(dados[1])
    if dados[1] > maior:
        maior = copy.copy(dados[1])

    pessoas.append(dados[:])
    if dados[1] >= 100:
        pessoas_pesadas.append(dados[:])
    if dados[1] < 100:
        pessoas_leves.append(dados[:])
    dados.clear()
    continua = str(input('Quer continuar? [S/N]')).upper()
    
    if continua in 'N':
        break
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
if len(pessoas_pesadas) == 0:
    for c in pessoas:
        if c[1] == maior:
            print(c[0], end= ' ')
    
for pessoa in pessoas_pesadas:
    if pessoa[1] == maior:
        print(pessoa[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa in pessoas_leves:
    if pessoa[1] == menor:
        print(pessoa[0], end=' ')




