import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

os_defeito_solucao = pd.read_csv(BASE_DIR / "Dataset" / "export_os_defeito_solucao.csv")
produtos = pd.read_csv(BASE_DIR / "Dataset" / "export_produtos.csv")

print("OS + defeito + solução:", os_defeito_solucao.shape)
print("Produtos:", produtos.shape)

# merge pedido pela atividade
dados = os_defeito_solucao.merge(produtos, on="produto_id", how="left")

print("Após merge:", dados.shape)

# converter datas
dados["data_abertura"] = pd.to_datetime(dados["data_abertura"], errors="coerce")
dados["data_fechamento"] = pd.to_datetime(dados["data_fechamento"], errors="coerce")

# criar atributos derivados da data de abertura
dados["ano_abertura"] = dados["data_abertura"].dt.year
dados["mes_abertura"] = dados["data_abertura"].dt.month
dados["dia_abertura"] = dados["data_abertura"].dt.day
dados["dia_semana_abertura"] = dados["data_abertura"].dt.dayofweek

# remover colunas que não devem entrar no modelo
colunas_descartar = [
    "os_id_anonimo",
    "data_abertura",
    "data_fechamento",
    "referencia_anonima",
    "linha_descricao",
    "familia_descricao",
]
dados = dados.drop(columns=colunas_descartar, errors="ignore")

# remover linhas sem target
dados = dados.dropna(subset=["tempo_resolucao_horas"])

# tratar nulos das features
# IDs ausentes podem virar 0
colunas_ids = [
    "produto_id",
    "defeito_reclamado_id",
    "defeito_constatado_id",
    "solucao_id",
    "fabrica_id",
    "linha_id",
    "familia_id",
]
for col in colunas_ids:
    if col in dados.columns:
        dados[col] = dados[col].fillna(0)

# remover linhas sem data derivada ou tipo de atendimento
colunas_obrigatorias = [
    "tipo_atendimento_id",
    "ano_abertura",
    "mes_abertura",
    "dia_abertura",
    "dia_semana_abertura",
]
dados = dados.dropna(subset=colunas_obrigatorias)

# garantir tipos numéricos
for col in dados.columns:
    if col != "tempo_resolucao_horas":
        dados[col] = pd.to_numeric(dados[col], errors="coerce")

dados = dados.dropna()

# converter para int onde faz sentido
colunas_int = [col for col in dados.columns if col != "tempo_resolucao_horas"]
dados[colunas_int] = dados[colunas_int].astype(int)

# salvar
saida = BASE_DIR / "Dataset" / "dados_tratados.csv"
dados.to_csv(saida, index=False)

print("Dataset tratado salvo com sucesso em:", saida)
print("Shape final:", dados.shape)
print("\nColunas finais:")
print(dados.columns.tolist())
print("\nNulos finais:")
print(dados.isna().sum())