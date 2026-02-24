# 📊 PROPOSTA 6 - Predição de Tempo de Resolução
**Status:** Em desenvolvimento ⚠️👍  

#### **Instituição:** Unimar | Universidade de Marília  
#### **Curso:** Inteligencia Artificial 
#### **Termo:** 3° A

## 👥 Nomes - Grupo:
- Nathan Gabriel da Silva RA: 2078558 
- Marcela Kawamoto Fernandes RA: 2224453 
- Kenji Yuri Mitsuka de Paula, RA: 2033472 
- Julia Soares de Azevedo Lombardi RA: 2032874 
- Tainá De Souza Alves RA: 2041631 
- Matheus Bargas Rodrigues Flausino RA: 2057008 
- Lucia Maria Reis Braga RA: 2035292 

---


## 🎯 Objetivo

Desenvolver um modelo de **Machine Learning** capaz de prever o tempo necessário para finalizar uma Ordem de Serviço (OS), utilizando dados históricos.

A proposta busca:

- Melhorar o planejamento operacional  
- Reduzir atrasos  
- Aumentar a eficiência na alocação de recursos  
- Estimar prazos com maior precisão  

---

## 📌 Definição do Problema

O problema é classificado como **Regressão**, pois o objetivo é prever um valor numérico contínuo:

> ⏱️ Tempo total de resolução da OS (em horas ou dias)

---

## 🗂️ Dados Utilizados

### 🔹 Variáveis de Entrada (Features)

- Tipo da OS  
- Categoria do problema  
- Prioridade  
- Data de abertura  
- Técnico responsável  
- Setor solicitante  
- Histórico de tempo médio por categoria  
- Status anteriores da OS  

### 🔹 Variável Alvo (Target)

- Tempo total de resolução  

---

## 🤖 Modelos Avaliados

Serão comparados diferentes modelos de regressão:

- Random Forest Regressor  
- XGBoost Regressor  
- Rede Neural (MLP Regressor)  

O modelo com melhor desempenho e capacidade de generalização será selecionado.

---

## 📏 Métricas de Avaliação

Para medir a performance dos modelos, serão utilizadas:

- **MAE (Mean Absolute Error)**  
  → Mede o erro médio absoluto das previsões  

- **RMSE (Root Mean Squared Error)**  
  → Penaliza erros maiores  

- **R² (Coeficiente de Determinação)**  
  → Indica o quanto o modelo explica a variabilidade dos dados  

---

## 🔄 Etapas do Projeto

1. Coleta e limpeza dos dados  
2. Análise Exploratória (EDA)  
3. Feature Engineering  
4. Divisão em treino e teste  
5. Treinamento dos modelos  
6. Avaliação comparativa  
7. Ajuste de hiperparâmetros  
8. Seleção do melhor modelo  

---

## 🚀 Possíveis Melhorias Futuras

- Deploy do modelo via API  
- Atualização automática com novos dados  
- Dashboard com previsões em tempo real  
- Sistema de alerta para OS com risco de atraso  

---

## 🛠️ Tecnologias Utilizadas

- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- XGBoost  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## 📂 Estrutura do Projeto
```text
projeto-predicao-os/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_modelagem.ipynb
│
├── src/
│ ├── preprocessing.py
│ ├── train.py
│ ├── evaluate.py
│
├── models/
│
├── requirements.txt
└── README.md