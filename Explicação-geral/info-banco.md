## 🗄️ Banco de Dados

O projeto utiliza banco de dados SQLite por meio do Django.

Atualmente, o banco foi adicionado principalmente para:

armazenar o histórico das previsões realizadas
permitir futura consulta administrativa desses registros
manter a estrutura padrão do Django para autenticação, sessões e administração

Ou seja, o modelo de Machine Learning continua funcionando com os arquivos .csv e .pkl, mas o banco de dados foi incorporado para registrar e consultar o histórico de uso do sistema.

O arquivo do banco é:
```
db.sqlite3
```
Histórico de Previsões

Sempre que uma previsão é gerada com sucesso, os dados principais da entrada e o resultado em horas podem ser salvos no banco para consulta posterior.

Isso torna o projeto mais completo, pois além de prever, ele também passa a registrar as previsões já realizadas.

## 🔐 Acesso ao Admin do Django

Caso queira testar o painel administrativo do Django para visualizar o histórico salvo no banco, crie um superusuário com:

```
python manage.py createsuperuser
Sugestão para testes
Usuário: admin
Email: admin@teste.com
Senha: Superuser123!
```
Depois, com o servidor rodando, acesse:
```
http://127.0.0.1:8000/admin
```