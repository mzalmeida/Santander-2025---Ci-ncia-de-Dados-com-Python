# Parametros especiais podem ser passados para uma funcao em python tanto por posicao quanto por nome.
#ex: por posicao, por posicao e nome ou por nome.

# Position Only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("pailio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina") # modelo valido

criar_carro(modelo="pailio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina") # modelo invalido


# Keyword only
# somente por nome

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="pailio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina") # modelo valido

# Keyword and positioal only
# por posicao e por nome

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("pailio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina") # modelo valido