'''
###################  O que é o MongoDB
❏ Banco de dados NoSQL orientado a documentos.
❏ Grandes volumes de dados, escalabilidade horizontal e
modelagem flexível.
❏ Não exige um esquema
❏ Permite que os documentos sejam armazenados em
formato BSON (Binary JSON), proporcionando uma
estrutura semiestruturada.


- Vantagens
❏ Flexibilidade na modelagem de dados.
❏ Escalabilidade horizontal para lidar com grandes volumes
de dados.
❏ Consultas ricas e suporte a consultas complexas.
❏ Alta disponibilidade e tolerância a falhas.
❏ Comunidade ativa e recursos de suporte.

- Desvantagens
❏ Menor consistência imediata em comparação com bancos
de dados relacionais.
❏ Consultas complexas podem exigir um maior conhecimento
e planejamento adequado.
❏ Maior consumo de espaço de armazenamento em
comparação com bancos de dados relacionais devido à
flexibilidade dos documentos.

- Onde o MongoDB é usado

❏ Aplicações web: Onde a flexibilidade e a escalabilidade são
cruciais para lidar com volumes variáveis de dados.
❏ Análise de big data: Análise de grandes volumes de dados
não estruturados ou semiestruturados, fornecendo uma
plataforma para armazenar e processar esses dados.
❏ Armazenamento de dados semiestruturados: Permite a
inserção de documentos com estruturas diferentes em
uma mesma coleção.
❏ Casos de uso de geolocalização: Com suas funcionalidades
de consulta geoespacial, é adequado para casos de uso que
envolvem dados baseados em localização, como aplicativos
de mapeamento e rastreamento.

- Links Uteis
 https://www.mongodb.com/docs/manual/introduction/


 ################### Instalação e configuração do MongoDB (Atlas)

 ❏ https://cloud.mongodb.com/
  https://www.mongodb.com/docs/atlas/getting-started/

  - Modelagem de dados usando documentos

  - Coleções
❏ Agrupamento lógico de documentos
❏ Não exige esquema ou que os documentos tenham a mesma estrutura

- Caracteristicas
❏ Os nomes das coleções devem seguir algumas regras:
❏ Devem começar com uma letra ou um underscore (_).
❏ Podem conter letras, números ou underscores.
❏ Não podem ser vazios.
❏ Não podem ter mais de 64 bytes de comprimento.

- Documentos:
❏ São armazenados em documentos BSON (Binary JSON),
que são estruturas flexíveis e semiestruturadas.
❏ Cada documento possui um identificador único chamado
"_id"
❏ É composto por pares de chaves e valores.
❏ Tamanho máximo: Cada documento no MongoDB pode ter
um tamanho máximo de 16 MB
❏ Aninhamento de documentos
❏ Flexibilidade na evolução do esquema

- Tipos de Dados Simples
❏ String
❏ Number
❏ Boolean
❏ Date
❏ Null
❏ ObjectId

- Tipos de Dados Complexas
❏ Array
❏ Documento Embutido (Embedded Document)
❏ Referência (Reference)
❏ GeoJSON

- Estrutura de um documento
{
_id: ObjectId(“”),
“nome_campo”: “valor_campo”,
…
}

- Modelagem da estrutura do Usuário e Destinos
https://jsonformatter.curiousconcept.com/

-  Referências:
○ https://www.mongodb.com/docs/manual/reference/bson-types/
○ https://www.mongodb.com/docs/manual/reference/geojson/#std-label-geojson-point


{
   "_id":1,
   "nome":"Mateus Zilio de Almeida",
   "idade":30,
   "data_nascimento":"1994-01-03",
   "endereco":"Via Orlando jose scutti, 245...",
   "enderecos":{
      "logradouro":"Via Orlando...",
      "numero":123,
      "bairro":"Park Imperador",
      "cidade":"Araraquara"
   }
}

{
"_id":1,
"nome":"Rodoviaria",
"descricao":"Rodoviaria central",
"localizacao":{
"type":"Point",
"coordinates":[-46.661056, -23.587384]

}

}


- Estratégias de modelagem de dados eficientes e escaláveis
 - Modelagem orientada por consultas
 ❏ A modelagem de dados no MongoDB deve ser orientada
pelas consultas que serão realizadas com mais frequência

- Inner Documents
No MongoDB, é comum denormalizar os dados para evitar
operações de junção (join) custosas. Isso significa que os dados
relacionados podem ser armazenados juntos em um único
documento, em vez de serem distribuídos em várias coleções.

- Modelar usuário com estratégia desnormalizada
https://jsonformatter.curiousconcept.com/

- Quando usar

❏ Os dados aninhados são específicos para o documento pai.
❏ Os dados aninhados são sempre acessados juntamente
com o documento pai.
❏ A cardinalidade do relacionamento é um-para-muitos (um
usuário pode ter várias reservas).

- Quando NÃO usar
❏ Se os dados aninhados precisarem ser consultados e
atualizados independentemente do documento pai, é mais
adequado utilizar coleções separadas.

Referências
❏ Forma de relacionar os documentos entre si.


- Modelar usuário com estratégia de referência
{
   "_id":1,
   "nome":"Mateus Zilio de Almeida",
   "idade":30,
   "data_nascimento":"1994-01-03",
   "endereco":"Via Orlando jose scutti, 245...",
   "enderecos":{
      "logradouro":"Via Orlando...",
      "numero":123,
      "bairro":"Park Imperador",
      "cidade":"Araraquara"
   }],
"interesses": ["kart", "culinaria"],
"reservar": [ ObjectId("123", Object("234")
]
}

{
"_id": ObjectId("123"),
"destino": ObjecId("456"),
"data": "2023-10-10",
"status": "pendente",
"usuario":ObjectId(345)
}

  - Quando usar

❏ Os dados têm seu próprio significado e podem ser
acessados independentemente do documento pai.
❏ Os dados têm uma cardinalidade mais alta (por exemplo,
vários usuários podem ter reservas).

- Quando NÃO usar
❏ Se os dados aninhados precisarem ser consultados e
atualizados independentemente do documento pai, é mais
adequado utilizar coleções separadas.

● Referências:
○ https://www.luiztools.com.br/post/padroes-para-modelagem-dedados-documentos-em-mongodb/


















'''