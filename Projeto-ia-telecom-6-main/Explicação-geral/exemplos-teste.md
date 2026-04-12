# Exemplos de Dados para Teste do Sistema

Este arquivo apresenta **3 exemplos reais e simples** que podem ser utilizados para testar o sistema de **Predição de Tempo de Resolução de Ordens de Serviço**.

Os valores foram montados com base nos datasets do projeto:

- `export_os_defeito_solucao.csv`
- `export_produtos.csv`

---

## Como preencher o formulário

Atualmente, o sistema funciona da seguinte forma:

- **Tipo de Atendimento**: selecionar uma opção existente na lista
- **Produto (ID)**: informar manualmente um `produto_id` que exista em `export_produtos.csv`
- **Defeito Reclamado**: pode ficar vazio, caso não exista informação
- **Defeito Constatado**: selecionar uma opção existente na lista
- **Solução**: pode ficar vazia, caso não exista informação
- **Data de Abertura**: informar uma data válida

### Observação importante

Nos dados analisados, muitos registros possuem campos vazios para:

- defeito reclamado
- solução

Por isso, nos testes abaixo, esses campos podem ser deixados em branco sem problema.

---

# Exemplo 1

## Preenchimento

**Tipo de Atendimento**  
252

**Produto (ID)**  
414898

**Defeito Reclamado**  
Deixar vazio

**Defeito Constatado**  
26826 - Reator queimado

**Solução**  
Deixar vazio

**Data de Abertura**  
2022-01-01

## Explicação

Este é um dos testes mais simples para começar.  
Ele usa um `produto_id` real e um `defeito_constatado_id` real encontrado nos datasets.  
É uma boa opção para validar se o sistema está funcionando corretamente.

---

# Exemplo 2

## Preenchimento

**Tipo de Atendimento**  
252

**Produto (ID)**  
414204

**Defeito Reclamado**  
Deixar vazio

**Defeito Constatado**  
28640 - Controlador com defeito

**Solução**  
Deixar vazio

**Data de Abertura**  
2022-01-01

## Explicação

Este exemplo também utiliza uma combinação real encontrada na base.  
Ele é útil para testar outro produto e outro defeito constatado, sem alterar a estrutura básica do preenchimento.

---

# Exemplo 3

## Preenchimento

**Tipo de Atendimento**  
252

**Produto (ID)**  
414698

**Defeito Reclamado**  
Deixar vazio

**Defeito Constatado**  
41384 - Micromotor evaporador solto

**Solução**  
Deixar vazio

**Data de Abertura**  
2022-01-02

## Explicação

Este exemplo ajuda a testar o sistema com outra data de abertura e outro defeito constatado real.  
É interessante para verificar se o sistema continua funcionando bem com combinações diferentes de entrada.

---

# Resumo dos valores usados

## Tipo de Atendimento
- 252

## Produtos (ID)
- 414898
- 414204
- 414698

## Defeitos Constatados
- 26826 — Reator queimado
- 28640 — Controlador com defeito
- 41384 — Micromotor evaporador solto

---

# Recomendação de Teste

Se for seu primeiro teste, comece pelo **Exemplo 1**.  
Ele é o mais direto e serve bem para confirmar se:

- o formulário está aceitando os dados
- o produto existe na base
- o modelo está conseguindo gerar a previsão