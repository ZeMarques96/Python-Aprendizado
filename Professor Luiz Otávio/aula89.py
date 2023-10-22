# dir, hasattr e getattr em python

string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe Upper')
    print(getattr(string, metodo)())
else:
    print(f'O método {metodo} não existe')