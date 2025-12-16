# funcao é um bloco de codigo identificado por um nome e pode receber uma lista de parametros.
# Melhora o código no quesito legivel e possibilita reaproveitamento de código

# Ex:

def exibir_mensagem():
    print ("ola mundo!")

def exibir_mensagem_2(nome):
    print (f"Seja bem vindo {nome}") 

def exibir_mensagem_3(nome="Anonimo"):
    print (f"ola mundo!{nome}")  

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")  
exibir_mensagem_3(nome="Anonimo") 
# Comentar cada exibir_mensagem para executar e printar a variavel

# Retornando valores
# Python pode retornar mais de um valor utilizando a palavra reservada return., toda funcao em python por padrao retorna None

# EX - Funcao de Lista de Numeros e Retorno de sucessor e antecessor de um numero informado.

# 1 - Funcao de Lista de Numeros
def calcular_total(numeros):
    return sum(numeros)

# 2 - Retorno de sucessor e antecessor de um numero informado.

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor   = numero + 1

    return antecessor,sucessor

calcular_total([10, 20 ,34]) 
print(calcular_total) #64

retorna_antecessor_e_sucessor(10) # (9, 11)



# Ex3
def func_3():
    print("ola mundo")
    #return none


    




