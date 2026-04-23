import json
import os
import time

timpo = 0.5
time.sleep(timpo)
os.system("cls")


from tarefas import adicionar_tarefas,lista_tarefas,listar_tarefas,concluir_tarefa,carregar_dados,salvar_dados,remover_tarefa

carregar_dados()

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
        salvar_dados()
        while True:

            escolha = input("quer adicionar mais alguma tarefa? :").lower()

            if escolha in ("sim", "s"):
                nova_tarefa = str(input("qual tarefa voce quer adicionar: "))
                adicionar_tarefas(nova_tarefa)
                print("tarefa adicionada!!")
                salvar_dados()
            elif escolha in ("não", "nao","n"):
                break
            else:
                print("ERRO")    

    elif escolha == 2:
        time.sleep(timpo)
        os.system("cls")
        listar_tarefas()
        numero = int(input("quer remover algo da lista digite 0: "))
        if numero == 0:
            indice = int(input("qual tarefa voce quer excluir: ")) - 1
            try:
                remover_tarefa(indice)
                salvar_dados()
                time.sleep(timpo)
                os.system("cls")
                listar_tarefas()
            except:
                print("ERRO")
                time.sleep(timpo)
                os.system("cls")   
            while True:
                os.system("cls")  
                listar_tarefas()
                escolha = str(input("quer remover mais alguma coisa?:"))
                if escolha == "sim" or escolha == "s" :
                    indice = int(input("qual tarefa voce quer excluir: ")) - 1
                    remover_tarefa(indice)
                    salvar_dados()
                    time.sleep(timpo)
                    os.system("cls")
                elif escolha == "não" or escolha == "nao" or escolha == "n":
                    break    
                else:
                    print("ERRO")
        else:    
            os.system("cls")
    elif escolha == 3:
        time.sleep(timpo)
        os.system("cls") 
        listar_tarefas()
        indice = int(input("qual tarefa voce quer concluir: ")) - 1
        concluir_tarefa(indice)
        salvar_dados()
        while True:
            listar_tarefas()
            escolha == str(input("quer concluir mais alguma tarefa? :"))
            if escolha == "sim" or escolha == "s":
                indice = int(input("qual tarefa voce quer concluir: ")) - 1
                concluir_tarefa(indice)
                salvar_dados()
                os.system("cls")
            elif escolha == "não" or escolha == "nao" or escolha == "n":
                break
            else:
                print("ERRO")     
    elif escolha == 4:
        print("saindo")
        break        


