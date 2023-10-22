"""Calculadora"""
resposta = ''
operadores_permitidos = '+-*/'
while True:
    n1 = input('Digite um valor: ')
    operador = input('Digite um operador matemático para a execução da conta: (+, -, *, /) ')
    n2 = input('Digite outro valor: ')
    if operador not in operadores_permitidos:
        print('O operador digitado é inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
    try:
        n1 = float(n1)
        n2 = float(n2)
        if operador == '+':
            print(f'{n1+n2}')
        elif operador == '-':
            print(f'{n1-n2}')
        elif operador == '*':
            print(f'{n1*n2}')
        elif operador == '/':
            print(n1/n2)
    except:
        print('Um ou ambos os valores informados são inválidos')
        continue
    resposta = input('Quer sair? [Sim] [Não] ').lower().startswith('s')

    if resposta :
        break

print('Programa Encerrado!')