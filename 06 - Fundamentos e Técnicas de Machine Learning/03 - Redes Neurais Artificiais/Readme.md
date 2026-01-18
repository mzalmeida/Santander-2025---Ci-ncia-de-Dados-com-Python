# 📘 Redes Neurais Artificiais - Teoria e Prática

Este repositório contém materiais de estudo e prática sobre **Redes Neurais Artificiais (RNA)**, baseados no conteúdo do Prof. Dr. Diego Bruno (Doutor em Robótica e Machine Learning pelo ICMC-USP, Education Tech Lead na DIO).

---

## 📑 Sumário
- [Introdução](#introdução)
- [O que são Redes Neurais](#o-que-são-redes-neurais)
- [Estrutura de uma RNA](#estrutura-de-uma-rna)
- [Redes Biológicas x Artificiais](#redes-biológicas-x-artificiais)
- [Neurônio Artificial](#neurônio-artificial)
- [Entrada e Saída](#entrada-e-saída)
- [Análise de Características (Features)](#análise-de-características-features)
- [Classificação](#classificação)
- [Dataset](#dataset)
- [Treinamento](#treinamento)
- [Algoritmo de Aprendizado](#algoritmo-de-aprendizado)
- [Importando Modelos de RNA](#importando-modelos-de-rna)
- [Exemplo no Google Colab](#exemplo-no-google-colab)
- [Referências](#referências)

---

## 🚀 Introdução
As **Redes Neurais Artificiais (RNA)** são modelos computacionais inspirados no funcionamento do cérebro humano. Elas são amplamente utilizadas em tarefas de:
- Reconhecimento de padrões
- Classificação de imagens
- Processamento de linguagem natural
- Previsão de séries temporais

---

## 🧠 O que são Redes Neurais
Uma RNA é composta por **neurônios artificiais** que recebem entradas, aplicam pesos e funções de ativação, e produzem saídas.

---

## 🔬 Estrutura de uma RNA
- **Entradas (X)**: dados de entrada
- **Pesos (W)**: parâmetros ajustáveis
- **Função soma (Σ)**: combina entradas e pesos
- **Função de ativação (g)**: define se o neurônio dispara ou não
- **Saída (y)**: resultado final

---

## 🧩 Redes Biológicas x Artificiais
| Redes Biológicas | Redes Artificiais |
|------------------|-------------------|
| Neurônio, axônio, dendritos | Unidade de processamento, pesos, função de ativação |
| Sinais elétricos | Dados numéricos |
| Sinapses | Conexões entre neurônios artificiais |

---

## ⚡ Neurônio Artificial
O neurônio artificial é modelado como:
\[
y = g\left(\sum_{i=1}^{n} w_i \cdot x_i - \theta \right)
\]

Onde:
- \(x_i\): entradas
- \(w_i\): pesos
- \(\theta\): limiar
- \(g\): função de ativação (sigmóide, ReLU, etc.)

---

## 🔄 Entrada e Saída
- **Entrada**: dados brutos (imagens, texto, números)
- **Processo**: combinação linear + função de ativação
- **Saída**: classificação ou previsão

---

## 🕵️ Análise de Características (Features)
As RNAs extraem **features** automaticamente:
- Camadas iniciais → bordas, linhas
- Camadas intermediárias → formas, texturas
- Camadas profundas → objetos complexos (faces, animais, etc.)

---

## 🐱 Classificação
Exemplo clássico: **classificação de imagens de gatos e não-gatos**.  
Dataset: **MNIST** (dígitos manuscritos) também é amplamente usado.

---

## 📂 Dataset
Os datasets são divididos em:
- **Treino**: usado para ajustar os pesos
- **Validação**: usado para avaliar desempenho
- **Teste**: usado para medir generalização

---

## 🏋️ Treinamento
Durante o treinamento:
1. Inicialização de pesos aleatórios
2. Propagação dos dados pela rede
3. Comparação da saída com o valor esperado
4. Cálculo do erro
5. Ajuste dos pesos (backpropagation)

---

## 📊 Algoritmo de Aprendizado
Fluxo simplificado:---

## 🐍 Importando Modelos de RNA
Exemplo com **ResNet50** em TensorFlow/Keras:

```python
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Carregar modelo pré-treinado
model = ResNet50(weights='imagenet')

# Preparar imagem
img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Predição
preds = model.predict(x)
print('Predição:', decode_predictions(preds, top=3)[0])

💻 Exemplo no Google Colab
Notebook de exemplo:
Redes Neurais com TensorFlow - Colab (colab.research.google.com in Bing)
Outro exemplo:
Mask R-CNN Demo - Colab (colab.research.google.com in Bing)

📚 Referências
- Medeiros (2006) - Modelo de Perceptron de Rosenblatt
- Prof. Dr. Diego Bruno - Material didático
- TensorFlow/Keras Documentation
- Datasets: MNIST, ImageNet

👨‍💻 Autor
Prof. Dr. Diego Bruno
Education Tech Lead na DIO
Doutor em Robótica e Machine Learning pelo ICMC-USP

📜 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.

----
