# Funcao com argumentos nomeados, são funcoes onde voce passa chave e valor

#Ex1:
# ** é dicionario

def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso" {marca}/{modelo}/{ano}/{placa})

salvar_carro("fiat", "palio", 1999, "ABC-1234")
#salvar_carro(marca="Fiat", modelo="palio", ano=1999, placa="ABC-1234")
#salvar_carro(**{"marca": "fiat", "modelo": "palio", "ano": 1999, "placa": "abc-1234"})     