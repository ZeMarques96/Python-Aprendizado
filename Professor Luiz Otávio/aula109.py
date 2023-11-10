# count é um iterador sem fim

from itertools import count


c1 = count()


print(hasattr(c1, '__iter__'))
# for i in range(100):
#     print(next(c1))

for i in c1:
    print(i)
    if i == 15:
        break

