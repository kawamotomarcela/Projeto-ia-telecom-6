# Exemplos de Dados para Teste do Sistema

Este arquivo apresenta **3 exemplos de teste mais completos** para o sistema de **Predição de Tempo de Resolução de Ordens de Serviço**.

Os exemplos abaixo utilizam valores já confirmados no projeto para:

- `tipo_atendimento_id`
- `produto_id`
- `defeito_constatado_id`

Nos campos de **defeito reclamado** e **solução**, a recomendação é selecionar uma opção **real disponível na própria lista do sistema**, para que o teste fique mais completo e sem depender de campos vazios.

---

## Como preencher o formulário

Atualmente, o sistema funciona da seguinte forma:

- **Tipo de Atendimento**: selecionar uma opção existente na lista
- **Produto (ID)**: informar manualmente um `produto_id` que exista em `export_produtos.csv`
- **Defeito Reclamado**: selecionar uma opção real da lista, quando desejar um teste mais completo
- **Defeito Constatado**: selecionar uma opção existente na lista
- **Solução**: selecionar uma opção real da lista, quando desejar um teste mais completo
- **Data de Abertura**: informar uma data válida

---

## Exemplo 1 — Teste simples e confiável

### Preenchimento

**Tipo de Atendimento**  
252

**Produto (ID)**  
414898

**Defeito Reclamado**  
Selecionar uma opção real da lista do sistema

**Defeito Constatado**  
26826 - Reator queimado

**Solução**  
Selecionar uma opção real da lista do sistema

**Data de Abertura**  
2022-01-01

### Objetivo do teste

Este é um teste inicial mais seguro, usando um produto confirmado e um defeito constatado confirmado.  
É indicado para validar se:

- o formulário aceita os dados
- o produto existe na base
- a previsão é gerada corretamente
- os campos opcionais também podem ser utilizados

---

## Exemplo 2 — Teste com outro produto e outro defeito

### Preenchimento

**Tipo de Atendimento**  
252

**Produto (ID)**  
414204

**Defeito Reclamado**  
Selecionar uma opção real da lista do sistema

**Defeito Constatado**  
28640 - Controlador com defeito

**Solução**  
Selecionar uma opção real da lista do sistema

**Data de Abertura**  
2022-01-01

### Objetivo do teste

Este exemplo ajuda a verificar se o sistema continua funcionando corretamente com outra combinação de produto e defeito.

É útil para testar:

- variação de produto
- variação de defeito constatado
- preenchimento mais completo do formulário

---

## Exemplo 3 — Teste com data diferente

### Preenchimento

**Tipo de Atendimento**  
252

**Produto (ID)**  
414698

**Defeito Reclamado**  
Selecionar uma opção real da lista do sistema

**Defeito Constatado**  
41384 - Micromotor evaporador solto

**Solução**  
Selecionar uma opção real da lista do sistema

**Data de Abertura**  
2022-01-02

### Objetivo do teste

Este exemplo é interessante para verificar o comportamento do sistema com:

- outro produto confirmado
- outro defeito confirmado
- outra data de abertura

Assim, ele ajuda a validar se a geração das features de data está funcionando corretamente.

---

## Valores confirmados usados nos testes

### Tipo de Atendimento
- 252

### Produtos (ID)
- 414898
- 414204
- 414698

### Defeitos Constatados
- 26826 — Reator queimado
- 28640 — Controlador com defeito
- 41384 — Micromotor evaporador solto

---

## Recomendação de uso

Para testes mais completos, o ideal é:

- manter os `produto_id` e `defeito_constatado_id` confirmados
- preencher também **defeito reclamado** e **solução** escolhendo valores reais da lista do sistema
- variar a data de abertura entre os exemplos

Se for o primeiro teste, comece pelo **Exemplo 1**.

Se quiser testar mais a interface, use o **Exemplo 2** e o **Exemplo 3** preenchendo todos os campos disponíveis.