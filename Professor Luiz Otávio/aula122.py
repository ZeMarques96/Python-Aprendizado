# Exercícios LISTA DE TAREFAS
import os
import json

tarefas = []
apagados = []


def ler(tarefas):
    temporarios = []
    try:
        with open('lista_de_tarefas.json', 'r', encoding='utf8') as file:
            temporarios = json.load(file)
        if tarefas != []:
            while True:
                resposta = input('Deseja adicionar os itens carregados aos itens existentes na lista? [S/N]').upper()
                if resposta not in 'SsNn':
                    print('RESPOSTA INVÁLIDA')
                    print()
                else:
                    break
            if resposta == 'N':
                for c in range(len(tarefas)):
                    tarefas.pop()
        for temporario in temporarios:
            tarefas.append(temporario)
        return tarefas
            
    except FileNotFoundError:
        print('Nenhum Arquivo .json encontrado para carregar.')

def salvar(tarefas):
    with open('lista_de_tarefas.json', 'w', encoding='utf8') as file:
        json.dump(tarefas, file,ensure_ascii=False, indent=2)

def adicionar(tarefas, acao):
    if acao == 'sair':
        return
    tarefas.append(acao)
    print(f'Tarefa {acao} adicionada na lista de tarefas.')

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
    print('Comandos: listar, desfazer, refazer, sair(para sair), ler, salvar.', )
    acao = input('Digite uma tarefa ou um comando:').lower().strip()
    print()
    if acao == 'sair':
        break
    comandos = {
        'listar' : lambda : listar(tarefas),
        'desfazer' : lambda : desfazer(tarefas),
        'refazer' : lambda : refazer(tarefas, apagados),
        'listar' : lambda : listar(tarefas),
        'clear' : lambda : os.system('cls'),
        'adicionar' : lambda : adicionar(tarefas, acao),
        'salvar' : lambda : salvar(tarefas),
        'ler' : lambda : ler(tarefas),
    
    }
    
    comando = comandos.get(acao) if comandos.get(acao) is not None else comandos['adicionar']
    comando()

