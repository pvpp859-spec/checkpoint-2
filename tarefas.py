import json

lista_tarefas = []

def salvar_dados():
    with open("dados.json","w"):
        json.dump()

def carregar_dados():
    with open("dados.json","r"):
        try:
            json.load()
        except FileNotFoundError:
            print("arquivo não existe")
            print("criando novo arquivo")
            salvar_dados()

def adicionar_tarefas(descricao):
    tarefa = {"descrição": descricao,"concluida" : False}
    lista_tarefas.append(tarefa)

def listar_tarefas():
    for tarefa in lista_tarefas:
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{tarefa['descrição']} [{status}]")

def concluir_tarefa(indice):
    lista_tarefas[indice]["concluida"] = True