# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y




def multiplicador(x, y):
    return x * y
    

def cria_funcao(funcao, x):
    def interna(y):
        return funcao(x ,y)
    return interna




soma_com_cinco = cria_funcao(soma, 5)
multiplica_por_dez = cria_funcao(multiplicador, 10)


print(soma_com_cinco(10))
print(multiplica_por_dez(10))




