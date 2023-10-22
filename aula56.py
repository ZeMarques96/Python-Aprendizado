"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_frase = frase.split(', ')
print(lista_frase)
for i, frase in enumerate(lista_frase):
    print(frase.strip())