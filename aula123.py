# Controlando a quantidade de argumentos posicionais e nomeados em funções *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional - only parameters (/) - Tudo antes da barra deve ser APENAS posicional
# PEP 570 - Python Positional - Only Parameters
# KeyWord- Only Arguments (*) - * sozinho SÃO SUGA valores
# PEP 3102 - Keyword - Only Arguments

def soma( a , b, /, x , y) :
    print(a + b + x + y)


def soma1( a , b, *, x , y) :
    print(a + b + x + y)

soma(1 , 2, y = 3)
soma(1 , 2)