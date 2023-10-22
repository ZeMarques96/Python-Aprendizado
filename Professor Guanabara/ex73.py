tabela_brasileirao = (
    'BOTAFOGO', 'RED BULL BRAGANTINO', 'GREMIO', 'PALMEIRAS', 'ATHLETICO-PR', 'FLAMENGO',
      'FORTALEZA', 'FLUMINENSE', 'ATLÉTICO-MG', 'CUIABÁ', 'SÃO PAULO', 'INTERNACIONAL', 
      'BAHIA', 'CRUZEIRO', 'CORINTHIANS', 'VASCO', 'SANTOS', 'GOIÁS', 'CORITIBA', 'AMÉRICA-MG'
      )

print(f'Os 5 primeiros colocados são')
for cont in range(5):
    print(f'{cont+1}° {tabela_brasileirao[cont]}', end=' ')
print('\n')

print('Os quatro ultimos colocados são: ', *tabela_brasileirao[16:], sep=' ')
print('Os quatro ultimos colocados são: ', *tabela_brasileirao[-4:], sep=' ')
print()
print('A lista em ordem alfabética é: ')
tabela_organizada = list(tabela_brasileirao)
tabela_organizada.sort()
for rank in range(len(tabela_organizada)):
    print(rank + 1, tabela_organizada[rank])
print('O Corinthians está na posição:', tabela_brasileirao.index('CORINTHIANS') + 1)