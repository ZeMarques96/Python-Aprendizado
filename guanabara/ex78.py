lista = [
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
]
maior_valor = max(lista)
menor_valor = min(lista)
print(f'O menor valor digitado foi {min(lista)} e se encontra nas posições:', end=' ' )
for menor in range(len(lista)):
    if lista[menor] == menor_valor:
        print(menor, end='...')
print()
print(f'O menor valor digitado foi {max(lista)} e se encontra nas posições:', end=' ' )
for maior in range(len(lista)):
    if lista[maior] == maior_valor:
        print(maior, end='...')
