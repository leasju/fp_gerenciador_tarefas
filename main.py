# Julia Leandro | RA: 25009148

import task_manager
from task_manager import select_option

while True:
    option = int(input("\nGerenciador de Tarefas\n\n"
                       "1 - Nova tarefa\n"
                       "2 - Listar tarefas\n"
                       "3 - Concluir tarefa\n"
                       "4 - Remover tarefa\n"
                       "5 - Sair\n\n"
                       "Opção: "))
    select_option(option)


