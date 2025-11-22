# Manipulando objetos do tipo string

curso = "  Python "

print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())

print(curso.center(10, "#"))

print(*.*.join(curso))


#Trabalhando com Maiuscula e minuscula


nome = "MaTEus"

print(nome.upper())
print(nome.lower())
print(nome.title())


# Trabalhando com tratamento de espaços em branco na variavél.

texto = "  Olá mundo!  "

print(texto + ".")          #Exibe variavél
print(texto.strip() + ".")  #Exibe variavél sem espaços
print(texto.rstrip + ".")   #Exibe variavél somente com os espaços a direita
print(texto.lstrip + ".")   #Exibe variavél somente com os espaços a esquerda

# Trabalhando com tratamento de junções e Centralização

menu = "Python"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(14,  "#"))
print("-".join(menu))