import json

lista_tarefas = []

def salvar_dados():
    with open("dados.json","w") as arquivo:
        json.dump(lista_tarefas,arquivo,indent=4)

def carregar_dados():
    global lista_tarefas
    try:
        with open("dados.json", "r") as arquivo:
            lista_tarefas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("arquivo não existe ou está vazio")
        lista_tarefas = []
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