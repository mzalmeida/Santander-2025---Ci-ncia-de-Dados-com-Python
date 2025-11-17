################# Tipos_de_Dados #################

print (1 + 10)    #inteiro
print (1 + 1.5)   #float
print (True)      #Boleano 
print (False)     #Boleano
print ('Python')  #String

################# Representação_dos_Dados #################
int()
float()
str()
bool()

################# Modo_Interativo #################
"""
Para iniciar é preciso no terminar chamar o interpretador digitando python
ou executando o script flag -i (python -i app.py)
"""

################# Funcoes_DIR_e_HELP #################
"""
DIR

dir()    - escopo local sem argumentos
dir(100) - retorna lista de atributos válidos para o objeto

HELP
Sistema de ajuda integrado para consulta de documentação 
help()
help(100)
"""

################# Variáveis_e_Constantes #################
"""
Variavél
Variavéis são para definir valores e esses valores podem sofrer alterações na execução do progama.
Para uma variavél em python não precisamos definir o tipo de dado, ele define automaticamente, por isso
precisamos criar uma variavél e atribuir um valor a ela.

Constantes
Já uma constante é igual uma variavél, utilizadas para armazenar valores, porém estes valores,
não sofrem alteração durante e execução de um programa.
Em python não existe constantes, para que o programador saiba que aquela variavél não deve sofrer
alterações no valor, é preciso que o nome da variavél seja criado com lestras maiusculas.
Ex: NOME_1
"""
# Exemplo_Variavél
nome = 'Gulherme'
idade = 28

nome, idade = "Giovana",27


print(nome, idade)

limite_saque_diario = 1000

print (nome , idade)
print ('Saque', limite_saque_diario)

# Exemplo_Constante

BRAZILIAN_STATES = ["SP","RJ","RS"]
print(BRAZILIAN_STATES)


################# Convertendo_Tipos #################
"""
Converter tipos de dados é necessário em alguns momentos como exemplo, fazer calculos com valores
convertendo um valor inteiro para floot ou ao contrario.
"""
#Exemplo Numero para String
preco = 10.50
print(str(preco))

idade = 28
print(str(idade))

preco = 10.50
idade = 28
texto1 = f"idade {idade} preco {preco}"
print(texto1)

#Exemplo String para Numero
preco = "10.50"
print(float(preco))
idade = "28"
print(int(idade))

#Exemplo float para inteiro
print(int(1.9))

#Exemplo string para inteiro
print(int("10"))

#Exemplo string para float
print(float("10.10"))

#Para trazer o tipo de dado é preciso colocar o type exemplo:
valor = 10
valor_str= str(valor)
print(type(valor))
print(type(valor_str))


################# Funcoes_Entrada_Saida #################
"""
Funcoes para receber valores e mostrar os valores para o usuário
input = recebe valores do teclado e converte para o tipo string
print = utilizada quando queremos exibir os dados e que também é convertido para string na exibição.


"""
#Exemplo Input
nome = input("informe o nome")

#Exemplo print
nome = 'Guilherme'
sobrenome = 'Silva'

print(nome, sobrenome)
print(nome. sobrenome, end="...\n")
print(nome, sobrenome, sep="#")




################# Apostila #################
# https://academiapme-my.sharepoint.com/personal/kawan_dio_me/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkawan%5Fdio%5Fme%2FDocuments%2FSlides%20dos%20Cursos%2FPython%20%2D%20M%C3%B3dulo%20I%20%2D%20Fundamentos%2FCurso%202&ga=1

################# GITHUB #################
"""
Sistema de Controle de Versão Distribuído
- Plataforma de hospedagem de código para controle de versão com Git, e colaboração.
- Registra o histórico de atualizações de um arquivo;
- Gerencia quais foram as alterações, a data, autor, etc.;
- Organização, controle e segurança.


Criação de Repositorio / Comandos
1º Acessar a pasta que deseja fazer o repositorio
2º Executar o comando git init
3º Executar o comando git remote add origin  + link
Ex: git remote add origin https://github.com/username/nome-do-repositorio.git
4º Adicionando conteudo que deseja adicionar ao github é preciso executar o comando git add
5º Adicionar uma mensagem ao commit é preciso executar o comando git commit -m "message"
6° Enviar as alterações feitas no repositorio é preciso executar o comando: git push
7° Como desfazer um commit:
                    git reset
                    git reset --soft
                    git reset --mixed
                    git reset --hard

8° Clonar um Repositorio é preciso executar o comando abaixo:
Ex: git clone https://github.com/username/nome-do-repositorio
9° Links:
        Repositório no GitHub
                    https://git-scm.com/
                    https://docs.github.com/
                    https://github.blog/







Links Úteis
GitHub Quick Start - Repositório com Link para Aulas de Git e GitHub.
https://github.com/digitalinnovationone/github-quickstart

GitBook: Formação GitHub Certification - Material textual sobre GitHub.
https://aline-antunes.gitbook.io/formacao-fundamentos-github 

Documentação do GitHub - Guia completo para uso do GitHub.
https://docs.github.com/

GitHub Markdown - Guia específico para Markdown no GitHub.
https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax


"""