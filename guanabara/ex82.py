# lista = [1,2,3,4,5,6,7,8,9,10]
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

pares = [
    par for par in lista
    if par % 2 == 0
    ]
impares = [
    impar for impar in lista
    if impar % 2 != 0
]

print(f'A lista original é : ', *lista)
print(f'Os números pares da lista são: ', *pares)
print('Os números impares da lista são: ',*impares)