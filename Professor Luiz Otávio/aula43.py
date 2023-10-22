texto = 'José' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break