# Dicionarios são conjuntos não ordenado de pares chave:valor.
#chaves são unicas e delimitadas por {} separados por virgula

pessoa = {"nome": "Guilherme", "Idade": 28}

pessoa = dict (nome= "Guilherme", Idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Acessar os Dados

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # "Guilherme"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

# Acessando os dados porém substituindo o valor do dicionario

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados # {"nome": "Maria", "Idade": 18, "telefone": "9988-1781"}

# Dicionarios Aninhados
# É quando temos uma estrutura dentro de outra

#Ex:

contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "teste2@gmail.com": {"nome": "Joao", "telefone": "3333-2222"},
    "teste3@gmail.com": {"nome": "Maria", "telefone": "3333-2223"},
    "teste4@gmail.com": {"nome": "Alfredo", "telefone": "3333-2224", "extra": {"a":1}}
}

contatos["teste1@gmail.com"]["telefone"] #"3443-2121"
print(telefone)

extra = contatos["teste4@gmail.com"]["extra"]["a"]
print(extra)


# Iterar Dicionarios

for chave in contatos:
    print(chave, contatos[chave])


for chave, valor in contatos.items():
    print(chave, valor)




