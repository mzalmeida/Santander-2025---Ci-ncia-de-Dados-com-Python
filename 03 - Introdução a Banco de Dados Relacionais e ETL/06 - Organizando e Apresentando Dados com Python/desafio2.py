'''
Desafio
Uma empresa produtora e exportadora de papéis para embalagens precisa gerar um relatório de pedidos por tipo de embalagem. Cada pedido contém:

O nome do cliente
O tipo de embalagem ("saco", "papelao ondulado" ou "papel kraft")
A quantidade de toneladas solicitadas
O sistema deve retornar o resultado o total solicitado para cada tipo de embalagem existente na lista.

Entrada
A entrada deve receber:

Um número inteiro N, representando o número de pedidos.
Para cada pedido:
Uma string com o nome do cliente
Uma string com o tipo de embalagem ("saco", "papelao ondulado", "papel kraft")
Um número decimal com a quantidade de toneladas
Saída
O programa deverá retornar a quantidade total de toneladas por cada tipo de embalagem, no formato:

saco: X
papelao ondulado: Y
papel kraft: Z

'''

# Lê o número de pedidos
N = int(input())

# Dicionário para armazenar totais por tipo de embalagem
totais = {}

# Processa cada pedido
for _ in range(N):
    linha = input()
    cliente, embalagem, quantidade = linha.split(", ")
    quantidade = float(quantidade)
    
    # TODO: Some a quantidade ao tipo de embalagem correspondente
    if embalagem in totais:
      totais[embalagem] = totais[embalagem] + quantidade
    else:
      totais[embalagem] = quantidade



# Imprime o resultado no formato solicitado, mantendo a ordem "saco", "papelao ondulado", "papel kraft"
for tipo in ["saco", "papelao ondulado", "papel kraft"]:
    print(f"{tipo}: {int(totais[tipo]) if tipo in totais and totais[tipo].is_integer() else totais.get(tipo, 0)}")