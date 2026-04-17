import json
import os
import time

timpo = 0.5
time.sleep(timpo)
os.system("cls")

from tarefas import adicionar_tarefas,lista_tarefas,listar_tarefas,concluir_tarefa

while True:
    time.sleep(timpo)
    os.system("cls")
    print("LISTA DE TAREFAS")
    print("  ADICIONAR 1")
    print("   LISTAR 2")
    print("CONCLUIR TAREFA 3") 
    print("    SAIR 4")
    escolha = int(input("qual sua escolha: "))

    if escolha == 1:
        time.sleep(timpo)
        os.system("cls")
        nova_tarefa = str(input("qual tarefa voce quer adicionar: "))
        adicionar_tarefas(nova_tarefa)
        print("tarefa adicionada!!")
    elif escolha == 2:
        time.sleep(timpo)
        os.system("cls")
        listar_tarefas()
    elif escolha == 3:
        time.sleep(timpo)
        os.system("cls") 
        listar_tarefas()
        indice = int(input("qual tarefa voce quer concluir: ")) - 1
        concluir_tarefa(indice)
    elif escolha == 4:
        print("saindo")
        break        


