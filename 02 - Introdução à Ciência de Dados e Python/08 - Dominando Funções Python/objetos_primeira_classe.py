# Objetos de primeira classe, funcoes sao objetos de primeira classe pois podemos atribuir funcoes a variaveis, passar um objeto como parametro para funcao e usar como valores em estruturas de dados(lista,tupla,dicionarios e etc)
# usar como valor de retorno para uma funcao(clousures)
 #Ex:

def somar (a, b):
    return a + b

def subtrair (a, b):
    return a - b

def test (a, b):
    return a * 2 + b * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao( a, b)
    print(f"o resultado de operacao é igual = {resultado}")

exibir_resultado(10, 10, somar) # o resultado da operacao 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # o resultado da operacao 10 + 10 = 0
exibir_resultado(10, 10, test) # o resultado da operacao 10 + 10 = 50

op = somar
print(op(1, 23)) # passa os valores ja no print para somar