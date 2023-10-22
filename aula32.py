n1 = input('Digite um número inteiro: ')
try:
    n1 = int(n1)
    if n1 % 2 == 0:
        print(f'O número {n1} é PAR')
    else:
        print(f'O número {n1} é ÍMPAR')
except:
    print('Apenas números inteiros')
