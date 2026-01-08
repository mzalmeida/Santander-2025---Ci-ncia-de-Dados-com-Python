'''
Desafio
Uma produtora e exportadora de papéis para embalagens deseja organizar um sistema que calcule o total de toneladas exportadas por país de destino.

Cada exportação contém:

O país de destino
A quantidade de toneladas enviadas
O programa deverá receber as informações de várias exportações e, ao final, exibir um relatório com o total de toneladas para cada país.

Entrada
A entrada deve receber:

Um número inteiro N, representando a quantidade de exportações registradas.
Para cada exportação:
Uma string com o país de destino
Um número decimal com a quantidade de toneladas enviadas
Saída
O programa deverá exibir o total de toneladas exportadas para cada país no formato: pais: X toneladas

A ordem de exibição deve seguir a ordem em que os países apareceram pela primeira vez na entrada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
3
Argentina, 10
Chile, 8
Argentina, 5	Argentina: 15 toneladas
Chile: 8 toneladas
'''
# Leitura do numero de exportações
n = int(input())

# Inicializa o dicionario para armazenar toneladas por pais
exportacoes = {}

# Loop para ler os dados de cada exportacao
for _ in range(n):
    linha = input().strip()
    pais, toneladas = linha.split(",")
    pais = pais.strip()
    toneladas = float(toneladas.strip())
    
    # TODO: Acumule as toneladas de exportação de cada país no dicionário
    if pais in exportacoes:
      exportacoes[pais] = exportacoes[pais] + toneladas
    else:
      exportacoes[pais] = toneladas


# TODO: Imprima o total de toneladas por pais
for pais in exportacoes:
    print(f"{pais}: {int(exportacoes[pais])} toneladas")
