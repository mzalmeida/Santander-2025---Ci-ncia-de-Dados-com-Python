# 📘 Máquina de Vetores de Suporte (SVM) - Teoria e Prática

Este repositório contém materiais de estudo e prática sobre **Máquinas de Vetores de Suporte (Support Vector Machines - SVM)**, baseados nas aulas e conteúdos do **Prof. Dr. Diego Bruno** (Doutor em Robótica e Machine Learning pelo ICMC-USP, Education Tech Lead na DIO).

---

## 📑 Sumário
- [O que são SVMs](#-o-que-são-svms)
- [Tipos de Aprendizado](#-tipos-de-aprendizado)
  - [Supervisionado](#supervisionado)
  - [Não supervisionado](#não-supervisionado)
- [Diferenças entre RNA e SVM](#-diferenças-entre-rna-e-svm)
- [Resultado esperado de uma SVM](#-resultado-esperado-de-uma-svm)
- [Por que "Máquina de Vetores"](#-por-que-máquina-de-vetores)
- [Desenvolvendo a hipótese](#-desenvolvendo-a-hipótese)
- [Implementação](#-implementação)
- [Referências](#-referências)

---

## 🔎 O que são SVMs
- **Support Vector Machines (SVMs)** são algoritmos de aprendizado supervisionado utilizados para classificação e regressão.
- O objetivo é encontrar um **hiperplano ótimo** que separa as classes de forma a maximizar a margem entre os pontos de dados mais próximos.
- Trabalham diretamente com a **fronteira de decisão**.

---

## 📊 Tipos de Aprendizado

### Supervisionado
- Utiliza **dados rotulados** (pares de entrada e saída conhecidos).
- O algoritmo aprende a relacionar entradas com saídas.
- Exemplos: regressão linear, regressão logística, SVM.

### Não supervisionado
- Utiliza **dados não rotulados**.
- O algoritmo busca padrões ou agrupamentos nos dados.
- Exemplos: K-means, PCA.

---

## ⚖️ Diferenças entre RNA e SVM
- **SVM**: busca a **otimização das margens** do hiperplano.
- **RNA (Redes Neurais Artificiais)**: busca o **mínimo global** da função de erro.
- Na prática, ambas podem resolver problemas similares, mas com abordagens diferentes.

---

## 🎯 Resultado esperado de uma SVM
- **Modelo discriminativo**: estima diretamente \( P(y|x) \).
- O que é aprendido: **fronteira de decisão**.
- Exemplos: regressões, SVMs.

---

## 🧩 Por que "Máquina de Vetores"?
- Os **vetores de suporte** são as coordenadas das observações individuais que definem a margem.
- A SVM constrói um **hiperplano** que melhor separa as classes.

---

## 🧠 Desenvolvendo a hipótese
- Dado um conjunto de hiperplanos possíveis (A, B, C), todos podem separar as classes.
- O **hiperplano correto** é aquele que **maximiza a distância** entre os pontos mais próximos das classes e o hiperplano.
- Essa maximização garante maior **generalização** do modelo.

---

## 💻 Implementação
- As SVMs podem ser implementadas em diversas linguagens e frameworks:
  - **Python**: `scikit-learn`, `libsvm`
  - **R**: `e1071`
  - **Matlab**
- Fluxo básico:
  1. Importar dados
  2. Pré-processamento
  3. Treinamento do modelo SVM
  4. Avaliação (acurácia, precisão, recall, F1-score)
  5. Ajuste de parâmetros (kernel, C, gamma)

---

## 📚 Referências
- [Stanford - CS229 Machine Learning Tips](https://stanford.edu/~shervine/l/pt/teaching/cs-229/dicas-aprendizado-nao-supervisionado)
- [Introdução ao Machine Learning - Dataat](https://dataat.github.io/introducao-ao-machine-learning/introdu%C3%A7%C3%A3o.html)
- [Material de Inteligência Artificial - UFPR](https://www.inf.ufpr.br/dagoncalves/IA07.pdf)

---

## 👨‍🏫 Autor
**Prof. Dr. Diego Bruno**  
- Doutor em Robótica e Machine Learning pelo ICMC-USP  
- Education Tech Lead na DIO  

---

## 🚀 Como usar este repositório
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Instale as dependências (se houver código em Python):
pip install -r requirements.txt
- Explore os notebooks e exemplos práticos de SVM.

📝 LicençaEste projeto está sob a licença MIT. Consulte o arquivo [Looks like the result wasn't safe to show. Let's switch things up and try something else!] para mais detalhes.   