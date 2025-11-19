# Estrutura de repeticao são utilizadas para repetir um trecho do código em um determinado numero de vezes.

#Exemplo sem repetição

a = int(input("informe um numero inteiro"))
print(a)

a +=1
print(a)

#Exemplo com repetição (FOR)
# For é utilizado para quando sabemos o tanto de vezes que o programa deve-se repetir.


texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()


#Exemplo com repetição (FOR) com (ELSE)
# For é utilizado para quando sabemos o tanto de vezes que o programa deve-se repetir.


texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Execua no final do laço")        






