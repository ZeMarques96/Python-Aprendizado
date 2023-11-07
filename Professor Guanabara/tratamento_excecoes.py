

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except ZeroDivisionError:
    print('Zero não é um número divisível')

except ValueError:
    print('ERRO!Por favor digite um número!')

except KeyboardInterrupt:
    print('Encerramento forçado!')

else: #Caso não ocorra nenhuma exceção
    print(f'O resultado é {r}')

finally:
    print('Muito obrigado, volte sempre!!')