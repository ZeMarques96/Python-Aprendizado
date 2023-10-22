# pessoa = {'nome': 'Pedro', 'idade': 25 }
# pessoa['sexo'] = 'M'

# print(pessoa)
# del pessoa['sexo']
# print(pessoa)

# filme = [
#     {
#     'titulo': 'StarWars',
#     'ano': 1977,
#     'diretor': 'George Lucas',
# },
#     {
#     'titulo': 'Avengers',
#     'ano': 2012,
#     'diretor': 'Joss Whedon',   
#     },
#     {
#     'titulo': 'Matrix',
#     'ano': 1999,
#     'diretor': 'Wachowski',   
#     },
# ]

locadora = [
    {
    'titulo': 'StarWars',
    'ano': 1977,
    'diretor': 'George Lucas',
},
    {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon',   
    },
    {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski',   
    },
]
#locadora.append(filme)
print(locadora[0]['ano'])
print(locadora[2].items())

# print(filme.values())
# print(filme.keys())
# print(filme.items())

# for k,v in filme.items():
#     print(f'O {k} é {v}')