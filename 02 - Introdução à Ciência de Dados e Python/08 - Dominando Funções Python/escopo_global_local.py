# python trabalha com escopo local e global, dentro do bloco da funcao é escopo local
# global informa ao interpretador que a variavel que esta sendo manipulada no escopo local é global. 
# isso nao é uma boa pratica e deve ser evistado


# Ex:
salario = 2000

def salario_bonus(bonus):
    global salario
    salario +=bonus
    return salario

salario_bonus(500)
print(salario)