# Problema dos parâmetros mutávies em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes = adiciona_clientes('José')
adiciona_clientes('Eloá', clientes)
clientes1 = adiciona_clientes('Cleito')
adiciona_clientes('Chico', clientes1)
print(clientes)
print(clientes1)