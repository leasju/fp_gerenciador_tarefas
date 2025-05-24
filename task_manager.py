# Julia Leandro | RA: 25009148
# task_manager.py

import sys
from rich.console import Console 
from rich.table import Table 

tasks = {}

# --------- AÇÕES ---------

# Criação de tarefas
def create_task(tasks, title, description=""):
    tasks[title] = {
        "Descrição" : description,
        "Feita": False
    }
    return print(f"Nova tarefa '{title}' adicionada com sucesso.")

# Listagem de tarefas
def list_tasks():
    # Verifica se há tarefas cadastradas
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    
    """ 
    A exibição da lista em tabela foi inspirada na documentação da biblioteca Rich fornecida pelo site FreeCodeCamp
    Fonte: https://www.freecodecamp.org/news/use-the-rich-library-in-python/

    """
    # Lista as tarefas em forma de tabela para melhor visualização
    table = Table(title="Tarefas")

    table.add_column("Índice", style="cyan", no_wrap=True) # Exibe o índice da tarefa
    table.add_column("Tarefa", style="yellow") # Exibe o título da tarefa
    table.add_column("Status", justify="center", style="green") # Exibe o status da tarefa

    for i, (title, data) in enumerate(tasks.items(), start=1): 
        status = "✅" if data["Feita"] else "❌" # Definição do status da tarefa
        table.add_row(str(i), title, status)

    console = Console()
    console.print(table)

# Conclusão de tarefas
def mark_complete(task_number):
    # Verifica se há tarefas cadastradas
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    
    # Verificação do índice inserido pelo usuário
    if task_number < 1 or task_number > len(tasks):
        return print("Número de tarefa inválido, tente novamente.")
    
    # Transformando as chaves (títulos) em uma lista 
    title = list(tasks.keys())[task_number - 1]
    tasks[title]["Feita"] = True # Torna o status da tarefa como "Concluída"
    print(f"Tarefa '{title}' marcada como concluída.")

# Remoção de tarefas
def remove_task(task_number):
    # Verifica se há tarefas cadastradas
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    
    # Verificação do índice inserido pelo usuário
    if task_number < 1 or task_number > len(tasks):
        print("Número de tarefa inválido, tente novamente.")
    
    # Transformando as chaves (títulos) em uma lista 
    title = list(tasks.keys())[task_number - 1]
    del tasks[title] # Remove a tarefa
    print(f"Tarefa '{title}' removida com sucesso.")


# --------- SELEÇÃO DE OPÇÕES ---------

# Chama a função correta com base na escolha do usuário
def select_option(option):
    # Uso do 'lambda' para adiar a execução da função até a escolha do usuário
    mapa_op = {
        1 : lambda : create_task(tasks, input("Título: "), input("Descrição: ")),
        2 : list_tasks,
        3 : lambda : list_tasks,
        3: check_mark_complete,
        4: check_remove_task,
        5 : sys.exit
    }

    if option in mapa_op:
        return mapa_op[option]()
    else: 
        return print("Ação inexistente")

# --------- FUNÇÕES AUXILIARES (ou funções handlers)---------
# Funções handlers são funções criadas para lidar com eventos ou situações específicas, controlando o que deve acontecer quando algo ocorre no programa.

"""
Uso de funções auxiliares 'check...()'

Motivo: Durante a execução do código, notei que ao selecionar as opções "Concluir tarefa" ou "Remover tarefa" sem ter tarefas cadastradas, as funções 'mark_complete' e 'remove_task' ainda pediam o índice da tarefa, mesmo não tendo nenhuma.

Essas funções verificam se há tarefas cadastradas ANTES de solicitar o índice. Se não houver tarefas, elas exibem a mensagem "Nenhuma tarefa cadastrada.", sem o input desnecessário.

"""
def check_mark_complete():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    list_tasks() # Lista as tarefas existentes antes de solicitar o índice
    mark_complete(int(input("Índice da tarefa: ")))

def check_remove_task():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    list_tasks() # Lista as tarefas existentes antes de solicitar o índice
    remove_task(int(input("Índice da tarefa: ")))
