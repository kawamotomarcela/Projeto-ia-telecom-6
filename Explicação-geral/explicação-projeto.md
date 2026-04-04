# Estratégia de Organização dos Dados e Uso do Banco de Dados no Projeto de Predição de Tempo de Resolução de Ordens de Serviço

## 1. Introdução

Este projeto tem como objetivo prever o tempo necessário para a resolução de Ordens de Serviço por meio de um modelo de *Machine Learning* integrado a uma aplicação web desenvolvida em Django.

Durante o desenvolvimento, observou-se que o sistema depende de dois tipos principais de informação:

- dados utilizados no treinamento do modelo
- dados auxiliares usados para melhorar a interface

Além disso, também surgiu a necessidade de registrar previsões realizadas pelo sistema, o que levou à utilização de um banco de dados para armazenamento do histórico.

Assim, foi necessário definir a melhor forma de organizar os datasets, executar o sistema em outras máquinas e utilizar o banco de dados de maneira simples, funcional e profissional.

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

Esses arquivos não possuem a mesma função dentro da solução. Alguns são necessários para o treinamento do modelo, enquanto outros servem principalmente para deixar a interface mais compreensível para o usuário.

---

## 3. Classificação recomendada dos datasets

Para manter o projeto bem organizado, a divisão mais adequada é em três grupos.

### 3.1 Dados principais do modelo

São os arquivos utilizados diretamente no treinamento e na predição:

- `export_os_base.csv`
- `export_os_defeito_solucao.csv`
- `export_produtos.csv`

Esses arquivos concentram as principais informações da Ordem de Serviço, como:

- data de abertura
- data de fechamento
- tipo de atendimento
- produto
- defeitos
- solução
- tempo de resolução

### 3.2 Dados auxiliares da interface

São os arquivos usados para substituir IDs numéricos por descrições legíveis:

- `export_tipos_atendimento.csv`
- `export_solucoes.csv`
- `export_defeitos_reclamados.csv`
- `export_defeitos_constatados.csv`
- `export_resumo_produto.csv`

Esses arquivos não precisam participar diretamente do treinamento do modelo, mas são importantes para tornar a interface mais intuitiva.

### 3.3 Dados de apoio analítico

São arquivos que podem ser aproveitados futuramente para enriquecer o modelo ou ampliar análises:

- `export_pecas_por_os.csv`
- `export_os_sem_pecas.csv`
- `export_diagnosticos.csv`
- `export_defeitos_os.csv`

---

## 4. Problema inicial do sistema

Na versão inicial, o sistema exigia que o usuário preenchesse vários campos usando apenas IDs numéricos, como:

- `tipo_atendimento_id`
- `produto_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`

Embora isso funcione tecnicamente para o modelo, não é adequado para o usuário final, pois números isolados não comunicam significado.

Isso gerava três problemas principais:

- preenchimento pouco intuitivo
- maior chance de erro
- pior experiência de uso

---

## 5. Por que API não foi escolhida como solução principal

Uma possibilidade considerada foi utilizar uma API para buscar, em tempo real, as descrições associadas aos IDs.

Essa solução poderia funcionar, mas não foi considerada a melhor para este projeto pelos seguintes motivos:

- aumentaria a complexidade sem necessidade
- criaria dependência de internet e de um serviço externo
- dificultaria a execução local em apresentações
- não traria ganho proporcional, já que os dados já existem em arquivos locais

Dessa forma, embora o uso de API seja válido em sistemas maiores, ele não é a melhor solução para o contexto atual do projeto.

---

## 6. Por que o Google Drive também não é a solução principal

Outra alternativa pensada foi deixar os datasets em uma pasta no Google Drive para que o usuário os baixasse antes de rodar o sistema.

Essa abordagem pode funcionar como apoio, mas não é a melhor solução principal porque:

- exige várias etapas manuais
- aumenta a chance de erro
- reduz a reprodutibilidade
- passa uma sensação de improviso
- não resolve a organização interna do projeto

Assim, o Google Drive pode ser usado como meio de distribuição dos arquivos, mas não como base da arquitetura do sistema.

---

## 7. Solução adotada para os datasets

A alternativa considerada mais correta foi organizar os datasets por função e usá-los de forma local no projeto.

Na prática, isso significa:

1. manter os datasets principais para o pipeline de *Machine Learning*
2. utilizar os datasets auxiliares apenas para melhorar a interface
3. deixar o modelo treinado pronto para uso
4. executar o sistema localmente, sem depender de API externa
5. usar o Google Drive apenas como apoio para disponibilização dos arquivos, quando necessário

Essa solução foi escolhida porque equilibra:

- simplicidade
- clareza
- portabilidade
- estabilidade
- facilidade de apresentação

---

## 8. Uso do banco de dados no projeto

Além da organização dos datasets, o projeto também passou a utilizar banco de dados.

No momento, o banco de dados não substitui os arquivos CSV nem o modelo treinado. Sua função principal é armazenar e consultar o histórico das previsões realizadas.

Ou seja:

- os datasets continuam sendo a base do treinamento
- o modelo continua sendo salvo em arquivo
- o banco passou a ser usado para registrar o uso do sistema

---

## 9. Qual banco de dados está sendo usado atualmente

Atualmente, o projeto utiliza o banco de dados padrão do Django com SQLite.

Isso significa que os dados ficam armazenados em um arquivo local chamado:

```text
db.sqlite3
``` 
Essa escolha é adequada para o projeto porque:

é simples de configurar
funciona bem localmente
não exige instalação de um servidor de banco
é suficiente para testes, desenvolvimento e apresentação

## 10. O que está sendo salvo no banco

Atualmente, o banco de dados é utilizado principalmente para:

guardar o histórico das previsões
armazenar os dados internos do Django, como autenticação e sessões
permitir consulta administrativa por meio do Django Admin

Assim, sempre que uma previsão é realizada com sucesso, os principais dados da entrada e o resultado previsto podem ser registrados no banco.

## 11. Quais são as opções de uso do banco de dados

Para facilitar o entendimento, o uso do banco pode ser pensado em níveis.

11.1 Sem banco de dados

O sistema poderia funcionar apenas com:

CSV
modelo treinado em .pkl
interface Django

Essa opção é suficiente para a previsão funcionar, mas não permite registrar histórico nem consultar previsões anteriores.

11.2 Banco apenas para histórico

Esta foi a opção adotada no projeto.

Nela, o banco é usado apenas para salvar:

- dados principais da previsão
- data da previsão
- resultado previsto

12. Superusuário: o que é e quando usar

Uma forma prática de consultar o banco no Django é criar um superusuário.

O superusuário permite acessar o painel administrativo do Django em:

/admin

Por meio desse painel, é possível:

- visualizar o histórico salvo
- consultar registros
- testar rapidamente o banco
- administrar dados sem criar uma tela nova

Portanto, criar um superusuário é uma ótima opção para testes e administração.

No entanto, ele não é a única forma de consultar o banco. Também é possível:
## Comandos para verificar o banco no shell do Django

### 1. Abrir o shell do Django

```bash
python manage.py shell
```

```bash
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
13. Estrutura recomendada

A organização recomendada do projeto é a seguinte:

```
projeto/
├── Dataset/
│   ├── raw/
│   │   ├── export_os_base.csv
│   │   ├── export_os_defeito_solucao.csv
│   │   ├── export_produtos.csv
│   │   ├── export_pecas_por_os.csv
│   │   ├── export_os_sem_pecas.csv
│   │   ├── export_diagnosticos.csv
│   │   └── export_defeitos_os.csv
│   ├── info/
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
# 14. Conclusão

A solução adotada no projeto combina organização de dados, simplicidade de execução e possibilidade de evolução futura.

Em resumo:

- os datasets principais continuam sendo usados no treinamento do modelo
- os datasets auxiliares melhoram a interface
- o sistema roda localmente, sem depender de API externa
- o Google Drive pode ser usado apenas para disponibilizar os arquivos
- o banco de dados foi incorporado de forma simples, inicialmente para armazenar o histórico das previsões

