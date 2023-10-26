

def fatorial(numero, show=False):
    """
    fatorial(numero, show=False)
        -> Calcula o Fatorial de um número.
        :param numero: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial do parâmetro numero.
    """
    fatorial = 1
    for x in range(numero, 0, -1):
        fatorial *= x
        if show:
            print (x, end=' x ')
    if show:
        print('= ',end='')
    return fatorial


print(fatorial(5, show=True))
print(fatorial(4))
print(fatorial(3, show=False))
help(fatorial)