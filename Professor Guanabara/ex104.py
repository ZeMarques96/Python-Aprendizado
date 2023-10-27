

def leiaInt(string):
    while True:
        inteiro = input(string)
        if inteiro.isnumeric():
            inteiro = int(inteiro)
            break
        else:
            print('\033[0;31mERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m ')
    return inteiro

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')