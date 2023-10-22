"""
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas 
# Tipos imutáveis como valor interno."""

# Criando um set
# set(iterável ou {1, 2, 3})

# Sets são eficientes para remover valores duplicados de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)


# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update('Olá Mundo')
# print(s1)
# s1.update(('Olá Mundo', 1, 2, 3))
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos 
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3, 'a'}
s2 = {2, 3, 4, 'A'}
s3 = s1 | s2
print(s3, 'União')
s4 = s1 & s2
print(s4, 'Intersecção')
s5 = s1 - s2
print(s5, 'Mostra o que está contido apenas no da esquerda')
s6 = s1 ^ s2
print(s6, 'Itens que não estão em ambos')