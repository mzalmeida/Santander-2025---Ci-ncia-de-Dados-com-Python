#  Sets é para eliminar objetos duplicados em uma lista
# Conjuntos em python não suportam indexação ou seja voce não consegue acessar o valor de um determinado indice

#Exemplo de Set

set([1,2,3,1,2,3]) # {1,2,3,4}

set("abacaxi") # {"b","a","c","x","i"}

set(("palio","gol","celta","palio")) # {"gol", "celta", "palio"}

# Acessando objetos de um set, tem que converter em lista

numeros = {1,2,3,4}

numeros = list(numeros)

print(numeros[0])

# Iterar set através do FOR

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# Funcao enumerate : saber o indice que esta percorrendo    

carros = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Metodo da classe SET

# Union

conjunto_a = {1,2}    
conjunto_b = {3,4}  
conjunto_a.union(conjunto_b) # {1,2,3,4}

# Intersection
# intersecção é para mostrar os conjuntos que são iguais

conjunto_a = {1,2,3}    
conjunto_b = {2,3,4}  
conjunto_a.intersection(conjunto_b) # {2,3}

# Difference
# Difference é tudo que existe em um conjunto que nao esteja no outro
conjunto_a = {1,2,3}    
conjunto_b = {2,3,4}  
conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# Symmetric_difference
# Symetric é apresentar todos os elementos que não estão na intersecção
conjunto_a = {1,2,3}    
conjunto_b = {2,3,4}  
conjunto_a.symmetric_difference(conjunto_b) # {1,4}

# Issubset
# Apresentar quais elementos em forma de verdadeiro ou falso pertence a cada conjunto
# ex: elementos do conjunto A pertence ao B = Verdadeiro, já o B não pertence ao A

conjunto_a = {1,2,3}    
conjunto_b = {4,1,2,5,6,3}  

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# Issuperset
# É o contrario do Issubet, ou seja todos os elementos de B estão em A = False, já os de A estão em B

conjunto_a = {1,2,3}    
conjunto_b = {4,1,2,5,6,3}  

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# Isdisjoin
# É quando eu quero fazer a operação em conjunto dejunto, ou não tem intersecção, os elementos não estão em no outro grupo

conjunto_a = {1,2,3,4,5}    
conjunto_b = {6,7,8,9} 
conjunto_c = {1,0} 

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False


# Add
# Passa um elemento e se não existir ele é adicionado

sorteio = {1, 23}

sorteio.add(25) #{1,23,25}
sorteio.add(42) #{1,23,25,42}
sorteio.add(25) #{1, 23 ,25, 42}

# Clear
# limpa a lista
sorteio = {1, 23}

sorteio  #{1,23}
sorteio.clear() # 
sorteio # {}

# Copy
#Copia os dados

sorteio = {1, 23}

sorteio  #{1,23}
sorteio.copy() # 
sorteio # {1,23}

# discard
# Discartar um valor
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros # {1,2,3,4,5,6,7,8,9,0}
numeros.discard(1)
numeros.discard(45) 
numeros # {2,3,4,5,6,7,8,9,0}

# Pop
# Retira os valores de uma lista
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros # {1,2,3,4,5,6,7,8,9,0}
numeros.pop() #0
numeros.pop() #1
numeros # {2,3,4,5,6,7,8,9}

# Remove
# Remove um valor de uma lista
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros # {0,1,2,3,4,5,6,7,8,9}
numeros.remove(0) #0
numeros # {1,2,3,4,5,6,7,8,9}

# Len
# Faz a leitura do tamanho da lista
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
len(numeros) # 10

# In
# verifica se um objeto está em uma lista
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
1 in numeros # True
10 in numeros # False













