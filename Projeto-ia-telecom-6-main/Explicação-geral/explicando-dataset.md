
# Problema Atual

No sistema atual, diversos campos da interface são preenchidos utilizando apenas **IDs numéricos**, por exemplo:

- `produto_id`
- `tipo_atendimento_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`

Exemplo no formulário atual:

Defeito Constatado (ID)
26826


Para o usuário final, esse valor **não possui significado claro**, pois o sistema não mostra a descrição associada ao ID.

Isso causa alguns problemas:

- Interface pouco intuitiva
- Maior chance de erro de preenchimento
- Necessidade de consultar o dataset manualmente

---

# Proposta de Solução

A proposta é criar uma pasta chamada:
DatasetInfo


Essa pasta conterá **datasets auxiliares que não foram utilizados no treinamento do modelo**, mas que possuem informações descritivas úteis.

Esses dados serão utilizados para:

- Melhorar a interface
- Traduzir IDs em descrições compreensíveis
- Criar listas de seleção (dropdown) no formulário

---

# Papel de Cada Dataset

## export_tipos_atendimento.csv

Contém a descrição dos tipos de atendimento.

Exemplo:


tipo_atendimento_id,descricao
252,Garantia
272,Manutenção corretiva
273,Manutenção preventiva
277,Visita técnica


Pode ser utilizado para mostrar no formulário:


Tipo de Atendimento

Garantia
Manutenção corretiva
Manutenção preventiva
Visita técnica


Internamente o sistema continuará enviando apenas o **ID correspondente**.

---

## export_solucoes.csv

Contém as soluções aplicadas nas ordens de serviço.

Exemplo:


solucao_id,descricao
1,Troca de componente
2,Atualização de software
3,Limpeza técnica


Pode ser utilizado para preencher o campo:


Solução Aplicada


---

## export_defeitos_reclamados.csv

Contém os defeitos relatados pelo cliente.

Exemplo:


defeito_reclamado_id,descricao
1001,Equipamento não liga
1002,Ruído excessivo
1003,Falha de funcionamento


---

## export_defeitos_constatados.csv

Contém os defeitos identificados durante o diagnóstico técnico.

Exemplo:


defeito_constatado_id,descricao
26826,Superaquecimento
28640,Falha elétrica
41384,Ruído anormal


Esse dataset é especialmente importante, pois os valores aparecem frequentemente no dataset principal.

---

## export_diagnosticos.csv

Contém informações adicionais sobre diagnósticos realizados nas ordens de serviço.

Pode ser utilizado para enriquecer análises futuras ou gerar relatórios.

---

## export_resumo_produto.csv

Contém informações resumidas dos produtos.

Pode ser utilizado para mostrar:

- Nome do produto
- Categoria
- Família
- Linha

Isso permitiria substituir o campo:


Produto (ID)


por algo mais intuitivo como:


Produto
Geladeira Frost Free 450L
Lavadora Automática 12kg
Ar-condicionado Split 12000BTU


---

# Integração com o Sistema

Os datasets da pasta `DatasetInfo` **não precisam ser utilizados no treinamento do modelo**.

Eles serão utilizados apenas para **melhorar a interface do usuário**.

Fluxo sugerido:


Usuário abre o formulário
↓

Django carrega os datasets da pasta DatasetInfo
↓

Campos do formulário são preenchidos com descrições
↓

Usuário seleciona a opção desejada
↓

Sistema envia o ID correspondente para o modelo
↓

Modelo realiza a previsão normalmente