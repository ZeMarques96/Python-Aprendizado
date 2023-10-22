lista = []
numero_inserido_pelo_usuario = 0
for c in range(5):
    numero_inserido_pelo_usuario = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(numero_inserido_pelo_usuario)
        print('Número adicionado no final da lista...')
    if len(lista) == 1:
        if numero_inserido_pelo_usuario > lista[0]:
            lista.append(numero_inserido_pelo_usuario)
            print('Número adicionado no final da lista...')
            continue
        if numero_inserido_pelo_usuario < lista[0]:
            lista.insert(0, numero_inserido_pelo_usuario)
            print('Número adicionado na posição 0 da lista...')
            continue
    if len(lista) != 1:
        for valor in range(len(lista)):
            if numero_inserido_pelo_usuario < lista[0]:
                print('Número adicionado na posição 0 da lista...')
                lista.insert(0,numero_inserido_pelo_usuario)
                break
            if numero_inserido_pelo_usuario > lista[-1]:
                lista.append(numero_inserido_pelo_usuario)
                print('Número adicionado no final da lista')
                break
            if numero_inserido_pelo_usuario > lista[valor] and numero_inserido_pelo_usuario < lista[valor + 1]:
                lista.insert(valor+1, numero_inserido_pelo_usuario)
                print(f'Número adicionado na posição {valor+1} da lista...')
                break


print('Os valores digitados foram: ', *lista)