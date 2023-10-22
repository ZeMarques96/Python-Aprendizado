tupla = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    ) 
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print('O número 3 foi digitado no index:  ', tupla.index(3))
else:
    print('O número 3 não foi digitado')
valores_pares = (
    par for par in tupla
    if par % 2 == 0
)
print('Os valores pares digitados foram: ', end='')
print(*valores_pares)