# 📊 PROPOSTA 6 - Predição de Tempo de Resolução
**Status:** Em desenvolvimento ⚠️👍  


---
# ▶️ Como Rodar o Projeto

Este projeto utiliza **Python, Django e Machine Learning** para prever o tempo de resolução de Ordens de Serviço.

Siga os passos abaixo para executar o projeto.

---

# 1️⃣ Instalar Requisitos

Certifique-se de ter instalado:

- Python 3.10 ou superior
- pip

Verifique a versão do Python:

```bash
python --version
```

## 2️⃣ Criar Ambiente Virtual

Dentro da pasta do projeto, execute:

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
## 4️⃣ Configurar o Django

Entre na pasta onde está o manage.py e execute:

```
python manage.py makemigrations
python manage.py migrate
```
## 5️⃣ Rodar o Servidor
```
python manage.py runserver
```

Abra no navegador:
```
http://127.0.0.1:8000
```
## 6️⃣ Rodar Treinamento do Modelo (Opcional)

Se quiser treinar o modelo de Machine Learning:

```
python src/train.py
```
# ✔️ Resumo Rápido
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
