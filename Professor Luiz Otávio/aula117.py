# Criando arquivos com Python
# Usamos a função open para abrir um arquivo (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação), a (escreve no final), b (binário), t (modo texto), + (leitura e escrita)
import datetime
# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho = 'E:\\Curso de Programação\\Udemy\\Python\\aulas\\Professor Luiz Otávio\\arquivos\\'
novo_arquivo = caminho + 'aula117.txt'

# QUANDO SE ABRE UM ARQUIVO TEM QUE FECHAR
# arquivo = open(novo_arquivo, 'w')

# arquivo.close()

# with open(novo_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.write(f'{5 + 5}\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     arquivo.seek(0, 0)
#     print('Lendo')
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

# print('#' * 15)
# with open(novo_arquivo, 'r') as arquivo:
#     print(arquivo.read())
# local_data = datetime.datetime.now()
# data_formatada = local_data.strftime("%Y-%m-%d %H:%M:%S")


with open(novo_arquivo, 'w', encoding='utf-8') as arquivo:
    
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write(f'{5 + 5}\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    # arquivo.write(data_formatada + '\n')