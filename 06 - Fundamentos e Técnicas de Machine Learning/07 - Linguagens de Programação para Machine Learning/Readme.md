# Linguagens de Programação para Machine Learning

Este repositório contém materiais e exemplos relacionados às principais **linguagens de programação** e **paradigmas** aplicados em **Machine Learning (ML)**.  
O conteúdo foi elaborado pelo **Prof. Dr. Diego Bruno**, Education Tech Lead na DIO e Doutor em Robótica e Machine Learning pelo ICMC-USP.

---

## 📚 Conteúdo

- Introdução às linguagens de programação para ML
- Exemplos práticos com **Python** e bibliotecas como TensorFlow/Keras
- Paradigmas de programação:
  - Imperativo
  - Lógico
  - Funcional
  - Orientado a Objetos
  - Multi-paradigma
- Demonstrações com linguagens como **Python, R e Scilab**
- Conceitos fundamentais de abstração, herança, polimorfismo e encapsulamento

---

## 🖥️ Linguagens abordadas

- **Python** → Principal linguagem para ML, com suporte a bibliotecas como TensorFlow, Keras, Scikit-learn, PyTorch.
- **R** → Forte em estatística e análise de dados.
- **Scilab** → Ambiente numérico multi-paradigma, útil para simulações matemáticas.

---

## 🔑 Paradigmas de Programação

### 1. Imperativo
- Computação descrita como ações e comandos que alteram o estado do programa.
- Exemplos: **C**, Assembly.

### 2. Lógico
- Baseado em lógica matemática.
- Exemplos: **Prolog**.
- Exemplo de consulta:
  ```prolog
  gosta(maria, flores).
  gosta(maria, pedro).
  gosta(paulo, maria).

  ?- gosta(maria, X).
  % Resposta: X = flores

### 3. Funcional
- Computação como avaliação de funções matemáticas.
- Exemplos: Scheme, R.
- Exemplo:
((lambda (x) (+ x x)) (* 3 4))
; Resultado: 24

### 4. Orientado a Objetos
- Estruturação em objetos que representam entidades do mundo real.
- Conceitos: Herança, Polimorfismo, Encapsulamento, Abstração.
- Exemplo em Python:

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense

class MyModel(Model):
    def __init__(self, hidden_units, outputs, **kwargs):
        super(MyModel, self).__init__(**kwargs)
        self.dense = Dense(hidden_units, activation='sigmoid')
        self.linear = LinearMap(hidden_units, outputs)

    def call(self, inputs):
        h = self.dense(inputs)
        return self.linear(h)

my_model = MyModel(64, 12, name='my_custom_model')

### 5. Multi-paradigma
- Combina diferentes paradigmas em uma mesma linguagem ou ambiente.
- Exemplo: Scilab.

🚀 Exemplos práticos
- Implementação de modelos customizados em TensorFlow/Keras.
- Uso de Prolog para consultas lógicas.
- Scripts em Scheme e R para programação funcional.
- Simulações numéricas em Scilab.

📂 Estrutura do Repositório

├── src/
│   ├── python/        # Exemplos em Python
│   ├── r/             # Scripts em R
│   ├── scilab/        # Exemplos em Scilab
│   └── prolog/        # Exemplos em Prolog
├── docs/              # Documentação teórica
└── README.md          # Este arquivo

🧑‍🏫 Autor
Prof. Dr. Diego Bruno
- Education Tech Lead na DIO
- Doutor em Robótica e Machine Learning pelo ICMC-USP

📌 Objetivo
Este repositório tem como objetivo apresentar e comparar diferentes paradigmas e linguagens de programação aplicados ao Machine Learning, oferecendo exemplos práticos e teóricos para estudantes e profissionais da área

