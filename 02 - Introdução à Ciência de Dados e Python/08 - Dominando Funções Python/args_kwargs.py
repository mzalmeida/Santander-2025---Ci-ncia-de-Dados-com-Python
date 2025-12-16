# Utilizando args e kwargs podemos combinar parametros, e esses quando definidos o método recebe os valores como tupla e dicionario respectivamente.
# args = vem em uma tupla (valores separados por virgula)
# kwargs = vem no dicionario(chave e valor)

# Ex:
'''
Neste programa foi definido a funcao exibir_poema, ela recebe 3 argumentos (data_extenso, *args e **kwargs)
Na variavel texto pega todos os argumentos que vierem de args e concatena com \n (quebrar linha)
Na variavel meta_dados, é recebido o kwargs, coloca o .items porque ele é um dicionario, o .items irá entregar uma lista de tlupas de chave e Valor 
e ira iterar(FOR) essa lista de tuplas criando uma string onde coloca a chave : o valor quebrando por linha \n. 
Na variavel mensagem é colocado a data por extenso com duas quebras de linha mostrando o texto e meta_dados
e exibe a mensagem com o print.
A ideia é passar uma data que irá exibir quando o poema, a lista de versos e as informacoes do poema (autor, livros e etc)
'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("terca-feira, 16 de dezembro de 2025","Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

