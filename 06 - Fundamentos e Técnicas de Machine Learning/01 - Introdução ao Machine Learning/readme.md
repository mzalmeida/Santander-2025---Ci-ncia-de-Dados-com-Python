Introdução ao Machine Learning - Prof. Dr. Diego Bruno
📚 Visão Geral do Curso
Material completo de 90 páginas sobre fundamentos e aplicações práticas de Machine Learning, ministrado pelo Prof. Dr. Diego Bruno (Doutor em Robótica e ML pelo ICMC-USP, Tech Lead na DIO). Abrange desde conceitos básicos até projetos avançados em veículos autônomos e visão computacional.
​

📖 Sumário Executivo por Tópicos
1. Fundamentos de IA e ML
Máquinas que pensam como humanos através de treinamento com dados, sem regras fixas. Diferencia IA Geral (ficção) de IA Restrita (ML prático).
​

2. Teste de Turing e Robótica
Avaliação de inteligência artificial via imitação humana. Exemplo: Sophia (Hanson Robotics, 2015), primeiro robô com cidadania.
​

3. Relação ML × IA
ML treina IA restrita através de datasets. Objetivo: aprender padrões automaticamente de exemplos e observações.
​

4. Tipos de Aprendizado
Supervisionado: Classificação/regressão com rótulos

Não-supervisionado: Clusterização de padrões

Por reforço: Aprendizado por tentativa/erro
​

5. Neurônios Artificiais
Arquitetura básica: entradas (X₁...Xn) × pesos (W₁...Wₙ) → função de ativação → saída. Base das CNNs.
​

6. Projetos USP/ICMC - Veículos Autônomos
CARINA 1/2: Robótica móvel

Scania G360: ADAS industrial

Uber XC90: Sensores LIDAR + câmeras
​

7. Sensores em Veículos
LIDAR Velodyne HDL-32E, câmeras estéreo 3D, radar, acelerômetros, ultrassônicos. Fusão 2D/3D para percepção.
​

8. Armadilha de Insetos (CLRMD)
Fototransistores + laser detectam Aedes aegypti fêmea via batimento de asas. Distingue macho/fêmea.
​

9. Agricultura de Precisão
Carbon Robotics: Laser remove plantas daninhas. Visão computacional + ML em campo.
​

10. Red Bull Basement
Co-guia robótico V2 com visão computacional e controle de hardware.
​

11. Deep Learning - TensorFlow
CNNs extraem features automaticamente: Convolução → Pooling → Fully Connected → Classificação.
​

12. Bibliotecas Essenciais
TensorFlow: Deep Learning

scikit-learn: ML clássico

pandas: Manipulação de dados
​

13. Google Colab
Plataforma online para ML. Exemplo prático: detecção de pedestres/veículos em imagens.
​

14. Detecção de Placas/Semáforos
Slide Window + Deep Learning. 99.1% precisão STOP, 96.2% PREFERÊNCIA.
​

15. Arquitetura Veículo Autônomo
text
Percepção → Tomada Decisão → Controle
  ↓          ↓              ↓
2D/3D      Neuro-FSM      Trajetória
16. Neuro-FSM (Neuro-Finite State Machine)
Máquina de estados + RNA para decisões autônomas. Acelera/Mantém/Freia baseado em leis trânsito.
​

17. Resultados LARS 2017
Artigo: "Image classification system based on Deep Learning" (Diego Renan Bruno). Testes sequenciais: média 94% eficiência.
​

18. Visão 2D State-of-the-Art
YOLO Series: Detecção real-time
Mask R-CNN: Detecção + segmentação
DeepLab: Segmentação semântica
​

19. Fusão Sensorial 2D/3D
Câmera estéreo (RGB+profundidade) + LIDAR Velodyne → Inception V3 → classificação sinais verticais.
​

20. Problemas Visão 2D
Oclusões, ataques adversariais (stickers em placas), falhas em smartphones Face Unlock.
​

21. Ética em Sistemas Autônomos
Dilemas: "criança vs idoso?" Leis de Asimov insuficientes para cenários reais.
​

22. Revoluções Industriais
text
1ª (1784): Mecânica
2ª (1870): Elétrica
3ª (1969): PLC
4ª (2012): Ciber-física
23. Indústria 4.0
Robôs colaborativos, Big Data, sistemas ciber-físicos, ML em escala industrial.
​

24. Aplicações Médicas
Suporte diagnóstico, detecção de anomalias, análise de imagens clínicas.
​

25. Interfaces Cérebro-Máquina
Miguel Nicolelis: Controle de próteses via BMI. Reabilitação neurológica.
​

26. Transhumanismo
Avatares digitais, upload de consciência (2045 Initiative).
​

🛠️ Como Reproduzir Experimentos
bash
1. Google Colab → Novo Notebook
2. !pip install tensorflow
3. Carregar dataset sinais trânsito
4. Transfer Learning (Inception V3)
5. Treinar/testar modelo
📈 Resultados Experimentais Resumidos
Sinal	Precisão
STOP	99.1-99.6%
PREFERÊNCIA	96.2-97.6%
PEDESTRE	88.5-89.2%
Média Geral	94%
🔬 Publicações e Projetos
LARS/SBR 2017: Classificação sinais trânsito via Deep Learning

IEEE WCCI 2018: Fusão 2D/3D (Rio de Janeiro)

Laboratórios: CLRMD, LRM, LABIC (USP São Carlos)
​

👨‍🏫 Sobre o Professor
Diego Renan Bruno - ICMC-USP São Carlos
Contato: diegobruno@icmc.usp.br
​