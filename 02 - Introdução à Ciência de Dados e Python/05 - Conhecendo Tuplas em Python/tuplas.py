#Tuplas são estruturas de dados muito parecidas com as listas, 
# a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. 
# Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses.

frutas = ("laranja","pera","uva")
letras = tuple("python")
numeros = tuple([1, 2, 3, 4,])
pais = ("Brasil",)

# Tupla

frutas = ("maca", "laranja", "uva", "pera")
frutas[0] #maça
frutas[2] #uva

# Tupla Indice Negativo
# Sequencias suportam indexação negativa. A contagem começa em -1

frutas = ("maca", "laranja", "uva", "pera")
frutas[-1] #pera
frutas[-3] #laranja

# Tuplas aninhadas
#Tuplas podem armazenar todos os tipos de objetos Python, 
# portanto podemos ter tuplas que armazenam outras tuplas. 
# Com isso podemos criar estruturas bidimensionais (tabelas), 
# e acessar informando os índices de linha e coluna. 

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2 
matriz[-1][-1] # "c"

# Matriz que é imutavél é interessante usar tupla em vez de lista

# Fatiamento
#Além de acessar elementos diretamente, podemos extrair um conjunto de valores 
# de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar 
# o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

tupla = ("p","y","t","h","o","n",)

tupla[2:] #("t", "h", "o", "n")
tupla[:2] #("p", "y")
tupla[1:3] #("y", "t")
tupla[0:3:2] #("p", "t")
tupla[::] # ("p", "y", "t", "h", "o", "n")
tupla[::-1] # ("n", "o", "h", "t", "t", "y", "p")

# Iterar Tupla
#A forma mais comum para percorrer os dados de uma tupla é utilizando o comando for.

carros = ("gol", "celta", "palio")

for carro in carros:
    print (carro)

# Funcao Enumerate
carros = ("gol", "celta", "palio")

for indice, carro in enumerate(Carros):
    print(f"[indice]: {carros}")


# Métodos da classes Tuple

# Metodo Count
carros = ("gol", "celta", "palio","palio")
carros.count("palio")  # 2
carros.count("celta")  # 1
carros.count("gol")    # 1

# Metodo Index
# Saber em qual posicao o objeto esta na tupla
carros = ("gol", "celta", "palio")

carros.index("palio") # 3
carros.index("gol")   # 1

# Metodo Len
# Ver o tamanho total dos elementos na tupla

carros = ("gol", "celta", "palio")
len(carros) # 3

# Tupla não é permitido atualização




  




