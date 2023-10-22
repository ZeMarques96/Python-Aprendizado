import os

lista = []
while True:
    print('Selecione uma opção:')
    escolha = input(' [i]nserir [a]pagar [l]istar: ').lower()
    try:
        escolha = int(escolha)
        print('números não são uma opção')
        continue
    except:
        if len(escolha) > 1:
            print('Opção inválida!')
            continue
        elif escolha.startswith('i'):
            print('Digite o nome do item que deseja inserir: ')
            lista.append(input())

        elif escolha.startswith('a'):
            if len(lista) == 0:
                print('Lista Vazia, não há nada para apagar!')
                continue
            apagar = input('Digite o índice do item que deseja apagar: ')
            try:
                apagar = int(apagar)
                print(f'Item {lista[apagar]} no Índice {apagar} foi apagado!')
                lista.pop(apagar)
            except:
                print('Desculpe índice inválido!')
                    
        elif escolha.startswith('l'):

            if len(lista) == 0:
                print('Não há nada para listar!')
            os.system('cls')
            for indice, item in enumerate(lista):
                print(indice,item)
        else:
            print('Opção inválida')