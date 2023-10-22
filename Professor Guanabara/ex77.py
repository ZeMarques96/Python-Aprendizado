tupla = ('arroz', 'feijao', 'queijo','coca-cola', 'batata')

for palavra in tupla:
    print(f'As vogais da palavra {palavra} são:', end=' ')
    for vogais in palavra:
        if vogais in 'aeiou':
            print(vogais, end=' ')
    print()