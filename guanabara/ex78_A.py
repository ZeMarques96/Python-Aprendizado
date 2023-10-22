lista = []
mai = 0
men = 0
for c in range(5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'O maior valor digitado foi foi {mai} e ele aparece nas posições: ', end='')
for c, v in enumerate(lista):
    if v == mai:
        print(f'{c}...' , end='')
print()
print(f'O menor valor digitado foi foi {men} e ele aparece nas posições: ', end='')
for c, v in enumerate(lista):
    if v == men:
        print(f'{c}...' , end='')