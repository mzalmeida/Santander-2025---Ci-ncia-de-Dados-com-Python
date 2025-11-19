# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
# Exemplo IF:

saldo = 2000.0
saque = float(input("informe o valor do saque"))

if saldo >= saque:
    print("Realizado saque")

if saldo < saque:
    print("Saque não realizado")
    

# Exemplo If com Else:

saldo = 2000.0
saque = float(input("informe o valor do saque"))

if saldo >= saque:
    print("Realizado saque")

else:
    print("Saque insuficiente")


# Exemplo Elif
import sys

opcao = int(input("informe uma opcao: [1] sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
                        
elif opcao == 2:
    print("Exibindo o extrato")

else:
    sys.exit("Opcao Invalida")    
         


# Programa teste de Idade
MAIOR_IDADE = 18

idade = int(input("Informe a idade"))

if idade >= MAIOR_IDADE:
    print("Maior de Idade, pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")

if idade >=MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")    
else:
    print("Ainda não pode tirar CNH")          



# Programa teste de Idade com elif
MAIOR_IDADE    = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a idade"))

if idade >= MAIOR_IDADE:
    print("Maior de Idade, pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")

if idade >=MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH") 

elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas téoricas, mas não as aulas práticas.")       
else:
    print("Ainda não pode tirar CNH")          


        