

def verificador_primos(numero): 
    if numero % 2 ==0:
        return f'O número {numero} é PAR'
    return f'O número {numero} é ÍMPAR'


while True:
    numero = int(input('Digite um número: '))
    print(verificador_primos(numero))