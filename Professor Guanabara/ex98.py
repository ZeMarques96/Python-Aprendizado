import time

def contador(i,f,p):
    
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if f < i and p > 0:
        p = p * -1
        f -= 1
    else:
        f += 1
    for x in range(i,f,p):
        print(x, end='..')
        time.sleep(0.2)
    print()
    print('-' * 50)

contador(10,20, 1)
contador(20,10, 1)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)