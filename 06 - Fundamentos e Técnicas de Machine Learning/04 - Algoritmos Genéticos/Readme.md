# 🧬 Algoritmos Genéticos - Teoria e Prática

Este repositório contém materiais e exemplos práticos sobre **Algoritmos Genéticos (AG)**, baseados na teoria apresentada pelo Prof. Dr. Diego Bruno. O objetivo é fornecer uma visão completa sobre como os AG funcionam, suas aplicações e exemplos de implementação em Python.

---

## 📖 Sumário
- [O que são Algoritmos Genéticos?](#-o-que-são-algoritmos-genéticos)
- [Etapas de um AG](#-etapas-de-um-ag)
- [Características dos AG](#-características-dos-ag)
- [Aplicações](#-aplicações)
- [Métodos de Implementação](#-métodos-de-implementação)
- [Exemplos Práticos](#-exemplos-práticos)
- [Como Executar](#-como-executar)
- [Referências](#-referências)

---

## 🧩 O que são Algoritmos Genéticos?
Um **Algoritmo Genético (AG)** é uma técnica de busca e otimização inspirada na **genética biológica** e nos princípios da **evolução natural**.  
Eles utilizam operadores como **seleção, crossover (recombinação) e mutação** para gerar soluções aproximadas para problemas complexos.

**Fluxo básico de um AG:**
1. Geração da população inicial
2. Avaliação da população (função de fitness)
3. Seleção dos melhores indivíduos
4. Recombinação (crossover)
5. Mutação
6. Nova população
7. Critério de parada (ótimo global ou número de gerações)

---

## 🔄 Etapas de um AG
- **População inicial**: indivíduos gerados aleatoriamente dentro de uma região de busca.  
- **Função de fitness**: avalia a qualidade de cada indivíduo.  
- **Seleção**: escolha dos melhores indivíduos (ex.: método da roleta).  
- **Crossover**: recombinação de cromossomos para gerar novos indivíduos.  
- **Mutação**: alteração aleatória em genes para evitar convergência prematura.  
- **Nova geração**: população atualizada e ordenada pelo fitness.  

---

## ⚙️ Características dos AG
- São **heurísticos** e **não determinísticos**.  
- Buscam o **ótimo global** em vez de soluções locais.  
- Trabalham bem em problemas **NP-completos**.  
- São aplicáveis em diversas áreas da ciência e tecnologia.  

---

## 🌍 Aplicações
Os AG podem ser aplicados em diferentes áreas, como:
- **Navegação robótica** 🦾  
- **Inteligência Artificial** 🤖  
- **Jogos digitais** 🎮  
- **Chatbots e ensino** 📚  
- **Planejamento de rotas em robôs móveis** 🚗  
- **Problema da Mochila (Knapsack Problem)** 🎒  

---

## 🛠️ Métodos de Implementação
**Passos principais:**
1. **População inicial**: geração aleatória.  
2. **Seleção**: escolha dos melhores indivíduos (ex.: roleta).  
3. **Crossover**: recombinação dos cromossomos.  
4. **Mutação**: pequenas alterações para diversidade.  
5. **Iteração**: repetição até atingir o critério de parada.  

---

## 🧪 Exemplos Práticos
- **Dashboard interativo em Python (Colab)**  
  - Visualização da evolução da população.  
  - Ajuste de taxa e escala de mutação.  

- **Problema da Mochila**  
  - Maximizar o valor dos itens sem ultrapassar o peso máximo.  
  - Exemplo implementado em Python.  

- **Games e agentes inteligentes**  
  - Evolução de comportamento em personagens de jogos.  
  - Exemplo: Dino IA (Google Chrome offline game).  

---

## ▶️ Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/algoritmos-geneticos.git
   cd algoritmos-geneticos

- Instale as dependências:
  pip install -r requirements.txt
- Execute os notebooks no Google Colab ou Jupyter:
- Dashboard Interativo (colab.research.google.com in Bing)
- Problema da Mochila (colab.research.google.com in Bing)

📚 Referências- Prof. Dr. Diego Bruno – Algoritmos Genéticos: Teoria e Prática
- Interactive Genetic Algorithm Dashboard (Colab) (colab.research.google.com in Bing)
- Problema da Mochila com AG (Colab) (colab.research.google.com in Bing)
- https://www.youtube.com/watch?v=P7XHzqZjXQs
- https://www.youtube.com/watch?v=pgaEE27nsQw

👨‍💻 AutorProf. Dr. Diego Bruno- Education Tech Lead na DIO
- Doutor em Robótica e Machine Learning pelo ICMC-USP
