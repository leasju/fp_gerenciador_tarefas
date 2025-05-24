<h1>📝 Gerenciador de Tarefas em Python</h1>
 <p> Este repositório contém o projeto desenvolvido para a disciplina <strong>Fundamentos de Programação em Python</strong>, ministrada pelo professor <strong>Denis Martins</strong>, da <strong>PUC Campinas</strong>. </p> 
 <p> O objetivo principal foi criar um módulo Python personalizado que permita o gerenciamento de tarefas, utilizando conceitos fundamentais da linguagem como <strong>funções, estruturas de dados e modularização</strong>. </p>

<h2>📂 Conteúdo do Repositório</h2> <ul> 
<li><code>task_manager.py</code> – Módulo com as funções de criação, listagem, conclusão e remoção de tarefas</li> 
<li><code>main.py</code> – Script principal com menu interativo no terminal para uso do gerenciador</li>
 <li><strong>Imagens</strong> – Prints da interface de terminal estilizada com a biblioteca Rich</li> </ul>

<h2>🎯 Funcionalidades</h2>
<p>O módulo <code>task_manager</code> oferece as seguintes funções principais:</p>

<code>create_task(title, description="")</code> - Cria uma nova tarefa

<code>list_tasks()</code> – Lista todas as tarefas 

<code>list_pend_tasks()</code> – Lista todas as tarefas pendentes

<code>mark_complete(task_number)</code> – Marca uma tarefa como concluída

<code>remove_task(task_number)</code> – Remove uma tarefa da lista

<code>select_option(option)</code> – Lida com a escolha do usuário no menu

As tarefas são armazenadas em um dicionário Python com as seguintes informações:

`{
  "Título da Tarefa": {
    "Descrição": "Descrição opcional",
    "Feita": False
  }
}`

<h2>🖥️ Interface do Terminal</h2>
<p>A interface foi estilizada com a biblioteca <strong>Rich</strong>, permitindo uma exibição visualmente agradável no terminal com quadros, tabelas e ícones:</p>

<p align="left">
  <img src="img/menu.png" alt="Menu de opções" width="220" style="display:inline-block; margin-right: 10px; vertical-align: top;">
  <img src="img/tarefas.png" alt="Listagem de tarefas" width="510" style="display:block;">
</p>

<h2>💡 Tecnologias Utilizadas</h2>
<strong>Python</strong> (versão 3.10+)

<strong>Rich</strong> – Para estilização do terminal
📦 Instalação: <code>pip install rich</code>

