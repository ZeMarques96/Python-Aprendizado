lista = []
resposta= ''
coletor = 0

while True:

    coletor = int(input('Digite um valor: '))

    if coletor not in lista:
        lista.append(coletor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado!')

    resposta = str(input('Quer Continuar? [S/N]')).upper()
    
    if resposta == 'N':
        break
    if resposta != 'S':
        print('Resposta inválida!')
print(f'Os valores inseridos na lista em ordem crescente foram {sorted(lista)}')
        
