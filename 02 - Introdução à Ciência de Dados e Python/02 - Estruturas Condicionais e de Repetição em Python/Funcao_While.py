# Comando while é usado para repetir um bloco de código varias vezes.Utilizado para quando não sabemos o numero exato de repetição que queremos.

# Exemplo de While
opcao = -1

while opcao !=0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n"))

    if opcao ==1:
        print("Sacando")

    elif opcao ==2:
        print("Exibindo Extrato")

# Exemplo de while com Else
opcao = -1

while opcao !=0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n"))

    if opcao ==1:
        print("Sacando")

    elif opcao ==2:
        print("Exibindo Extrato")
else:
    print("Obrigado")    

# Exemplo while com break
while True:# 1 == 1

    numero = int(input("Informe o numero:"))
                 
     if numero == 10:
         break
     print(numero)  
    

# Exemplo de for com break
for numero in range(100):
                    
     if numero == 99:
         break
     print(numero, end=" ")
    

# Exemplo variacao Continue
for numero in range(100):
                    
     if numero == 12:
         continue
     print(numero, end=" ")


     #Break para o laço e o Continue irá pular
    

