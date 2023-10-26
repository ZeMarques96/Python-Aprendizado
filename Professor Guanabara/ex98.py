import time

def contador(inicio,fim,passo):
    """
    -> Faz uma contagem e mostra na tela.
    inicio : início da contagem
    fim : fim da contagem
    passo : passo da contagem
    retrun : sem retorno
    """
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if fim < inicio and passo > 0:
        passo = passo * -1
        fim -= 1
    else:
        fim += 1
    for x in range(inicio,fim,passo):
        print(x, end='..')
        time.sleep(0.2)
    print()
    print('-' * 50)
    
contador(1,10, 1)
contador(10,0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)