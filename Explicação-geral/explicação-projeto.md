# Documentação do Projeto — Predição de Tempo de Resolução de Ordens de Serviço

## Visão Geral

Este projeto tem como objetivo desenvolver um sistema capaz de **prever o tempo necessário para a resolução de uma Ordem de Serviço (OS)** utilizando técnicas de **Machine Learning**.

O sistema recebe informações básicas da OS e utiliza um modelo previamente treinado para estimar quantas horas serão necessárias para sua conclusão.

A aplicação é composta por duas partes principais:

- Pipeline de **Machine Learning**
- Interface Web desenvolvida com **Django**

---

# Dataset

A pasta `Dataset` contém os dados utilizados para treinamento do modelo.

## Arquivos principais

### export_os_defeito_solucao.csv

Contém informações relacionadas às ordens de serviço.

Principais colunas utilizadas no projeto:

- `produto_id`
- `tipo_atendimento_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`
- `data_abertura`
- `tempo_resolucao_horas`

Esses dados representam as características da OS e o **tempo real de resolução**, que é a variável alvo do modelo.

---

### export_produtos.csv

Contém características adicionais dos produtos atendidos.

Principais colunas:

- `produto_id`
- `fabrica_id`
- `linha_id`
- `familia_id`

Essas informações são utilizadas como **features adicionais no modelo de Machine Learning**.

Durante o processamento dos dados, essas informações são combinadas com os dados das ordens de serviço através da coluna `produto_id`.

---

# Pasta src

A pasta `src` contém os scripts responsáveis pelo **pipeline de Machine Learning**.

Esses scripts realizam todo o processo de preparação dos dados e treinamento do modelo.

---

## preprocess.py

Script responsável pelo **pré-processamento dos dados**.

Principais funções:

- Carregar os datasets originais
- Realizar o **merge entre as bases** utilizando `produto_id`
- Criar novas features baseadas na data de abertura
- Tratar valores nulos
- Remover colunas desnecessárias
- Gerar o dataset final utilizado para treinamento

Entre as features geradas estão:

- `ano_abertura`
- `mes_abertura`
- `dia_abertura`
- `dia_semana_abertura`

O resultado final é um dataset preparado para treinamento do modelo.

---

## train.py

Script responsável pelo **treinamento do modelo de Machine Learning**.

Principais etapas:

1. Carregar o dataset tratado
2. Separar as variáveis de entrada (**features**) da variável alvo (**target**)
3. Dividir os dados em conjunto de treino e teste
4. Treinar o modelo de regressão
5. Avaliar o modelo
6. Salvar o modelo treinado

---

## Arquivos gerados

Após o treinamento, dois arquivos são gerados:

- `modelo_tempo_os.pkl`
- `colunas_modelo.pkl`

### modelo_tempo_os.pkl

Arquivo que contém o **modelo treinado**.

Esse modelo será utilizado pela aplicação Django para realizar previsões.

---

### colunas_modelo.pkl

Arquivo que armazena a **lista de colunas utilizadas no treinamento do modelo**.

Isso garante que a ordem e estrutura das features utilizadas na previsão sejam as mesmas utilizadas durante o treinamento.

---

# Pasta models

A pasta `models` armazena os arquivos gerados após o treinamento do modelo.

Arquivos armazenados:

- `modelo_tempo_os.pkl`
- `colunas_modelo.pkl`

Esses arquivos são carregados pela aplicação Django para realizar previsões em tempo real.

---

# Aplicação Django

A aplicação web foi desenvolvida utilizando **Django**.

Ela permite que um usuário insira os dados de uma ordem de serviço e receba a previsão do tempo de resolução.

---

# previsao/forms.py

Arquivo responsável por definir o **formulário exibido na interface web**.

Esse formulário coleta os dados necessários para gerar a previsão.

Campos principais do formulário:

- `tipo_atendimento_id`
- `produto_id`
- `defeito_reclamado_id`
- `defeito_constatado_id`
- `solucao_id`
- `data_abertura`

Esses campos representam as principais informações de uma ordem de serviço.

Após o envio do formulário, esses dados são utilizados para montar o **vetor de entrada do modelo de Machine Learning**.

---

# previsao/views.py

Arquivo responsável pela **lógica de funcionamento da aplicação web**.

Principais responsabilidades:

- Receber os dados enviados pelo formulário
- Buscar as informações do produto em `export_produtos.csv`
- Montar o vetor de features com base nos dados fornecidos
- Carregar o modelo treinado
- Executar a previsão
- Exibir o resultado para o usuário

---

# Fluxo de Funcionamento do Sistema

O funcionamento do sistema ocorre da seguinte forma:

1. O usuário preenche o formulário na interface web
2. O Django recebe os dados enviados
3. O sistema busca as características do produto
4. Um vetor de features é montado
5. O modelo de Machine Learning é carregado
6. O modelo realiza a previsão do tempo de resolução
7. O resultado é exibido na tela para o usuário

---

# Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python**
- **Django**
- **Pandas**
- **Scikit-learn**
- **HTML**
- **CSS**

---

# Conclusão

Este projeto demonstra a integração entre:

- Engenharia de Dados
- Machine Learning
- Desenvolvimento Web

Ele mostra como um modelo de aprendizado de máquina pode ser integrado a uma aplicação web para gerar previsões em tempo real, permitindo que usuários interajam diretamente com o sistema de forma simples e intuitiva.