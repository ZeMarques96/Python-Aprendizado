# Generator expression, Iterable e Iterators em Python
import sys 

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()# tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)