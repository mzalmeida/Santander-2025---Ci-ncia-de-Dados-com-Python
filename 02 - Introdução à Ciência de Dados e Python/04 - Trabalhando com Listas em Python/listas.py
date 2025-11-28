# Listas em python é utilizado para armazenar de forma sequencial qualquer tipo de objeto.
# Para criaçãos de listas é possivél criar com list, com a função range ou colocando valores separados por virgula dentro de colchetes.

# Exemplo

frutas = ["laranja","uva","limao"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["ferrari","F8",4200000, 2020, 2900, "São Paulo", True]

frutas = ["maça", "laranja", "uva", "pera"]
frutas[0]
frutas[2]

# Indice negativo
frutas = ["maça", "laranja", "uva", "pera"]
frutas[-1]
frutas[-3]

# Listas Aninhadas
# Listas podem armazenar todos os tipos de objetos python, portando podemos ter listas que armazenam outras listas.
# Com isso podemos criar estrutuas bidimensionais(tabelas). e acessar informando os índices de linha e coluna.

matriz = [
     [1,"a",2],
     ["b",3,4],
     [6,5,"c"],
]

matriz[0]
matriz[0][0]
matriz[0][-1]
matriz[-1][-1]

# Fatiamento
# É uma forma que passa  o valor inicial ou final para acessar um conjunto de elementos.

lista = ["p","y","t","h","o","n"]

lista[2:] # ["t","h,","o","n"]
lista[:2] # ["p","y"]
lista[1:3] # ["y","t"]
lista[0:3:2] # ["p","t"]
lista[::] # ["p","y","t","h","o","n"]
lista[::-1] # ["n","o","h","t","y","p"]


# Iterar listas

carro = ["gol","celta","palio"]
for carro in carros:
    print(carro)

# Função Inumerate
carro = ["gol","celta","palio"]   
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensao de listas
# A compreensao de lista oferece uma sintaxe mais curta quando voce deseja > criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

# Filtro versão 1 = pegar todos os numeros pares
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)

# Filtro versão 2 = pegar todos os numeros pares
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 ==0:]

# Modificando valores versão 1 = pegar todos os numeros pares
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Modificando valores versão 2 = pegar todos os numeros pares
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [ numero ** 2 for numero in numeros]




      
