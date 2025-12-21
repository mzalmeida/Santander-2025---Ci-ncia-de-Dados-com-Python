'''
Desafio
Uma produtora e exportadora de papéis para embalagens precisa calcular 
o valor final de suas exportações. 
Cada remessa possui um peso em toneladas e um preço por tonelada em dólares. 
Além disso, dependendo do tipo de cliente, a empresa oferece descontos:

Novo cliente: sem desconto
Cliente fidelizado: 5% de desconto
Cliente premium: 10% de desconto
O programa deve calcular o valor total da remessa considerando o peso, 
o preço por tonelada e o desconto aplicável, retornando o valor final a ser pago 
pelo cliente.

Entrada
A entrada deve receber:

Um número decimal representando o peso da carga em toneladas.
Um número decimal representando o preço por tonelada em dólares.
Uma string representando o tipo de cliente ("Novo cliente", "Cliente fidelizado", 
"Cliente premium").
Saída
O programa deverá retornar o valor final da exportação (em dólares), 
já com o desconto aplicado, formatado com duas casas decimais.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e 
suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses 
exemplos e com outros casos possíveis.

Entrada	Saída
10
500
Novo cliente	5000.00
8
600
Cliente fidelizado	
4560.00

12
400
Cliente premium	4320.00
Atenção: É extremamente importante que as entradas e saídas sejam exatamente
iguais às descritas na descrição do desafio de código.

'''
# Leitura dos dados de entrada
print("Programa para calcular peso de exportacoes\n\n")
print("Digite o peso do produto:")
peso = float(input())
print("O peso digitado é:\n",peso)
print("digite o preço da tonelada:")
preco_por_tonelada = float(input())
print("O preço da tonelada é:\n", preco_por_tonelada)
print("Digite o tipo de cliente que são:\n 1 - Novo_Cliente\n 2 - Cliente_Fidelizado \n 3 - Cliente_Premium\n")
tipo_cliente = input()
print("O tipo de cliente escolhido é:\n", tipo_cliente)

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada      # Para se calcular o valor total é multiplicado a variael peso pela variavel preco_por_tonelada


# TODO Aplique o desconto conforme o tipo de cliente
'''
desconto depende de tipo_cliente ou seja precisamos fazer uma comparação, para comparar e decidir é utilizado
if / elfif / else
No caso desconto precisará ser uma variavél onde iremos atribuir os valores de desconto para cada tipo de cliente.
OBS: Sempre que algo muda dependendo de uma condição,você precisa de:uma variável,uma decisão (if)
= → atribuição
== → comparação

0 representa 0% de desconto.
antes de analisar o tipo de cliente,o sistema assume nenhum desconto
Sempre inicialize variáveis de decisão com um valor válido e neutro.
'''

desconto = 0                    
if tipo_cliente == '1':
 desconto = 0

elif tipo_cliente == '2':
 desconto = 0.05
else:
 desconto = 0.10

valor_final = valor_total * (1 - desconto)

# Exibe o resultado formatado com duas casas decimais
print(f"O valor final é:{valor_final:.2f}")
