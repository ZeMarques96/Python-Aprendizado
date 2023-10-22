#              0          1        2         3 
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#print(len(lanche))
for cont in range(len(lanche)):
    print(lanche[cont])
print()
for comidas in lanche:
    print(comidas)
print()

for pos,comida in enumerate(lanche):
    print(pos,comida)
print()

print(lanche.sort())