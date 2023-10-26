import os

# cor_branca = "\033[97m"
# cor_vermelha = "\033[91m"
# cor_verde = "\033[92m"
# cor_amarela = "\033[93m"
# cor_azul = "\033[94m"
# cor_reset = "\033[0m"

def chama_help(comando):
    help(comando)




control = 0
while True:
    comando = input('Função ou Biblioteca > ').lower()
    control += 1
    if control == 2:
        os.system('cls')
        control = 0
    if comando != 'fim':
        chama_help(comando)
    if comando == 'fim':
        break