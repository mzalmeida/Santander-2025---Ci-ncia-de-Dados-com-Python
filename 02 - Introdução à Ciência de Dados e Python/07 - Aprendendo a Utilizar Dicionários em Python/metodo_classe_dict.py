# .Clear
# Limpa os valores do dicionario
contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "teste2@gmail.com": {"nome": "Joao", "telefone": "3333-2222"},
    "teste3@gmail.com": {"nome": "Maria", "telefone": "3333-2223"},
    "teste4@gmail.com": {"nome": "Alfredo", "telefone": "3333-2224"}
}

contatos.clear()
contatos # {}

# .Copy
# utilizado para quando voce quer manipular dados porém nao quer alterar o original
contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()  
copia["teste1@gmail.com"] = {"nome": "Gui"}

contatos["teste1@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-2221"}
copia["teste1@gmail.com"] # {"nome": "Gui"}


# .fromkeys
# adiciona chaves ao dicionario de uma vez só

dict.fromkeys(["nome","telefone"]) # {"Nome": none, "telefone": none}

dict.fromkeys(["nome","telefone"], "vazio") # {"Nome": "vazio", "telefone": "vazio"}

# .Get
# Segunda forma de acessar valor dentro de uma dicionario

contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
 }

contatos["chave"] # keyerror

contatos.get("chave") #none
contatos.get("chave", {}) #{}
contatos.get("teste1@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


#.items
# Retorna uma lista de tuplas, util quando é utilizado o comando for para retornar valores

contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
 }

contatos.items() #dict_items(['teste1@gmail.com', {'nome:'Guilherme','telefone]:'3333-2221'})])


# .keys
# Util para querer saber todas as chaves que seu dicionario possui

contatos = {"teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys() # dict_keys(['teste1@gmail.com])
print(resultado)

novo_dicionario={"a": 100, 1:"teste", "b":"python"}
print(novo_dicionario.keys())

# .pop
# Remove chaves do dicionario, independete de se a chave estar ou nao no dicionario

contatos = {"teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.pop("teste1@gmail.com") # {'nome': 'Guilherme','telefone':'3333-2221}
contatos.pop("teste1@gmail.com",{}) #{}

# popitem
# Nao informa qual chave quer remover, ele remove as chaves em sequencia

contatos = {"teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.popitem() # ('teste1@gmail.com',{'nome': 'Guilherme','telefone':'3333-2221}

# .setdefault
# se o atributo nao estiver no dicionario, ele adiciona com o valor que voce passou, 
# se o valor estiver no dicionario ele nao adiciona e retorna o valor

contatos = {"teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.setdefault("nome","Giovana") # 'Guilherme
contatos # {'nome'}: 'Guilherme', 'telefone': '3333-2221'}

contatos.setdefault("idade", 28) # 28
contatos # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

# .update
# Atualiza um dicionario com outro dicionario

contatos = {"teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"teste1@gmail.com":{"nome": "Gui"}})
contatos #{'teste1@gmail.com': {'nome': 'Gui'}}

contatos.update({"testeip@gmail.com":{"nome": "Giovana", "telefone":"3333-9002"}})
contatos # {'teste1@gmail.com': {'nome':'Gui'}, 'testeip@gmail.com': {'nome': 'Giovana', 'telefone': '3333-9002'}}


# .values
# Retorna os valores que estao amarrados com as chaves

contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "teste2@gmail.com": {"nome": "Joao", "telefone": "3333-2222"},
    "teste3@gmail.com": {"nome": "Maria", "telefone": "3333-2223"},
    "teste4@gmail.com": {"nome": "Alfredo", "telefone": "3333-2224"}
}

contatos.values() #dict_values([{'nome': 'Guilherme', 'telefone':'3333-2221' .....}])


# in
# Verificar se uma chave existe no dicionario
contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "teste2@gmail.com": {"nome": "Joao", "telefone": "3333-2222"},
    "teste3@gmail.com": {"nome": "Maria", "telefone": "3333-2223"},
    "teste4@gmail.com": {"nome": "Alfredo", "telefone": "3333-2224"}
}

"teste1@gmail.com" in contatos # True
"teste321@gmail.com" in contatos # False


# del
# Retira valores do dicionario
contatos = {
    "teste1@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "teste2@gmail.com": {"nome": "Joao", "telefone": "3333-2222"},
    "teste3@gmail.com": {"nome": "Maria", "telefone": "3333-2223"},
    "teste4@gmail.com": {"nome": "Alfredo", "telefone": "3333-2224"}
}

del contatos["teste1@gmail.com"]["telefone"]
del contatos ["teste2@gmail.com"]
print(contatos)
