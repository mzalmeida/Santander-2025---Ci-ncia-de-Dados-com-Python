# Identacao no código é para deixar o código mais legivél e facilitar a manutenção do código.
# No python a identação é utilizada para informar ao interpretador onde inicia e onde é o fim de um bloco de comando.

def sacar(valor: float):
    saldo = 500
    if saldo >= valor:
        print ("valor sacado!")
        print ("retire o dinheiro do caixa!")

    print("obrigado por ser nosso cliente")

def depositar(valor):
    saldo=500
    saldo += valor



sacar(400)