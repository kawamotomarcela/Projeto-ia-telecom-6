# Estratégia de Organização dos Dados e Uso do Banco de Dados no Projeto de Predição de Tempo de Resolução de Ordens de Serviço

## 1. Introdução

Este projeto tem como objetivo prever o tempo necessário para a resolução de Ordens de Serviço por meio de um modelo de *Machine Learning* integrado a uma aplicação web desenvolvida em Django.

Durante o desenvolvimento, verificou-se que o sistema depende de dois grupos principais de informação:

- **dados usados no treinamento do modelo**
- **dados auxiliares usados para melhorar a interface**

Além disso, foi adicionado um **banco de dados local** para armazenar o **histórico das previsões realizadas**, tornando o sistema mais completo e permitindo consultas posteriores.

Assim, foi necessário definir uma estratégia que permitisse:

- organizar corretamente os datasets
- executar o sistema localmente
- apresentar o projeto em outras máquinas
- utilizar o banco de dados de forma simples e funcional

---

## 2. Datasets identificados no projeto

Com base nos arquivos analisados, o projeto possui os seguintes datasets:

- `export_tipos_atendimento.csv`
- `export_solucoes.csv`
- `export_resumo_produto.csv`
- `export_produtos.csv`
- `export_pecas_por_os.csv`
- `export_os_sem_pecas.csv`
- `export_os_defeito_solucao.csv`
- `export_os_base.csv`
- `export_diagnosticos.csv`
- `export_defeitos_reclamados.csv`
- `export_defeitos_os.csv`
- `export_defeitos_constatados.csv`

Esses arquivos não possuem a mesma função dentro da solução. Alguns são necessários para o treinamento do modelo, enquanto outros servem principalmente para deixar a interface mais compreensível ao usuário.

---

## 3. Classificação recomendada dos datasets

Para manter o projeto bem organizado, a divisão mais adequada é em três grupos.

### 3.1 Datasets principais

São os arquivos utilizados diretamente no pipeline de *Machine Learning*:

- `export_os_defeito_solucao.csv`
- `export_produtos.csv`

Esses arquivos concentram as informações mais importantes da Ordem de Serviço, como:

- data de abertura
- data de fechamento
- tipo de atendimento
- produto
- defeitos
- solução
- tempo de resolução

### 3.2 Datasets auxiliares da interface

São os arquivos usados para substituir IDs numéricos por descrições legíveis:

- `export_tipos_atendimento.csv`
- `export_solucoes.csv`
- `export_defeitos_reclamados.csv`
- `export_defeitos_constatados.csv`

Esses arquivos não precisam participar diretamente do treinamento do modelo, mas são fundamentais para tornar a interface mais intuitiva.

### 3.3 Datasets de apoio analítico

São arquivos que podem ser aproveitados futuramente para enriquecer o modelo ou ampliar análises:

- `export_pecas_por_os.csv`
- `export_os_sem_pecas.csv`
- `export_os_base.csv`
- `export_diagnosticos.csv`
- `export_defeitos_os.csv`
- `export_resumo_produto.csv`

Esses dados podem contribuir para uma evolução futura do projeto, caso se queira criar novas variáveis ou análises complementares.

---

## 4. Problema inicial do sistema

Na versão inicial, o sistema exigia que o usuário preenchesse vários campos usando apenas IDs numéricos, como:

- `tipo_atendimento_id`
- `produto_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`

Embora isso funcione tecnicamente para o modelo, não é adequado para o usuário final, pois números isolados não comunicam significado.

Isso causava três problemas principais:

- preenchimento pouco intuitivo
- maior chance de erro
- pior experiência de uso

---

## 5. Por que API não foi adotada como solução principal

Uma possibilidade considerada foi utilizar uma API para buscar, em tempo real, as descrições associadas aos IDs.

Essa solução poderia funcionar, mas não foi adotada como solução principal porque:

- aumentaria a complexidade sem necessidade
- criaria dependência de internet e de serviço externo
- dificultaria a execução local em apresentações
- não traria ganho proporcional, já que os dados já existem em arquivos locais

Dessa forma, embora o uso de API possa ser válido em sistemas maiores, ele não representa a melhor escolha para a versão atual deste projeto.

---

## 6. Solução adotada

A solução adotada foi organizar os dados por função e utilizá-los localmente no projeto.

Na prática, isso significa:

1. manter os datasets principais para o pipeline de *Machine Learning*
2. utilizar os datasets auxiliares apenas para melhorar a interface
3. gerar localmente o dataset tratado
4. treinar o modelo e salvar seus artefatos
5. usar banco de dados local para guardar o histórico das previsões

Essa abordagem foi escolhida porque equilibra:

- simplicidade
- clareza
- portabilidade
- estabilidade
- facilidade de apresentação

---

### 7. No ambiente local do desenvolvedor

Os arquivos ficam organizados dentro da estrutura do projeto e são utilizados diretamente pelo sistema.

### 7.1 Para quem clonar o projeto pelo GitHub

É importante observar que:

- os **datasets principais** foram enviados com **Git LFS**
- os arquivos de **`DatasetInfo` não foram incluídos no repositório**
- portanto, quem clonar o projeto precisará **baixar os arquivos auxiliares do `DatasetInfo` manualmente**

Ou seja:

- os arquivos principais podem ser obtidos normalmente pelo repositório, desde que o usuário tenha suporte ao **Git LFS**
- os arquivos auxiliares da interface precisam ser baixados e colocados manualmente na pasta correta

### 7.2 Consequência prática

Se a pessoa baixar o projeto sem os arquivos de `DatasetInfo`, o sistema poderá abrir, mas alguns campos da interface não funcionarão corretamente, pois dependem dessas descrições auxiliares.

---

## 8. Estrutura recomendada

A organização recomendada do projeto é a seguinte:

```text
projeto/
├── Dataset/
│   ├── export_os_defeito_solucao.csv
│   ├── export_produtos.csv
│   ├── DatasetInfo/
│   │   ├── export_tipos_atendimento.csv
│   │   ├── export_solucoes.csv
│   │   ├── export_defeitos_reclamados.csv
│   │   ├── export_defeitos_constatados.csv
│   │   └── export_resumo_produto.csv
│   └── processed/
│       └── dados_tratados.csv
├── models/
│   ├── modelo_tempo_os.pkl
│   └── colunas_modelo.pkl
├── previsao/
├── src/
├── templates/
├── static/
├── db.sqlite3
├── requirements.txt
├── README.md
└── manage.py
```

Essa estrutura deixa claro:

- quais arquivos são base do treinamento
- quais arquivos servem para a interface
- quais arquivos são gerados pelo preprocessamento
- onde ficam os artefatos do modelo
- onde fica o banco de dados

## 9. Uso do banco de dados no projeto

Além da organização dos datasets, o projeto também passou a utilizar banco de dados.

Atualmente, o banco não substitui os arquivos CSV nem o modelo treinado. Sua função é complementar o sistema, armazenando o histórico das previsões realizadas.

Ou seja:

- os datasets continuam sendo a base do treinamento
- o modelo continua sendo salvo em arquivo
- o banco é usado para registrar o uso do sistema

## 10. Qual banco de dados está sendo usado

O projeto utiliza o banco de dados padrão do Django com SQLite.

Isso significa que os dados ficam armazenados localmente no arquivo:
```
db.sqlite3
```
Essa escolha é adequada porque:

- é simples de configurar
- funciona bem localmente
- não exige servidor externo
- é suficiente para desenvolvimento, testes e apresentação

## 11. O que está sendo salvo no banco e como consultar

Atualmente, o banco de dados é utilizado principalmente para:

- guardar o histórico das previsões realizadas
- armazenar os dados internos do Django, como autenticação e sessões
- permitir consulta administrativa pelo Django Admin

Assim, sempre que uma previsão é realizada com sucesso, seus principais dados podem ser armazenados para consulta futura.

## 11.1 Superusuário no Django Admin

A forma mais simples de consultar o banco para testes é criar um superusuário e acessar o painel administrativo do Django.

O superusuário permite acessar:

/admin

## 11.2 Shell do Django

Também é possível verificar o banco pelo terminal, usando o shell do Django:
```
python manage.py shell

Exemplo de verificação:

from django.db import connection
from previsao.models import HistoricoPrevisao
from django.contrib.auth.models import User

cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas:", cursor.fetchall())

print("Quantidade no histórico:", HistoricoPrevisao.objects.count())
print("Histórico:", list(HistoricoPrevisao.objects.all()[:5]))
print("Usuários:", list(User.objects.values("id", "username", "email", "is_superuser")))
``` 
## 11.3 Evolução futura

No futuro, o sistema também pode ganhar uma tela própria para exibir o histórico das previsões dentro da própria aplicação, sem depender do admin.

## 12. Conclusão

A solução adotada no projeto combina organização de dados, simplicidade de execução e possibilidade de evolução futura.

Em resumo:

- os datasets principais continuam sendo usados no treinamento do modelo
- os datasets auxiliares melhoram a interface
- a solução local segue a mesma lógica da solução distribuída, mudando apenas a forma de obtenção dos arquivos
quem clonar o projeto pelo GitHub precisará baixar os arquivos de DatasetInfo, enquanto os principais foram disponibilizados com Git LFS
- o sistema roda localmente, sem depender de API externa
- o Google Drive pode ser usado apenas como apoio para disponibilizar arquivos auxiliares
- o banco de dados foi incorporado de forma simples para armazenar o histórico das previsões


## 📌 Observações

Atualmente, o projeto já utiliza a pasta DatasetInfo para melhorar a interface, permitindo que o usuário selecione descrições legíveis em vez de preencher apenas IDs numéricos.

Como possibilidades futuras, o projeto pode evoluir com:

- uso de API, caso seja necessário centralizar os dados auxiliares em um único serviço
- uso de Sass/SCSS, caso a interface cresça e seja necessário organizar melhor os estilos
- busca inteligente para produto
- pipeline automático de treino
- melhorias de UX e validação do modelo
