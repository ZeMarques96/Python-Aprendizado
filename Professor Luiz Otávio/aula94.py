# try, except, else e finally
# Finally sempre será executado

try:
    print('Abriu arquivo')
    8/0
except ZeroDivisionError:
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')

