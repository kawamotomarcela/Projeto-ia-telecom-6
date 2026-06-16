```bash
## Modelos Testados

Para prever a variável `tempo_resolucao_horas`, foram realizados experimentos com três modelos de regressão:

- **RandomForestRegressor**
- **XGBoostRegressor**
- **MLPRegressor** — rede neural artificial

O objetivo dos testes foi comparar o desempenho dos modelos utilizando as mesmas 12 features e identificar qual abordagem apresentou melhor capacidade de previsão para o tempo de resolução das ordens de serviço.

---

## Modelo Escolhido

O modelo escolhido foi o **RandomForestRegressor**, pois apresentou o melhor desempenho geral entre os modelos testados.

Ele foi selecionado porque obteve:

- menor erro médio nas previsões
- menor erro considerando grandes desvios
- maior capacidade de explicar a variação dos dados

Por isso, o RandomForest foi considerado o modelo mais adequado para ser utilizado como modelo oficial do projeto.

---

## Resultados dos Experimentos

| Modelo | MAE | RMSE | R² |
|---|---:|---:|---:|
| **RandomForest** | 93.3418 | 290.9576 | 0.4951 |
| **XGBoost** | 110.6385 | 334.3904 | 0.3331 |
| **MLPRegressor** | 124.1440 | 390.0251 | 0.0927 |

---

## Features Utilizadas

O modelo foi treinado utilizando **12 features**, ou seja, 12 variáveis de entrada usadas para prever o tempo de resolução da ordem de serviço.

As features utilizadas foram:

1. `tipo_atendimento_id`
2. `produto_id`
3. `defeito_reclamado_id`
4. `defeito_constatado_id`
5. `solucao_id`
6. `fabrica_id`
7. `linha_id`
8. `familia_id`
9. `ano_abertura`
10. `mes_abertura`
11. `dia_abertura`
12. `dia_semana_abertura`

Essas variáveis representam informações sobre o tipo de atendimento, o produto relacionado à ordem de serviço, os defeitos informados e constatados, a solução aplicada e dados referentes à data de abertura da OS.

---

## Interpretação das Features

As features podem ser divididas em três grupos principais:

### Informações da Ordem de Serviço

- `tipo_atendimento_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`

Essas variáveis ajudam o modelo a entender o tipo de problema registrado, o defeito informado pelo cliente, o defeito identificado tecnicamente e a solução aplicada.

---

### Informações do Produto

- `produto_id`
- `fabrica_id`
- `linha_id`
- `familia_id`

Essas variáveis indicam características relacionadas ao produto envolvido na ordem de serviço. Produtos, linhas ou famílias diferentes podem apresentar níveis distintos de complexidade e, consequentemente, tempos diferentes de resolução.

---

### Informações Temporais

- `ano_abertura`
- `mes_abertura`
- `dia_abertura`
- `dia_semana_abertura`

Essas variáveis permitem que o modelo identifique padrões relacionados ao momento de abertura da OS, como sazonalidade, períodos com maior demanda e diferenças entre dias úteis e finais de semana.

---

## Quantidade de Amostras

Os experimentos foram realizados com **1.243.232 amostras**.

Essa quantidade representa o número de registros tratados utilizados no processo de treinamento e avaliação dos modelos.

Ter um grande volume de amostras é positivo, pois permite que o modelo aprenda padrões a partir de muitos exemplos históricos. Porém, a quantidade de dados sozinha não garante uma previsão perfeita.

O desempenho também depende da qualidade e da capacidade explicativa das features disponíveis.

---

## O que Significa Cada Modelo

### RandomForestRegressor

O **RandomForestRegressor** é um modelo baseado em várias árvores de decisão.

Ele cria diversas árvores e combina os resultados para gerar uma previsão mais estável. Esse tipo de modelo costuma apresentar bom desempenho em dados tabulares, como é o caso deste projeto.

No experimento, foi o modelo que apresentou o melhor resultado geral, com menor MAE, menor RMSE e maior R².

---

### XGBoostRegressor

O **XGBoostRegressor** também é um modelo baseado em árvores de decisão, mas utiliza uma técnica chamada boosting.

Nesse processo, o modelo tenta corrigir os erros cometidos nas etapas anteriores, buscando melhorar progressivamente a previsão.

Apesar de ser um modelo bastante poderoso, neste projeto ele ficou abaixo do RandomForest, apresentando maior erro e menor capacidade de explicação dos dados.

---

### MLPRegressor

O **MLPRegressor** é uma rede neural artificial utilizada para problemas de regressão.

Ele foi testado para comparação com os modelos baseados em árvores. Porém, neste caso, apresentou o pior desempenho entre os três modelos avaliados.

Isso pode ter ocorrido porque o dataset é tabular, possui variáveis representadas por IDs e apresenta grande variação no tempo de resolução das ordens de serviço.

---

## O que Significa Cada Métrica

### MAE

O **MAE** representa o erro médio absoluto das previsões.

Ele mostra, em média, quantas horas o modelo errou ao prever o tempo de resolução.

**Quanto menor o MAE, melhor.**

No RandomForest, o MAE foi de **93.3418 horas**, indicando que o modelo errou, em média, cerca de 93 horas nas previsões.

---

### RMSE

O **RMSE** também mede o erro das previsões, mas penaliza mais os erros muito grandes.

Quando o RMSE é muito maior que o MAE, isso indica que existem casos em que o modelo errou bastante, provavelmente por causa de ordens de serviço com tempos muito fora do padrão.

**Quanto menor o RMSE, melhor.**

No RandomForest, o RMSE foi de **290.9576 horas**, indicando a presença de casos extremos no dataset.

---

### R²

O **R²** indica quanto da variação do tempo de resolução o modelo conseguiu explicar.

**Quanto maior o R², melhor.**

No RandomForest, o R² foi de **0.4951**, o que significa que o modelo conseguiu explicar aproximadamente **49,51% da variação** do tempo de resolução das ordens de serviço.

Esse resultado mostra que o modelo conseguiu aprender padrões relevantes, mas ainda existem fatores que influenciam o tempo de resolução e que não estão presentes no dataset.

---

## Análise dos Resultados

O **RandomForestRegressor** apresentou o melhor desempenho geral entre os modelos testados.

Ele obteve o menor MAE, o menor RMSE e o maior R², demonstrando maior capacidade de prever o tempo de resolução em comparação aos demais modelos.

O **XGBoostRegressor** teve desempenho intermediário. Embora tenha conseguido aprender parte dos padrões dos dados, apresentou erros maiores e menor R² em relação ao RandomForest.

O **MLPRegressor**, por sua vez, apresentou o pior resultado, indicando que a rede neural não conseguiu capturar bem os padrões desse problema com as features disponíveis.

---

## Limitações do Modelo

Apesar do bom desempenho relativo do RandomForest, o modelo ainda apresenta limitações.

O tempo de resolução de uma ordem de serviço pode depender de fatores operacionais que não estão presentes no dataset, como:

- disponibilidade de técnicos
- fila de atendimento
- localização do cliente
- prioridade real da OS
- necessidade de peças
- reagendamentos
- quantidade de visitas
- tempo até o primeiro atendimento
- feriados e finais de semana
- pendências administrativas

Por isso, o modelo não deve ser interpretado como uma previsão exata, mas sim como uma ferramenta de apoio para estimar tendências com base nos dados disponíveis.

---

## Conclusão

O **RandomForestRegressor** foi escolhido como modelo oficial por apresentar o melhor equilíbrio entre desempenho, estabilidade e capacidade de explicação dos dados.

Os resultados indicam que o modelo conseguiu capturar parte relevante dos padrões presentes no dataset, explicando aproximadamente 49,51% da variação do tempo de resolução.

No entanto, os erros ainda são consideráveis, principalmente em casos extremos. Isso ocorre porque o dataset não contém todas as variáveis operacionais que influenciam diretamente o tempo real de resolução de uma ordem de serviço.

Dessa forma, o modelo é considerado uma primeira versão promissora, útil como apoio à análise e estimativa do tempo de resolução, mas ainda com possibilidade de melhoria a partir da inclusão de novas variáveis e maior tratamento dos dados.
```

