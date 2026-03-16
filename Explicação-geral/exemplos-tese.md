# Exemplos de Dados para Teste do Sistema

Este arquivo contém exemplos reais de dados que podem ser utilizados para testar o sistema de **Predição de Tempo de Resolução de Ordens de Serviço**.

Os valores foram escolhidos com base nos datasets utilizados no projeto:

- `export_os_defeito_solucao.csv`
- `export_produtos.csv`

⚠️ Importante:
- O campo **produto_id** precisa existir em `export_produtos.csv`
- Os demais campos podem aceitar `0` quando não houver informação.

---

# Exemplo 1

Tipo de Atendimento (ID)

252

Produto (ID)

414898

Defeito Reclamado (ID)

0

Defeito Constatado (ID)

26826

Solução (ID)

0

Data de Abertura

2022-01-01

---

# Exemplo 2

Tipo de Atendimento (ID)

252

Produto (ID)

414204

Defeito Reclamado (ID)

0

Defeito Constatado (ID)

28640

Solução (ID)

0

Data de Abertura

2022-01-01

---

# Exemplo 3

Tipo de Atendimento (ID)

252

Produto (ID)

415179

Defeito Reclamado (ID)

0

Defeito Constatado (ID)

28640

Solução (ID)

0

Data de Abertura

2022-01-01

---

# Exemplo 4

Tipo de Atendimento (ID)

252

Produto (ID)

414833

Defeito Reclamado (ID)

0

Defeito Constatado (ID)

26842

Solução (ID)

0

Data de Abertura

2022-01-02

---

# Exemplo 5

Tipo de Atendimento (ID)

252

Produto (ID)

414698

Defeito Reclamado (ID)

0

Defeito Constatado (ID)

41384

Solução (ID)

0

Data de Abertura

2022-01-02

---

# Valores comuns encontrados no dataset

Alguns valores reais encontrados no dataset:

## tipo_atendimento_id

- 252
- 272
- 273
- 277

## defeito_constatado_id (exemplos)

- 26826
- 28640
- 26842
- 41384

## Observação

O dataset analisado apresenta muitos valores ausentes para:

- `defeito_reclamado_id`
- `solucao_id`

Por isso, durante os testes do sistema, é possível utilizar `0` nesses campos.