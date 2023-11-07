# I IDEÁ DESSE EXERCÍCIO FOI FAZER UMA FUNÇÃO PARA TRATAMENTO DE EXCEÇÕES

def tratamentodeExecoes(inteiro, tipo='inteiro'):
    try:
        if tipo == 'inteiro':
            numero = int(inteiro)
            return numero
        
        elif tipo == 'flutuante':
            numero = float(inteiro)
            return numero
        
        if numero.is_integer():
            erro = 'O número digitado é um número inteiro'
            return erro
        
    except ValueError:
            erro = 'ValueError, valor digitado é uma string ou um número float'
            return erro
    except KeyboardInterrupt:
            erro = KeyboardInterrupt.__name__
            return erro
        

def leiaInt():
    while True:
        numero = input('Digite um número inteiro: ')
        resultado = tratamentodeExecoes(numero, 'inteiro')
        if type(resultado) == int:
            break
        else:
            print(resultado)
    return resultado

def leiaFloat():
    while True:
        numero = input('Digite um número Flutuante: ')
        resultado = tratamentodeExecoes(numero, 'flutuante')
        if type(resultado) == float:
            break
        # Não funcionou no code runner
        if resultado == 'KeyboardInterrupt':  
             print('O usuário prefiriu não digitar esse número')
             numero = 0
             break
        else: print(resultado)
    
    return resultado

inteiro = leiaInt()
flutuante = leiaFloat()

print(f'O valor inteiro digitado foi {inteiro} e o real foi {flutuante}')