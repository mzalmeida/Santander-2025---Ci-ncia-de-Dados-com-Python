'''
################ O que é um Banco de Dados não relacional?

Termo correto: NOT Only SQL
❏ Não seguem modelo de tabelas e relacionamentos
❏ Projetados para lidar com alto volume de dados, alta
escalabilidade
❏ Alta flexibilidade na estrutura de dados
❏ Eles são amplamente utilizados em cenários onde a
consistência imediata dos dados não é crítica

Diferenças
SQL                                             NoSQL
Modelo de dados fixo                       Modelo de dados flexivel
Escalabilidade vertical (hardware)         Escalabilidade horizontal
Transações ACID 100%                       Transações ACID ausentes total ou parcial
LInguagem de consulta SQL                  Cada SGBD tem sua própria

Vantagens dos bancos de dados NoSQL
Flexibilidade na modelagem
❏ Alta escalabilidade
❏ Melhor desempenho em cenário de consulta intensiva
❏ Tolerância a falhas

Desvantagens dos bancos de dados NoSQL

Menor consistência de dados imediata
❏ Menor suporte a consultas complexas ** depende do
SGBD

Links Úteis
https://www.oracle.com/br/database/nosql/what-is-nosql


################ Visão geral dos tipos de NoSQL

Tipos
❏ Key
-Value
❏ Documento
❏ Coluna 
❏ Grafos 
❏ entre 
outros
…
Key-Value > Chave Valor
Armazena dados como pares de chave e valor, onde cada
chave é um identificador único para acessar o valor
correspondente
Exemplo de SGBD: Redis, Riak, Amazon DynamoDB
Uso: Um site pode usar um banco de dados Redis para
armazenar informações de sessão de usuário


Document > Documento
Armazenam dados em documentos semiestruturados,
geralmente em formato JSON ou BSON
Exemplo de SGBD: MongoDB, Couchbase, Apache
CouchDB
Uso: Um catálogo de e-commerce pode usar o MongoDB
para armazenar informações de produtos, como nome,
descrição, preço e atributos adicionais.

Coluna
Armazenam dados em formato de colunas, o que permite
alta escalabilidade e eficiência em determinados tipos de
consultas
Exemplo de SGBD: Apache Cassandra, ScyllaDB, HBase
Uso: Um sistema de registro de aplicativos pode usar o
Apache Cassandra para armazenar registros de log.

Grafo
Armazenar e consultar dados interconectados, onde os
relacionamentos entre os dados são tão importantes
quanto os próprios dados
Exemplo de SGBD: Neo4j, Amazon Neptune, JanusGraph
Uso: Uma rede social pode usar o Neo4j para armazenar os
perfis dos usuários e suas conexões, permitindo consultas
eficientes para encontrar amigos em comum.

Links Úteis

https://www.oracle.com/br/database/nosql/what-is-nosql















'''