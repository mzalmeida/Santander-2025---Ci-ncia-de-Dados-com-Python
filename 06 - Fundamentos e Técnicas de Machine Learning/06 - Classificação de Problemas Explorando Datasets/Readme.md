# 📘 DATASETS: Teoria e Prática

Projeto baseado nas aulas e materiais do **Prof. Dr. Diego Bruno**  
Education Tech Lead na DIO | Doutor em Robótica e Machine Learning pelo ICMC-USP  

---

## 📑 Sumário
- [O que é um Dataset?](#-o-que-é-um-dataset)
- [Como devem ser minhas amostras?](#-como-devem-ser-minhas-amostras)
- [Como criar um Dataset?](#-como-criar-um-dataset)
- [Serviços de Datasets](#-serviços-de-datasets)
- [SVM - Máquinas de Vetores de Suporte](#-svm---máquinas-de-vetores-de-suporte)
- [Tipos de Aprendizado](#-tipos-de-aprendizado)
- [Diferenças entre RNA e SVM](#-diferenças-entre-rna-e-svm)
- [Resultado esperado de uma SVM](#-resultado-esperado-de-uma-svm)
- [Por que "Vetores"?](#-por-que-vetores)
- [Desenvolvendo a hipótese](#-desenvolvendo-a-hipótese)
- [Algoritmos](#-algoritmos)
- [Referências](#-referências)

---

## 🐶🐱 O que é um Dataset?
Um **dataset** é uma coleção organizada de dados que pode ser utilizada para treinar, validar e testar modelos de Machine Learning.  
Exemplo clássico: classificação de imagens de **gatos e cachorros**.

---

## 📊 Como devem ser minhas amostras?
- As amostras devem estar **rotuladas** (ex.: `Dog`, `Cat`).
- Devem ser **balanceadas** para evitar viés no treinamento.
- Devem estar **limpas** (sem ruídos ou dados irrelevantes).

---

## 🛠️ Como criar um Dataset?
- Coletar dados de fontes confiáveis.
- Realizar **pré-processamento** (remoção de duplicatas, normalização, padronização).
- Rotular manualmente ou com auxílio de ferramentas.
- Dividir em **treino, validação e teste**.

---

## 🌐 Serviços de Datasets
Top 5 fontes para datasets de Machine Learning e Analytics:

| Fonte | Descrição |
|-------|-----------|
| **UCI Machine Learning Repository** | Repositório clássico de datasets acadêmicos |
| **.gov Datasets** | Bases públicas governamentais |
| **Google Dataset Search** | Ferramenta de busca de datasets |
| **Kaggle Datasets** | Comunidade com milhares de datasets e competições |
| **AWS Datasets** | Conjunto de dados hospedados na Amazon |

---

## 🧮 SVM - Máquinas de Vetores de Suporte
- Algoritmo supervisionado para classificação e regressão.
- Busca encontrar o **hiperplano ótimo** que separa as classes.
- Utiliza **vetores de suporte** (pontos mais próximos da fronteira de decisão).

---

## 📚 Tipos de Aprendizado
### 🔹 Supervisionado
- Dados rotulados (entrada → saída conhecida).
- Exemplos: regressão linear, SVM, redes neurais.

### 🔹 Não supervisionado
- Dados **não rotulados**.
- Algoritmos agrupam ou reduzem dimensionalidade.
- Exemplos: K-Means, PCA.

---

## 🔄 Diferenças entre RNA e SVM
- **SVM**: busca otimizar margens de separação entre classes.  
- **RNA (Redes Neurais Artificiais)**: busca o **mínimo global** através de múltiplas camadas e funções de ativação.  

---

## 🎯 Resultado esperado de uma SVM
| Característica | Descrição |
|----------------|-----------|
| **Objetivo** | Estimar diretamente P(y|x) |
| **O que é aprendido** | Fronteira de decisão |
| **Exemplos** | Regressões, SVMs |

---

## 📐 Por que "Vetores"?
- Os **vetores de suporte** são as coordenadas das observações mais próximas da fronteira.  
- Eles definem o hiperplano que separa as classes.

---

## 🧩 Desenvolvendo a hipótese
- Existem múltiplos hiperplanos possíveis (A, B, C).  
- O **melhor hiperplano** é aquele que **maximiza a margem** entre as classes.  
- SVM é robusto contra **outliers**.

---

## ⚙️ Algoritmos
- **SVM (Support Vector Machines)**  
- **RNA (Redes Neurais Artificiais)**  
- **K-Means (Clusterização)**  
- **Regressão Linear/Logística**  

---

## 📚 Referências
- [Cats vs Dogs Image Classification - CNN](https://www.linkedin.com/pulse/cats-vs-dogs-image-classification-using-cnn-piyush-pareek)  
- [Stanford CS229 - Aprendizado Não Supervisionado](https://stanford.edu/~shervine/l/pt/teaching/cs-229/dicas-aprendizado-nao-supervisionado)  
- [Introdução ao Machine Learning - DataAt](https://dataat.github.io/introducao-ao-machine-learning/introdu%C3%A7%C3%A3o.html)  
- [IA - UFPR](https://www.inf.ufpr.br/dagoncalves/IA07.pdf)  

---

## 👨‍🏫 Autor
**Prof. Dr. Diego Bruno**  
Education Tech Lead na DIO  
Doutor em Robótica e Machine Learning pelo ICMC-USP