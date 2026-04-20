# Estratégia de Organização dos Dados, Modelagem e Uso do Banco de Dados no Projeto de Predição de Tempo de Resolução de Ordens de Serviço

## 1. Introdução

Este projeto tem como objetivo prever o tempo necessário para a resolução de Ordens de Serviço por meio de um modelo de *Machine Learning* integrado a uma aplicação web desenvolvida em Django.

Durante o desenvolvimento, verificou-se que o sistema depende de três frentes principais:

- **dados usados no treinamento do modelo**
- **dados auxiliares usados para melhorar a interface**
- **banco de dados local para armazenar o histórico das previsões**

Além disso, o projeto também passou a incluir uma etapa de **testes comparativos entre modelos de regressão**, permitindo avaliar alternativas antes de definir qual modelo seria utilizado como principal no sistema.

## 2. Organização dos datasets

Os arquivos utilizados no projeto podem ser divididos em três grupos.

### 2.1 Datasets principais

São os arquivos utilizados diretamente no pipeline principal de *Machine Learning*:

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

### 2.2 Datasets auxiliares da interface

São os arquivos usados para substituir IDs numéricos por descrições legíveis no formulário:

- `export_tipos_atendimento.csv`
- `export_solucoes.csv`
- `export_defeitos_reclamados.csv`
- `export_defeitos_constatados.csv`

Esses arquivos não são a base principal do treinamento, mas tornam a aplicação mais compreensível e intuitiva para o usuário.

### 2.3 Datasets de apoio analítico

São arquivos que podem ser utilizados futuramente para enriquecer o modelo ou ampliar análises:

- `export_pecas_por_os.csv`
- `export_os_sem_pecas.csv`
- `export_os_base.csv`
- `export_diagnosticos.csv`
- `export_defeitos_os.csv`
- `export_resumo_produto.csv`

---

## 3. Problema inicial do sistema

Na versão inicial, o sistema exigia que o usuário preenchesse vários campos usando apenas IDs numéricos, como:

- `tipo_atendimento_id`
- `produto_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`

Embora isso funcionasse tecnicamente para o modelo, não era adequado para o usuário final, pois números isolados não comunicam significado.

Isso causava problemas como:

- preenchimento pouco intuitivo
- maior chance de erro
- pior experiência de uso
- dificuldade de apresentação do sistema

---

## 4. Obtenção dos arquivos no ambiente local

Atualmente, o projeto não depende de o usuário organizar manualmente todos os arquivos antes de começar.

A obtenção dos dados funciona por meio do script:

```bash
python src/data/download_data.py
```
Esse script acessa a pasta disponibilizada no Google Drive e baixa automaticamente os arquivos necessários, organizando-os na estrutura esperada pelo sistema.

## 5. Modelo principal e testes comparativos

O projeto foi estruturado com duas frentes de modelagem.

## 5.1 Modelo principal

O modelo principal é aquele utilizado pela aplicação web para gerar previsões ao usuário.

Ele é treinado por meio do arquivo:
```bash
python src/train.py
```
Esse modelo é o modelo oficial do sistema, ou seja, é o que alimenta o Django e gera os arquivos utilizados pela previsão.

Arquivos gerados:
```
models/modelo_tempo_os.pkl
models/colunas_modelo.pkl
```
## 5.2 Testes comparativos

Além do modelo principal, o projeto também possui uma etapa de experimentos com diferentes modelos de regressão, com o objetivo de comparar desempenho e justificar tecnicamente a escolha do modelo final.

Esses testes são executados por meio do arquivo:

```bash
python src/train_experimentos.py
```

Os modelos avaliados são:

- Random Forest
- XGBoost
- NN (Rede Neural com MLPRegressor)

Os resultados dos testes são salvos em:
```
models/resultados_experimentos.json
```
## 5.3 Finalidade dos experimentos

Os experimentos não substituem automaticamente o modelo principal do sistema.
Sua função é:

- comparar abordagens diferentes
- medir desempenho com a mesma base
- justificar a escolha do modelo oficial
- registrar tentativas de melhoria

Essa separação foi adotada para garantir que o sistema continue estável, mesmo enquanto outros modelos são testados.

## 6. Estrutura recomendada do projeto
```
projeto/
├── Dataset/
│   ├── export_os_defeito_solucao.csv
│   ├── export_produtos.csv
│   ├── DatasetInfo/
│   │   ├── export_tipos_atendimento.csv
│   │   ├── export_solucoes.csv
│   │   ├── export_defeitos_reclamados.csv
│   │   └── export_defeitos_constatados.csv
│   └── processed/
│       └── dados_tratados.csv
├── models/
│   ├── modelo_tempo_os.pkl
│   ├── colunas_modelo.pkl
│   ├── resultados_experimentos.json
│   └── modelo_randomforest_teste.pkl
├── previsao/
├── src/
│   ├── data/
│   │   ├── download_data.py
│   │   └── preprocess.py
│   ├── train.py
│   ├── train_experimentos.py
│   └── predict.py
├── templates/
├── static/
├── db.sqlite3
├── requirements.txt
├── README.md
└── manage.py
``` 

## 7. 🗄️ Banco de Dados

O projeto utiliza banco de dados SQLite por meio do Django.

O arquivo do banco é:
```
db.sqlite3
```
Atualmente, o banco é utilizado principalmente para:

- armazenar o histórico das previsões realizadas
- manter os dados internos do Django, como autenticação e sessões
- permitir consulta administrativa pelo Django Admin

## 🔐 Acesso ao Admin do Django

Caso queira visualizar o histórico salvo no banco, crie um superusuário com:

```bash
python manage.py createsuperuser
```

Sugestão para testes
```
Usuário: administrator

Email: admin@teste.com

Senha: Superuser123!
```

Depois, com o servidor rodando, acesse:
```
http://127.0.0.1:8000/admin
```

### 9.2 Shell do Django

Também é possível verificar o banco pelo terminal, usando o shell do Django:
```
python manage.py shell
```
Exemplo de verificação:
```
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