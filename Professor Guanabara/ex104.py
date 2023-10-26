

def leiaInt(string):
    while True:
        inteiro = input(string)
        try :
            inteiro = int(inteiro)
            break
        except:
            print('ERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO ')
    return inteiro

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')