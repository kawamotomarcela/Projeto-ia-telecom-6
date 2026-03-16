# 📊 PROPOSTA 6 — Predição de Tempo de Resolução

**Status:** Em desenvolvimento ⚠️👍

---

# ▶️ Como Rodar o Projeto

Siga os passos abaixo para executar o sistema localmente.

---

## 1️⃣ Clonar o Repositório

No terminal (CMD / PowerShell / Terminal):

```bash
git clone https://github.com/kawamotomarcela/Projeto-ia-telecom-6.git

cd Projeto-ia-telecom-6
```

## 2️⃣ Criar Ambiente Virtual

Dentro da pasta do projeto.

Windows
```
python -m venv venv
venv\Scripts\activate
```

Linux / Mac
```
python3 -m venv venv
source venv/bin/activate
```
## 3️⃣ Instalar Dependências
```
pip install -r requirements.txt
```

## 4️⃣ Verificar os Datasets

Certifique-se de que os arquivos necessários estão dentro da pasta:

```
Dataset/
```

Arquivos utilizados pelo projeto:
```
Dataset/export_os_defeito_solucao.csv
Dataset/export_produtos.csv
```
Esses datasets são utilizados para:

- treinamento do modelo

- geração das features do modelo

- consulta de características do produto

## 5️⃣ Treinar o Modelo de Machine Learning

Antes de rodar o sistema é necessário treinar o modelo.

Execute:
```
python src/train.py
```
Esse script irá:

1- Carregar os datasets

2- Fazer o merge das bases

3- Criar features de data

4- Gerar o dataset tratado

5- Treinar o modelo de Machine Learning

6- Salvar os arquivos do modelo

Os arquivos gerados serão:
```
models/modelo_tempo_os.pkl
models/colunas_modelo.pkl
```
Esses arquivos são utilizados posteriormente pelo Django para gerar previsões.

## 6️⃣ Configurar o Django

Execute as migrações do banco de dados:
```
python manage.py makemigrations
python manage.py migrate
```

## 7️⃣ Rodar o Servidor
```
python manage.py runserver
```
Abra no navegador:
```
http://127.0.0.1:8000
```
A interface permitirá inserir os dados da Ordem de Serviço e gerar a previsão de tempo de resolução.

## ✔️ Resumo Rápido

Para rodar rapidamente:
```
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python src/train.py

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

## 📌 Melhorias Futuras

Planejadas para próximas versões:

- pasta datasetinfo com descrição dos IDs

- interface com busca de defeitos e soluções

- pipeline automático de treino

- validação mais robusta do modelo

- melhorias de UX na interface