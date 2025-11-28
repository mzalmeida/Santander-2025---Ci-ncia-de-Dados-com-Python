# Metodo Append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

# Metodo Copy

lista = [1, "Python", [40, 30, 20]]
l2 = lista.copy()
print(lista) # [1, "Python", [40, 30, 20]]
print(id(l2), id(lista))
l2[0] =2
print(l2)
print(lista)

# Metodo Count
# Utilizado para contas quantas vezes um objeto aparece em uma determinada lista

cores = ["Vermelho","azul","verde","azul"]

cores.count("Vermelho") #1
cores.count("azul")     #2
cores.count("verde")    #1

# Metodo Extend
# Utilizado para adicionar elementos de uma lista em uma outra lista

linguagens = ["python", "js","c"]
print(linguagens) #["python", "js","c"]
linguagens.extend(["java","csharp"])
print(linguagens) #["python", "js","c","java","csharp"]

# Metodo Index
# Utilizado para encontrar a primeira ocorrencia de uma objeto

linguagens = ["python", "js","c","java","csharp"]
linguagens.index("java")   #3
linguagens.index("python") #0

# Metodo Pop
# Utilizado para remover o ultimo elemento de uma lista ou o elemento de uma posição

linguagens = ["python", "js","c","java","csharp"]
linguagens.pop()   #csharp
linguagens.pop()   #java
linguagens.pop()   #c
linguagens.pop(0)  #python

# Metodo Remove
# Utilizado para remover elementos de uma lista, passando o objeto que quer remover

linguagens = ["python", "js","c","java","csharp"]
linguagens.remove("c")   #csharp
print(linguagens) #["python", "js","java","csharp"]

# Metodo Reverse
# Utilizado para espelhar uma lista e colocar ela ao contrario

linguagens = ["python", "js","c","java","csharp"]
linguagens.reverse()
print(linguagens) #["csharp", "java","c","js","python"]

# Metodo Sort
# Utilizado para ordenar uma lista

linguagens = ["python", "js","c","java","csharp"]
linguagens.sort() #["c", "csharp","java","js","python"]

linguagens = ["python", "js","c","java","csharp"]
linguagens.sort(reverse=True) #["python", "js","java","csharp","c"]

linguagens = ["python", "js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x)) #["c", "js","java","python","csharp"]

linguagens = ["python", "js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #["python", "jcsharp","java","js","c"]

# Metodo Len
# Utilizado para verificar o tamanho da lista

linguagens = ["python", "js","c","java","csharp"]
len(linguens) #5

# Metodo sorted
# Utilizado para verificar o tamanho da lista

linguagens = ["python", "js","c","java","csharp"]
sorted(linguagens, key=lambda x: len(x)) #["c", "js","java","python"]
linguagens.sort(key=lambda x: len(x), reverse=True) #["python", "csharp","java"]
