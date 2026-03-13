# Objetivo da IA

A Inteligência Artificial terá como papel principal analisar dados históricos de Ordens de Serviço para prever o tempo necessário para sua resolução.

O modelo de Machine Learning será treinado com registros de atendimentos anteriores, identificando padrões que relacionam características da OS com o tempo que foi necessário para finalizá-la. A partir desses padrões, o sistema poderá estimar o tempo de resolução de novas ordens de serviço antes mesmo de sua conclusão.

**Entrada do modelo (features):**
- Tipo da Ordem de Serviço  
- Categoria do problema  
- Prioridade  
- Data de abertura  
- Técnico responsável  
- Setor solicitante  
- Histórico de tempo médio por categoria  
- Status anteriores da OS  

**Processamento:**
Os dados serão processados por modelos de regressão em Machine Learning, capazes de analisar variáveis numéricas e categóricas para encontrar relações entre os dados históricos e o tempo de resolução.

Os modelos avaliados serão:
- Random Forest Regressor  
- XGBoost Regressor  
- MLP Regressor (Rede Neural)

**Saída da IA:**

Estimativa do tempo total necessário para concluir uma Ordem de Serviço, representado em horas ou dias.

---