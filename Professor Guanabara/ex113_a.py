# RESOLUÇÃO FEITA DE MANEIRA ADEQUADA 

def leiaInt():
    while True:
        try:
            numero = input('Digite um número inteiro:')
            numero = int(numero)
            break
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            numero = 0
            break
    return numero


def leiaFloat():
    while True:
        try:
            numero = input('Digite um número Real:')
            numero = float(numero)
            break
        except (ValueError, TypeError):
            print('ERRO: digite um número real.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            numero = 0
            break


    return numero


inteiro = leiaInt()
flut =leiaFloat()

print(f'O número inteiro digitado foi {inteiro} e o Real foi {flut}')
