# from sys import path

# import aula99_package.modulo # 1
# from aula99_package.modulo import soma_do_modulo,fala_oi # 2
# from aula99_package import modulo # 3

# from aula99_package import modulo_b




# print(__name__)
# print(soma_do_modulo(1,1)) # 2
# print(aula99_package.modulo.soma_do_modulo(1,1))  # 1
# print(modulo.soma_do_modulo(1,1)) # 3
# modulo_b.fala_oi()
# fala_oi()

from aula99_package import modulo


print(modulo.fala_oi())