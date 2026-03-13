# Requisitos Funcionais

| ID | Requisito | Descrição |
|----|-----------|-----------|
| RF01 | Importação de dados | O sistema deve permitir a importação da base histórica de Ordens de Serviço. |
| RF02 | Validação dos dados | O sistema deve verificar inconsistências ou erros nos dados importados. |
| RF03 | Pré-processamento dos dados | O sistema deve preparar os dados para uso nos modelos de Machine Learning. |
| RF04 | Transformação de variáveis | O sistema deve converter variáveis categóricas em formato numérico adequado para os algoritmos. |
| RF05 | Divisão dos dados | O sistema deve dividir a base de dados em conjuntos de treino e teste. |
| RF06 | Treinamento dos modelos | O sistema deve permitir o treinamento de modelos de regressão para prever o tempo de resolução. |
| RF07 | Avaliação do modelo | O sistema deve calcular métricas de avaliação para medir o desempenho dos modelos. |
| RF08 | Comparação de modelos | O sistema deve comparar diferentes algoritmos e selecionar o melhor modelo. |
| RF09 | Predição de tempo | O sistema deve permitir prever o tempo de resolução de uma nova Ordem de Serviço. |
| RF10 | Exibição dos resultados | O sistema deve apresentar ao usuário o tempo estimado de resolução. |
| RF11 | Atualização do modelo | O sistema deve permitir que o modelo seja re-treinado com novos dados históricos. |

---

# Requisitos Não Funcionais

| ID | Requisito | Descrição |
|----|-----------|-----------|
| RNF01 | Desempenho | O sistema deve gerar previsões em poucos segundos após a inserção dos dados. |
| RNF02 | Usabilidade | O sistema deve possuir uma interface simples e de fácil entendimento. |
| RNF03 | Confiabilidade | O sistema deve produzir resultados consistentes com base nos dados fornecidos. |
| RNF04 | Segurança | O sistema deve garantir proteção dos dados utilizados no treinamento e nas previsões. |
| RNF05 | Escalabilidade | O sistema deve suportar aumento no volume de dados sem perda significativa de desempenho. |
| RNF06 | Manutenibilidade | O sistema deve permitir atualização da base de dados e re-treinamento do modelo. |
| RNF07 | Disponibilidade | O sistema deve estar disponível para uso sempre que necessário. |
| RNF08 | Reprodutibilidade | O sistema deve permitir repetir os experimentos de treinamento com os mesmos resultados. |

---

# Casos de Uso

## Caso de Uso 1 – Importação de dados

**Ator principal:** Usuário do sistema  

**Descrição:**  
Permite que o usuário carregue a base histórica de Ordens de Serviço para que os dados possam ser utilizados no treinamento do modelo de Machine Learning.

**Fluxo principal:**

1. O usuário acessa o sistema.
2. O usuário seleciona o arquivo contendo a base de dados.
3. O sistema realiza a importação do arquivo.
4. O sistema valida a estrutura dos dados.
5. Os dados são armazenados para processamento.

---

## Caso de Uso 2 – Treinamento do modelo

**Ator principal:** Usuário do sistema  

**Descrição:**  
Permite que o sistema utilize os dados históricos para treinar modelos de Machine Learning capazes de prever o tempo de resolução das ordens de serviço.

**Fluxo principal:**

1. O usuário solicita o treinamento do modelo.
2. O sistema prepara os dados para análise.
3. O sistema divide os dados em treino e teste.
4. O sistema executa o treinamento dos modelos.
5. O sistema calcula as métricas de desempenho.
6. O sistema apresenta os resultados obtidos.

---

## Caso de Uso 3 – Predição do tempo de resolução

**Ator principal:** Usuário do sistema  

**Descrição:**  
Permite prever o tempo estimado para finalizar uma nova Ordem de Serviço utilizando o modelo treinado.

**Fluxo principal:**

1. O usuário acessa o sistema.
2. O usuário informa os dados da nova Ordem de Serviço.
3. O sistema envia os dados para o modelo de Machine Learning.
4. O modelo realiza o cálculo da previsão.
5. O sistema apresenta o tempo estimado de resolução.

---

## Caso de Uso 4 – Análise de desempenho do modelo

**Ator principal:** Usuário do sistema  

**Descrição:**  
Permite visualizar as métricas de avaliação do modelo treinado para analisar sua precisão.

**Fluxo principal:**

1. O usuário solicita a análise do modelo.
2. O sistema apresenta métricas como MAE, RMSE e R².
3. O usuário analisa o desempenho do modelo.

---

