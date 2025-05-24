# Julia Leandro | RA: 25009148

import task_manager
from task_manager import select_option

# Uso da função Console() para estilizar a impressão, e função Panel() para exibir o menu dentro de um 'quadro' com borda
from rich.console import Console
from rich.panel import Panel


console = Console()

menu_options = (
    "[bold cyan]Gerenciador de Tarefas[/bold cyan]\n\n"
    "[bold]1[/bold] - Nova tarefa\n"
    "[bold]2[/bold] - Listar todas as tarefas\n"
    "[bold]3[/bold] - Listar tarefas pendentes\n"
    "[bold]4[/bold] - Concluir tarefa\n"
    "[bold]5[/bold] - Remover tarefa\n"
    "[bold]6[/bold] - Sair"
)


while True:
    # Exibe o menu de opções dentro de um painel com título 'Menu'
    console.print(Panel(menu_options, title="Menu", expand=False))
    option = int(input("Opção: "))
    select_option(option)

