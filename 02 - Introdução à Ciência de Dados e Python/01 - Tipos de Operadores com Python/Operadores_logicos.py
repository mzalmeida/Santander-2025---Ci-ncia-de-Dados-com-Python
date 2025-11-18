#Operadores logicos são operadores que são utilizados em conjuntos com os operadores de comparacao para montar uma expressao logica.

# AND = para ser True tudo tem que ser TRUE
# OR  = para ser True apenas um tem que ser True

print(True  and True )
print(True  and False)
print(False and False)
print(True  or  True )
print(True  or  False)
print(False or  False)

#Variavéis
saldo = 1000
saque = 250
limite = 2000
conta_especial = True




#logica
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and  saldo >=saque
exp_3 = conta_normal_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

