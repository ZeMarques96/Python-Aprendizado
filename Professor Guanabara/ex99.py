import random

lista1 = [random.randint(1,20) for x in range(10)] # APENAS PARA A CONSTRUÇÃO DO ALGORÍTIMO

lista6 = []

def maior_encontrado(*args):
    maior = 0
    print('valores a serem analisados...')
    if len(args) != 0:    
        for numero in args:
            print(numero, end=' ')
            if numero > maior:
                maior = numero
        print()
    print(f'Foram informados {len(args)} ao todo.')
    print(f'O maior número encontrado foi {maior}')
    print('-'*40)
    
maior_encontrado(1,5,6,7)
maior_encontrado()
