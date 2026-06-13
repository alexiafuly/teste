# Importar as bibliotecas 

import os
import json # replica dados
from datetime import datetime # importar somente uma classe do módulo datetime


def criar_gitkeep(caminho):
    gitkeep = os.path.join(caminho,".gitkeep")
    if not os.path.exists(gitkeep):
        with open(gitkeep, "w"):
            pass
        return gitkeep
    return None


def remover_gitkeep(caminho):
    gitkeep = os.path.join(caminho,".gitkeep")
    if os.path.exists(gitkeep):
        os.remove(gitkeep)
        return gitkeep
    return None


def salvarlog(criados, removidos):
    os.makedirs("log", exist_ok = True)
    log_file = os.path.join("logs", "log.json")
    registro = {"data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "gitkeeps_criados": criados, "gitkeeps_removidos": removidos}
    logs = []
    if os.path.exists(log_file):
        try:
             with open(log_file, "r", encoding = "utf-8") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append(registro)
    with open(log_file, "w", encoding = "utf-8") as f:
        json.dump(logs, f, indent = 4, ensure_ascii = False)


def processamento_repositorio():
    criados = []
    removidos = []
    for raiz, diretorios, arquivos in os.walk("."):
        if "logs" in diretorios:
            diretorios.remove("logs")

        arquivos_reais = [arquivo for arquivo in arquivos if arquivo != ".gitkeep"]

        pasta_vazia = (len(arquivos_reais) == 0 and len(diretorios) == 0)
        if pasta_vazia:
            criado = criar_gitkeep(raiz)
            if criado:
                criados.append(criado)
        else:
            removido = remover_gitkeep(raiz)
            if removido:
                removidos.append(removido)

    salvarlog(criados, removidos)

    print("\nExecutado com sucesso!")

    print("\nGitkeeps criados:")
    for item in criados:
        print(item)

    print("\nGitkeeps removidos:")
    for item in removidos:
        print(item)


if __name__ == "__main__":
    processamento_repositorio()

