'''
############################ Tipos de Banco de Dados

Relacionais/SQL
Não Relacionais/NoSQL (Not OnlySQL)
Orientado a Objetos
Hierárquico

https://www.oracle.com/br/database/what-is-a-relational-database/


############################ Organização da SQL

DQL - Linguagem de Consulta de Dados
SELECT;
DML - Linguagem de Manipulação de Dados 
INSERT, UPDATE e DELETE;
DDL - Linguagem de Definição de Dados
CREATE, ALTER, DROP;
DCL - Linguagem de Controle de Dados
GRANT, REVOKE
DTL - Linguagem de Transação de Dados
BEGIN, COMMIT, ROLLBACK

Referências:
https://www.sqltutorial.org/


 ############################ MER e DER

 O Modelo Entidade-Relacionamento (MER) é representado através de diagramas chamados Diagramas 
 Entidade-Relacionamento (DER).

https://app.creately.com/
https://app.quickdatabasediagrams.com/ - IA

- Entidade = Representacao das tabelas
As entidades são nomeadas com substantivos concretos ou abstratos que 
representem de forma clara sua função dentro do domínio.

- Atributos = caracteristicas e propriedades da tabela
Os atributos são as características ou propriedades das entidades. 
Eles descrevem informações específicas sobre uma entidade. 

- Relacionamentos
Os relacionamentos representam as associações entre entidades

- Cardinalidades
Refere-se a como as entidades se relaciona com as outras.

Relacionamento 1..1 (um para um)
Relacionamento 1..n ou 1..* (um para muitos)
Relacionamento n..n ou *..* (muitos para muitos)

https://clients.cloudclusters.io/ordering/app

- Tabelas
Usada par armazenar dados de forma organizada, cada tabela tem um numero unico e é divida em colunas e linhas.

- Colunas
Coluna é uma estrutura dentro de uma tabela que representa um atributo especifico de dados armazenado.
cada coluna tem um nome unico e um tipo de dado associado que define o tipo de informação que ira armazenar
Ex: numero, texto, data  e etc.

- Registro
É conhecido como linha ou tupla, é uma instancia individual de dados

############################ Comando: CREATE TABLE
Ex: CREATE TABLE {{nome}} 
({{coluna}} {{tipo}} {{opções}} COMMENT {{‘COMENTARIO´}});

############################ Tipos de dados:
Os dados podem variar muito entre os diversos SGBD, os mais comuns são:
Inteiro (Integer)
Decimal/Numérico (Decimal/Numeric)
Caractere/Varchar (Character/Varchar)
Data/Hora (Date/Time)
Booleano (Boolean)
Texto longo (Text)

- Restrições de valor:
NOT NULL
UNIQUE
DEFAULT
Chaves primárias e estrangeiras
Auto Incremento

############################ Comando: INSERT
INSERT INTO
  {{ nome-tabela }}
  ([ coluna1, coluna2, … ]) *** você pode ocultar as colunas
VALUES
  ([ valor-coluna1, valor-coluna2, … ])


############################ Comando: SELECT
SELECT {{ lista_colunas}}
FROM tabela;

Onde * retorna todas as colunas

############################ Comando: SELECT com Where
SELECT {{ lista_colunas}}
FROM tabela
WHERE {{condicao}};

############################ Comando: SELECT - Operadores

= (igualdade)
<> ou != (desigualdade)
> (maior que)
< (menor que)
>= (maior ou igual que)
<= (menor ou igual que)
LIKE (comparação de padrões)
IN (pertence a uma lista de valores)
BETWEEN (dentro de um intervalo)
AND (e lógico)
OR (ou lógico)


############################ Comando: Update

UPDATE {{ tabela }}
SET
 {{ coluna_1 }} = {{ novo_valor_1 }},
 {{ coluna_2 }} = {{ novo_valor_2 }}
WHERE
  {{ condicao }} ;


############################ Comando: Delete
DELETE FROM
        {{ tabela }}
WHERE
        {{ condicao }};

############################ Links Úteis

Referências:
https://mariadb.com/kb/en/data-types/
https://mariadb.com/kb/en/create-table/
https://clients.cloudclusters.io/
https://github.com/pamelaborges/dio-bd-relacional
https://mariadb.com/kb/en/alter-table/
https://mariadb.com/kb/en/drop-table/
https://mariadb.com/kb/en/data-types/
https://mariadb.com/kb/en/create-table/
São 6 ao todo, para mais detalhes consultar
 https://pt.wikipedia.org/wiki/Normaliza%C3%A7%C3%A3o_de_dados
https://pt.wikipedia.org/wiki/Normaliza%C3%A7%C3%A3o_de_dados
https://github.com/pamelaborges/dio-bd-relacional
https://mariadb.com/kb/en/joins/
https://github.com/pamelaborges/dio-bd-relacional
https://mariadb.com/kb/en/aggregate-functions/
https://github.com/pamelaborges/dio-bd-relacional
https://mariadb.com/kb/en/alter-table/#add-index










############################ Chaves Primária
Identifica exclusivamente
Não pode conter valores nulos (NULL) 
Uma tabela pode ter apenas uma chave primária.

CREATE TABLE {{tabela}}
( ID PRIMARY KEY AUTOINCREMENT,
    … );
ALTER TABLE {{tabela}}
MODIFY COLUMN ID INT PRIMARY KEY;

############################ Chaves Estrangeira
Ela é usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas
Pode ser nula (NOT NULL); ** registro órfão
É possível ter mais de uma (ou nenhuma) em uma tabela.

CREATE TABLE {{tabela }} (
  id INT PRIMARY KEY,
  chave_estrangeira INT,
  FOREIGN KEY (chave_estrangeira) REFERENCES {{outra tabela }} (id)
);

ALTER TABLE {{ tabela }}
ADD CONSTRAINT {{nome_constraint }} 
FOREIGN KEY (ID_) 
REFERENCES {{outra_tabela}} (ID)

Chaves Estrangeira - Restrições
ON DELETE especifica o que acontece com os registros dependentes quando um registro pai é excluído.
ON UPDATE define o comportamento dos registros dependentes quando um registro pai é atualizado.
CASCADE, SET NULL, SET DEFAULT e RESTRICT


############################ Normalização de Dados
A normalização de dados é um processo no qual se organiza e estrutura um banco de dados 
relacional de forma a eliminar redundâncias e anomalias, garantindo a consistência e 
integridade dos dados. 

1º Formas Normais
1FN: Atomicidade de dados
A 1FN estabelece que cada valor em uma tabela deve ser atômico, ou seja, indivisível. 
Nenhum campo deve conter múltiplos valores ou listas. No seu caso, o campo "endereco"
contém múltiplos valores, como rua, número, cidade e estado. Para atingir a 1FN, 
precisamos dividir o campo "endereco" em colunas separadas.
Ex: dividir o endereço em varios campos, logradouro,cep,numero,estado,cidade,complemento

2°2FN
A 2FN estabelece que uma tabela deve estar na 1FN .
Todos os atributos não chave devem depender totalmente da chave primária. 
Dica se sua tabela tem uma chave primária simples não existe a 
possibilidade de termos dependência parcial e por tanto ela já se encontra na 2FN
obs: se a tabela já tem chave primaria ela já está no 2fn

3FN
Uma tabela deve estar na 2FN .
Nenhuma coluna não-chave depender de outra coluna não-chave. 
Nosso exemplo: Relação Estado -> Cidade
obs: todos os atributos tem que depender do ID

Resumo
A 1FN garante que cada valor seja atômico e que os registros sejam únicos e identificáveis.
A 2FN garante que os atributos não chave dependam totalmente da chave primária, 
evitando dependências parciais.
A 3FN elimina dependências transitivas entre os atributos não chave, 
garantindo que cada atributo não chave dependa apenas da chave primária, 
não havendo dependências indiretas entre eles.



############################ Consultas Avançadas

Junções: JOINs
São usadas no SQL para combinar dados de duas ou mais tabelas relacionadas em uma única consulta

Junções: Tipos

INNER JOIN
LEFT JOIN ou LEFT OUTER JOIN
RIGHT JOIN ou RIGHT OUTER JOIN
FULL JOIN ou FULL OUTER JOIN

INNER JOIN
Retorna apenas as linhas que têm correspondência em ambas as tabelas envolvidas na junção. A junção é feita com base em uma condição de igualdade especificada na cláusula ON.
SELECT *
FROM tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

LEFT JOIN
Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondentes da tabela à direita. Se não houver correspondência, os valores da tabela à direita serão NULL.
SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

RIGHT JOIN
Retorna todas as linhas da tabela à direita da junção e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, os valores da tabela à esquerda serão NULL.
SELECT *
FROM tabela1
RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

FULL JOIN
Retorna todas as linhas de ambas as tabelas envolvidas na junção, combinando-as com base em uma condição de igualdade. Se não houver correspondência, os valores ausentes serão preenchidos com NULL.
SELECT *
FROM tabela1
FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

Sub Consultas
Elas permitem realizar consultas mais complexas permitindo que você use o 
resultado de uma consulta como entrada para outra consulta.

As subconsultas podem ser usadas em várias partes de uma consulta:
SELECT
FROM
WHERE
HAVING 
JOIN. 

select * from destinos d where id not in (select id_destino from reservas)
select nome, (select count(*) from reservas r where r.id_usuario = u.id_usuario) 
as total_reservas from usuario u

OBS: inner join traz na consulta da tabela da esquerda,
apenas os dados que tem correspondencia na tabela direita.

O left join retorna os dados da tabela da esquerda e aqueles que ele localizar na direita.
O que ele não localizar ele retorna como nulo.

O rigth join é o contrario retorna os dados da tabela da direita e o que localizar na tabela da esquerda.
O que não localizar ele retorna nulo

############################ Funcoes Agregadas

COUNT: Conta o número de registros.
SUM: Soma os valores de uma coluna numérica.
AVG: Calcula a média dos valores de uma coluna numérica.
MIN: Retorna o valor mínimo de uma coluna.
MAX: Retorna o valor máximo de uma coluna.

EX: SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade FROM usuario u

Agrupamento de Resultados
SELECT …
FROM …
GROUP BY

EX: SELECT COUNT(*),id_destino FROM reservas GROUP BY id_destino

Limite de Resultados
SELECT …
FROM …
GROUP BY …
LIMIT {{numero}}
OFFSET {{numero}} *** opcional

Ordenação de Resultados
SELECT …
FROM …

ORDER BY
ASC
DESC
Multiplas Colunas

Ex: SELECT COUNT(*) as qtd_res,id_destino FROM reservas GROUP BY id_destino order by qtd_res



max = calcula o total de linhas
timestampdiff = calcula diferenca de uma data entre outra data, primeiro parametro no caso acima
é o ano que queremos ver a diferença, o proximo paremtro é a coluna que serve diferenca no caso data_nascimento, e o ultimo é a data quer quer comparar
usar o current_data traz a data atual do banco


############################ Análise do Plano de Execução
Ela nos permite examinar as operações realizadas, as tabelas acessadas, 
os índices utilizados e outras informações importantes para identificar possíveis melhorias 
de desempenho.

EXPLAIN
	SELECT * 
	FROM {{TABELA}}
    
    select_type:"SIMPLE", "SUBQUERY" , "JOIN" 
table.
type: "ALL" , "INDEX" entre outros
possible_keys: Os índices possíveis que podem ser utilizados na operação.
key: O índice utilizado na operação, se aplicável.
key_len: O comprimento do índice utilizado.
ref: As colunas ou constantes usadas para acessar o índice.
rows

Esses recursos são fundamentais para melhorar o desempenho das consultas 
e otimizar a recuperação de informações em bancos de dados.

CREATE INDEX {{nome_index}}
 ON {{tabela}} ({{coluna1, coluna2…}});


















































'''

