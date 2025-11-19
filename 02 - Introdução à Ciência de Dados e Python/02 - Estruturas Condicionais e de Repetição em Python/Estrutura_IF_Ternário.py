# A estrutura IF ternário, permite que a condição seja escrita em uma unica linha. 
# primeira parte é o retorno, segunda parte é a logica e a terceira é o retorno caso a expressão não seja atendida.

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")