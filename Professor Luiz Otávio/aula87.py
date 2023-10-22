# isinstance - para saber se o objeto é de determinado tipo

lista = ['a', 1, 1.1, False, [0, 1, 2], (1,2), {0, 1}, {'nome': 'Luiz'},]

print(lista)

for item in lista:
    
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item)

    if isinstance(item, bool):
        print('BOOL')
        item = True
        print(item)

    if isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))

    if isinstance(item, (int, float)):
        print('int')
        print(item, item * 2)