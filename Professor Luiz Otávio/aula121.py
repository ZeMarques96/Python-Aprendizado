# Exercícios LISTA DE TAREFAS
import os

comandos = ['listar', 'desfazer', 'refazer', 'sair', 'clear']
tarefas = []
apagados = []




def listar(tarefas):
    print()
    if not tarefas:
        print('LISTA DE TAREFAS ESTÁ VAZIA')
        print()
        return
    print('-'*13)
    print(f'{"   TAREFAS"}')
    print('-'*13)
    for tarefa in tarefas:
        print(f'- {tarefa}')
    print()

def desfazer(tarefas):
    print()
    if not tarefas:
        print('-' * 27)
        print('Nada mais para ser desfeito'.upper())
        print('-' * 27)
        return
    
    ultimo = tarefas[-1]
    apagados.append(ultimo)
    print(f'Tarefa {ultimo} removida da lista de tarefas.')
    tarefas.pop()
    print()

def refazer(tarefas, apagados):
    if not apagados:
        print('-' * 21)
        print('Nada para ser refeito'.upper())
        print('-' * 21)
        return
    tarefas.append(apagados[-1])
    print(f'Tarefa {apagados[-1]} retornada a lista de tarefas.')
    apagados.pop(-1)
    print()
    

while True:
    print()
    print('Comandos: listar, desfazer, refazer, sair(para sair)')
    acao = input('Digite uma tarefa ou um comando:').lower().strip()
    print()
    if acao not in comandos:
        tarefas.append(acao)
        print(f'Tarefa {acao} adicionada na lista de tarefas.')
    elif acao == 'listar':
        listar(tarefas)
    elif acao == 'desfazer':
        desfazer(tarefas)
        listar(tarefas)

    elif acao == 'refazer':
        refazer(tarefas,apagados)
        listar(tarefas)

    elif acao == 'clear':
        os.system('cls')
        listar(tarefas)
    elif acao == 'sair':
        break
