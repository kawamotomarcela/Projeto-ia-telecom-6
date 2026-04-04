# 📊 PROPOSTA 6 — Predição de Tempo de Resolução

**Status:** Em desenvolvimento ⚠️👍

---


## 👥 Nomes - Grupo:
- Nathan Gabriel da Silva RA: 2078558 
- Marcela Kawamoto Fernandes RA: 2224453 
- Kenji Yuri Mitsuka de Paula, RA: 2033472 
- Julia Soares de Azevedo Lombardi RA: 2032874 
- Tainá De Souza Alves RA: 2041631 
- Matheus Bargas Rodrigues Flausino RA: 2057008 
- Lucia Maria Reis Braga RA: 2035292 

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

## 📌 Observações

Atualmente, o projeto já utiliza a pasta DatasetInfo para melhorar a interface, permitindo que o usuário selecione descrições legíveis em vez de preencher apenas IDs numéricos.

Como possibilidades futuras, o projeto pode evoluir com:

- uso de API, caso seja necessário centralizar os dados auxiliares em um único serviço
- uso de Sass/SCSS, caso a interface cresça e seja necessário organizar melhor os estilos
- busca inteligente para produto
- pipeline automático de treino
- melhorias de UX e validação do modelo

