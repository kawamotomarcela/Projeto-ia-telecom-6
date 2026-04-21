# Modelos testados

Foram testados três modelos para prever `tempo_resolucao_horas`:

- **RandomForest**
- **XGBoost**
- **MLPRegressor (rede neural)**

## Modelo escolhido

O modelo escolhido foi o **RandomForest**, porque apresentou o melhor desempenho geral nos testes.

### Resultados
- **RandomForest:** MAE 93.3418 | RMSE 290.9576 | R² 0.4951
- **XGBoost:** MAE 110.6385 | RMSE 334.3904 | R² 0.3331
- **MLPRegressor:** MAE 124.1440 | RMSE 390.0251 | R² 0.0927

## O que significa cada modelo

### RandomForest
Modelo baseado em várias árvores de decisão.  
Foi o melhor porque errou menos e teve maior capacidade de explicar os dados.

### XGBoost
Modelo de boosting, também baseado em árvores.  
Teve resultado razoável, mas ficou abaixo do RandomForest.

### MLPRegressor
Rede neural artificial.  
Foi testada para comparação, mas teve o pior desempenho neste problema.

## O que significa cada métrica

### MAE
Mostra o erro médio das previsões.  
**Quanto menor, melhor.**

### RMSE
Também mede o erro, mas penaliza mais os erros muito grandes.  
**Quanto menor, melhor.**

### R²
Mostra o quanto o modelo consegue explicar os dados.  
**Quanto maior, melhor.**

## Conclusão

O **RandomForest** foi escolhido porque apresentou o melhor equilíbrio entre desempenho e confiabilidade, sendo o modelo que mais se aproximou dos valores reais nos experimentos.
