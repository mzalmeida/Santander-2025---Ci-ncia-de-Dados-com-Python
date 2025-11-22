# Manipulando objetos do tipo string em python

#oldStyle

nome      =     "Guilherme" 
idade     =      28
profissao =     "Programador"
linguagem =     "Python"

print ("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#Metodo Format

nome      =     "Guilherme" 
idade     =      28
profissao =     "Programador"
linguagem =     "Python"

print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
print ("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}." .format(nome, idade, profissao, linguagem))
print ("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print ("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))

#F-string
nome      =     "Guilherme" 
idade     =      28
profissao =     "Programador"
linguagem =     "Python"

print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

# Formatar string com F-string

PI = 3.14159
print(f"Valor de PI: {PI:.2f}") ## 2 casas decimais
print(f"Valor de PI: {PI:10.2f}") ## 10 espaços


# Exemplo aula com metodo Format, F-string

nome        = "Mateus"
idade       = 30
profissao   = "Programador"
linguagem   = "Pyhon"
saldo       = 8.980

dados = {"nome":"Mateus","idade":30,"profissao":"Programador","linguagem":"Python","saldo":8.980}

print ("Nome: %s\nidade:%d \nprofissao: %s\nlinguagem: %s\nsaldo: %.2f" % (nome, idade, profissao, linguagem, saldo))
#print("Nome: %s\nIdade: %d\nProfissão: %s\nLinguagem: %s\nSaldo: %.2f" % (nome, idade, profissao, linguagem, saldo))

print("Nome:{} idade:{} profissao:{} linguagem:{} saldo{}"      .format(nome, idade, profissao, linguagem, saldo))
print("Nome:{0} idade:{1} profissao:{2} linguagem:{3} saldo{4}" .format(nome, idade, profissao, linguagem, saldo))
print("Nome:{1} idade:{0} profissao:{2} linguagem:{3} saldo{4}" .format(nome, idade, profissao, linguagem, saldo))
print("Nome:{1} idade:{0} profissao:{2} linguagem:{3} saldo{4}" .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem, saldo=saldo))
print("Nome:{nome} idade:{idade} profissao:{profissao} linguagem:{linguagem} saldo{saldo}" .format(++dados))
print(f"Nome: {nome} Idade: {idade} Profissao: {profissao} Linguagem:{linguagem} Saldo:{saldo:.2f}")  
print(f"Nome: {nome} Idade: {idade} Profissao: {profissao} Linguagem:{linguagem} Saldo:{saldo:10.2f}")       