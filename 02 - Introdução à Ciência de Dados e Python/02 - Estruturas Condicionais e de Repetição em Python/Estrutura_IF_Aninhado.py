#Exemplo de programa com IF aninhado que são IF dentro de um IF já existente.
conta_normal        = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

"""
conta_ = input("Informe a conta [1] Normal \n [2] Universitaria: ")

if conta ==1:
    print("Conta Normal")
else:
    print("Conta Universitaria")  
"""

if conta_normal:
    if saldo >= saque:
        print("Saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        ("Nao permitido saque")    
elif conta_universitaria:
    if saldo>=saque:
        print("Saque realizado")        
    else:
        print("Saldo insuficiente")
