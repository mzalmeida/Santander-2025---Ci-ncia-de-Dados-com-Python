'''
Desafio
Você foi contratado para desenvolver um sistema que determine a quantidade de paletes 
necessária para armazenar a produção diária de caixas. Cada palete possui uma capacidade 
fixa de caixas, e o objetivo é calcular o número total de paletes requeridos para acomodar 
toda a produção do dia.

Entrada
A entrada deve receber:

O número total de caixas produzidas.
A capacidade de caixas que um palete pode suportar.
Saída
Deverá retornar uma string que representa o número total de paletes necessários, 
sem espaços ou caracteres especiais.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
 Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
100
10	10
45
5	
9

150
20	8
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas 
na descrição do desafio de código.
'''
import math

# Leitura das entradas como strings
total_caixas = input().strip()
capacidade_palete = input().strip()

# Conversão para inteiros
total_caixas = int(total_caixas)
capacidade_palete = int(capacidade_palete)

# TODO: Calcule o número de paletes necessários (arredondando para cima)
# Para arredondamento de calculo, é utilizado a funcao math.ceil
paletes_necessarios = math.ceil(total_caixas / capacidade_palete) 

# Impressão como string (sem espaços ou caracteres especiais)
print(str(paletes_necessarios))