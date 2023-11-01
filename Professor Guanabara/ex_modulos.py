from utilidadescev import moeda
from utilidadescev import dados
preco = dados.validador('Digite um preço: R$')
# print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
# print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
# print(f'Aumentando  10%, temos {moeda.aumentar(preco, 10, False)}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, False)}')
moeda.resumo(preco, 35, 22, True)