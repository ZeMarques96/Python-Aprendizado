import copy

a = [[15, 3], 22, 31, 16, 28, 37]
b = copy.deepcopy(a)
b[0][0] = 'aoba'

print(a)
print(b)