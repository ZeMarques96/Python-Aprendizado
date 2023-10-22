import random

tupla = tuple(random.randint(1, 100) for _ in range(5))
print('Os valores sorteados foram: ',end='')

for x in tupla:
    print(x, end=' ')
print()
print(f'O maior número foi: {max(tupla)}')
print(f'O menor número foi: {min(tupla)}')
