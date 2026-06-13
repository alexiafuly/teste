# Trilha de Python - Semana 4: Automação de Versionamento de Diretórios Vazios

## Funcionamento do programa
O programa automatiza a organização de um repositório no git, garantindo que todos os diretórios contenham pelo menos um arquivo para que possam sem comitados. Utilizando as bibliotecas datetime, json e os, o código percorre todos os diretórios e verifica os arquivos presentes nesles. Caso a pasta esteja vazia, o programa gera um arquivo .gitkeep; caso a pasta tenha somente um arquivo .gitkeep, o programa não adiciona nada; caso a pasta tenha um arquivo .gitkeep e mais algum outro arquivo, o programa remove o .gitkeep. Além disso, também são utilizados logs para marcar a data e o horário das alterações.

## Instruções de Uso
O usuário deve criar seus diretórios e adicionar quantos arquivos quiser. Depois, ele deve executar o programa para percorrer o repositório e garantir que todas as pastas tenham ao menos um arquivo e que não haja nenhum arquivo desnecessário. Por fim, basta salvar as mudanças utilizando git add . e git commit e então empurrar para o repositório com git push.

## Respostas às perguntas teóricas

Explique as diferenças entre:

a) json.dump() vs json.dumps()

R: json.dump() manda as informações para um arquivo, enquanto json.dumps() manda as informações para uma string.

b) json.load() vs json.loads()

R: json.load() é uilizado para pegar as informações de um arquivo, enquanto json.loads() pega as informações de uma string.