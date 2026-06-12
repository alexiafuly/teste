# Importar as bibliotecas 

import os
import json # replica dados
from datetime import datetime # importar somente uma classe do módulo datetime

# os.walk percorre os diretórios
def criar_gitkeep(caminho):
    gitkeep = os.path.join(caminho,".gitkeep")
    if not os.path.join(gitkeep):
        open(gitkeep, "w").close()
        return gitkeep
    return None

def remover_gitkeep(caminho):
    gitkeep = os.path.join(caminho,".gitkeep")
    





# definir uma função 

def salvarlog(criado, removido):
    os.makedirs("log", exist_ok = True)
    log_file = "log/log.json"
    registro = {"data_hora": datetime.now().strftime(
        "%y-%m-%d %H:%M:%S"),
        "criados": criados,
        "removidos": removidos
        }
    if os.path.exists(log_file):
        with open(log_file, "r", encoding = "utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []
    logs.append(registro)
    with open(log_file, "w", encoding = "utf-8") as f:
        json.dump(logs, f, indent = 4, ensure_ascii = False)




# referenciar as pastas como listas, em que os arquivos são os itens


# se for log, não verificar (.remove)


# os.remove(/workspaces/teste/logs)


# print(len()) para saber quantos arquivos tem 
print(f"Arquivos em {logs}: {len(logs)}")

# os.path.join para adicionar arquivo gitkeep caso a pasta esteja vazia


# caso a pasta tenha mais de um arquvio, os.exists para ver se existe o arquivo .gitkeep; se existir, os.remove
def processar_repositorio():
    criados = []
    removidos = []
    for raiz, diretorios, arquivos in os.walk("."):
        if "logs" in diretorios:
            diretorios.remove("logs")

        arquivos_reais = [for arquivo in arquivos if arquivo != ".gitkeep"]