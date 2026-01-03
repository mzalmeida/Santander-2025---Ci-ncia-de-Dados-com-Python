############################################################
# INTRODUÇÃO AO ETL
############################################################

# ETL significa:
# Extract (Extrair)
# Transform (Transformar)
# Load (Carregar)

# ETL é um tipo de integração de dados (Data Integration)
# utilizado para combinar dados provenientes de diversas fontes.
# É amplamente utilizado na construção de Data Warehouses e Data Marts.

# O processo ETL consiste em:
# - Extrair dados de sistemas-fonte
# - Transformar esses dados conforme regras de negócio
# - Carregar os dados em um destino final (Data Warehouse, Data Mart ou Data Lake)

# Existe também a abordagem ELT (Extract, Load, Transform),
# onde a transformação ocorre no banco de dados de destino,
# melhorando a performance ao usar o poder de processamento do banco.

############################################################
# FERRAMENTAS DE ETL
############################################################

# Exemplos de ferramentas de ETL comerciais:
# - IBM Information Server (DataStage)
# - Oracle Data Integrator (ODI)
# - Informatica PowerCenter
# - Microsoft SQL Server Integration Services (SSIS)

# Ferramentas Open Source de ETL:
# - Pentaho Data Integrator (PDI)
# - Talend ETL

# As ferramentas de ETL automatizam:
# - Extração
# - Transformação
# - Carregamento
# - Controle de qualidade
# - Metadados
# - Performance e segurança

############################################################
# PROCESSO DE ETL
############################################################

# O processo de ETL possui etapas bem definidas:

# 1) Mapeamento
# - Identificação das fontes de dados
# - Definição dos atributos
# - Armazenamento em uma área temporária (Staging Area)

# 2) Extração
# - Comunicação com sistemas ou bancos de dados de origem
# - Captura dos dados brutos

# 3) Transformação
# - Limpeza dos dados (remoção de erros)
# - Padronização (tipos, formatos, nomenclaturas)
# - Complementação (enriquecimento dos dados)
# - Garantia da qualidade da informação

# 4) Load (Carga)
# - Leitura dos dados da Staging Area
# - Carregamento no Data Warehouse ou Data Mart final

############################################################
# ETAPAS DO PROCESSO ETL
############################################################

# As três etapas principais do ETL são:

# 1) Extract
# Consiste em capturar dados de diferentes sistemas de origem.
# Pode envolver múltiplas tecnologias e formatos.

# 2) Transform
# Etapa mais complexa do ETL.
# Envolve:
# - Padronização de dados
# - Conversão de tipos (ex: VARCHAR2 Oracle x VARCHAR SQL Server)
# - Limpeza
# - Qualidade dos dados

# 3) Load
# Etapa final do processo.
# Os dados são carregados no destino final:
# - Data Warehouse
# - Data Mart

############################################################
# VANTAGENS DAS FERRAMENTAS DE ETL
############################################################

# Principais vantagens:

# - Garantia de qualidade dos dados
# - Execução automatizada de cargas
# - Facilidade de desenvolvimento, mesmo para usuários não técnicos
# - Manutenção mais simples que código manual
# - Geração automática de metadados
# - Alta performance para grandes volumes de dados
# - Capacidade de reinício de cargas interrompidas
# - Melhor controle de segurança e estabilidade
# - Facilidade de integração com múltiplas fontes (SAP, Mainframe, VSAM, etc.)

############################################################
# ETL PARA BIG DATA
############################################################

# Com o crescimento do Big Data, as ferramentas de ETL evoluíram
# para se integrar a ambientes distribuídos.

# Hadoop é uma plataforma de computação distribuída em Java
# focada em processamento de grandes volumes de dados,
# com tolerância a falhas.

# No contexto de Big Data:
# - O processo de carga é conhecido como Ingestão de Dados
# - Geralmente corresponde à etapa de Extract

# Ferramentas do ecossistema Hadoop:
# - SQOOP: movimentação de dados entre bancos relacionais e Hadoop
# - HIVE: ambiente SQL sobre Hadoop
# - PIG: linguagem de script para processamento de dados
# - SPARK: framework de processamento em memória

############################################################
# BIBLIOTECA PANDAS
############################################################

# Pandas é uma biblioteca Python para análise e manipulação de dados.
# Permite trabalhar com:
# - Dados tabulares (Excel, SQL)
# - Séries temporais
# - Matrizes
# - Conjuntos de dados não rotulados

# Principais estruturas de dados do Pandas:

# Series:
# - Estrutura unidimensional
# - Semelhante a uma coluna do Excel
# - Possui índice (numérico ou rotulado)

# DataFrame:
# - Estrutura tabular bidimensional
# - Semelhante a uma planilha do Excel
# - Possui linhas e colunas rotuladas

# Principais funcionalidades:
# - df.shape: retorna dimensões do DataFrame
# - df.info(): informações sobre tipos e memória
# - df.columns: visualização e alteração de nomes de colunas
# - unique(): valores únicos de uma Series
# - plot(): visualização gráfica
# - Estatísticas descritivas

############################################################
# BIBLIOTECA SCIKIT-LEARN
############################################################

# Scikit-learn é uma biblioteca de Machine Learning em Python.
# Fornece ferramentas simples e eficientes para análise preditiva.

# Características:
# - Código aberto
# - Reutilizável
# - Construída sobre NumPy, SciPy e Matplotlib

# Exemplo de criação de dados:
# - make_regression
# - n_samples = 200
# - n_features = 1
# - noise define a dispersão dos dados

# Criação de modelo:
# - LinearRegression
# - Método fit(): treina o modelo
# - Método predict(): realiza previsões

# Visualização:
# - scatter(): pontos reais
# - plot(): reta de regressão

############################################################
# CONCLUSÃO
############################################################

# ETL é a base de qualquer processo de engenharia de dados.
# Ferramentas de ETL facilitam a integração, qualidade e governança dos dados.
# Pandas auxilia na manipulação e análise dos dados.
# Scikit-learn permite criar modelos de Machine Learning
# utilizando dados preparados por processos de ETL.

# Link Uteis

# https://github.com/spotify/luigi
# https://anaconda.org/
# https://colab.google/
# https://github.com/diegobrunoDIO?tab=repositories