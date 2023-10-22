lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        resposta = str(input('Deseja continuar? [S/N]')).upper()

        if resposta == 'N':
            break
        if resposta == 'S':
            break
        else:
            print('Resposta inválida')
    if resposta == 'N':
        break
print(f'Foram digitados {len(lista)} números nesta lista.')

print(f'A lista ordenada de forma decrescente é {sorted(lista, reverse=True)}')
print(lista)
if 5 in lista:
    print(f'O valor 5 foi digitado na lista e se econtra no index {lista.index(5)}')
else:
    print('O valor 5 não se encontra na lista')