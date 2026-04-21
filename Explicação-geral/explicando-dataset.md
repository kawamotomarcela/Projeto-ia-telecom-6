# Resumo dos dados usados no modelo

## Visão geral

O modelo foi treinado usando, principalmente, dados de **dois datasets**:

- `export_os_defeito_solucao.csv`
- `export_produtos.csv`

Depois disso, essas informações passaram por um tratamento e geraram o arquivo final:

- `dados_tratados.csv`

É esse arquivo tratado que entra no treinamento do modelo.

---

## O que cada dataset faz

### 1. `export_os_defeito_solucao.csv`
Esse é o dataset principal da ordem de serviço.

Dele saem informações como:

- `tipo_atendimento_id`
- `produto_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`
- `data_abertura`
- `tempo_resolucao_horas` → **essa é a variável que o modelo tenta prever**

### 2. `export_produtos.csv`
Esse dataset complementa o principal com dados do produto.

Ele é usado para trazer informações do item relacionado ao `produto_id`.

Ou seja: ele ajuda o modelo a entender **qual produto está envolvido na OS**.

### 3. `dados_tratados.csv`
Esse é o resultado final do pré-processamento.

Nele ficam somente os dados já prontos para o treinamento, como:

- IDs das variáveis principais
- informações derivadas da data de abertura
- variável alvo (`tempo_resolucao_horas`)

---

## Quais dados entram no modelo

De forma simples, o modelo usa:

- tipo de atendimento
- produto
- defeito reclamado
- defeito constatado
- solução
- informações extraídas da data de abertura

Esses dados ajudam o modelo a identificar padrões e estimar o tempo de resolução.

---

## Qual dado o modelo quer prever

O modelo tenta prever:

- `tempo_resolucao_horas`

Ou seja, ele recebe as características da ordem de serviço e estima quantas horas aquela OS pode levar para ser resolvida.

---

## Por que usar esses dados

Cada campo ajuda por um motivo:

- **tipo de atendimento** → mostra o contexto da OS
- **produto** → mostra qual equipamento está sendo atendido
- **defeito reclamado** → mostra o problema informado pelo cliente
- **defeito constatado** → mostra o problema real encontrado pelo técnico
- **solução** → mostra o tipo de ação tomada
- **data de abertura** → ajuda a capturar padrões de tempo relacionados ao dia, mês ou período

---

## O que fica só para a interface

Os arquivos da pasta `DatasetInfo` **não precisam participar do treinamento**.

Eles servem para deixar o sistema mais fácil de usar.

Exemplo:

em vez de mostrar:

- `26826`

o sistema pode mostrar:

- `Superaquecimento`

Isso melhora muito a experiência do usuário.

Esses arquivos servem para transformar IDs em nomes compreensíveis.

---

## Resumindo em uma frase

O modelo usa os **IDs e dados tratados** para fazer a previsão, enquanto os arquivos da pasta `DatasetInfo` servem para **traduzir esses IDs em descrições mais amigáveis na interface**.