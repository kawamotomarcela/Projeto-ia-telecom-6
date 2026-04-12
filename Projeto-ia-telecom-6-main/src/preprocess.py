import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "Dataset"
PROCESSED_DIR = DATASET_DIR / "processed"

ARQUIVO_OS_DEFEITO_SOLUCAO = DATASET_DIR / "export_os_defeito_solucao.csv"
ARQUIVO_PRODUTOS = DATASET_DIR / "export_produtos.csv"
ARQUIVO_SAIDA = PROCESSED_DIR / "dados_tratados.csv"


def carregar_csv(caminho: Path) -> pd.DataFrame:
    """
    Carrega um CSV com tentativas de codificação para evitar erros comuns.
    """
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    ultimo_erro = None
    for encoding in ("utf-8-sig", "utf-8", "latin-1", "cp1252"):
        try:
            return pd.read_csv(caminho, encoding=encoding)
        except Exception as erro:
            ultimo_erro = erro

    raise ValueError(f"Não foi possível ler o arquivo {caminho}. Erro: {ultimo_erro}")


def validar_colunas(df: pd.DataFrame, nome_arquivo: str, colunas_obrigatorias: list[str]) -> None:
    """
    Verifica se as colunas obrigatórias existem no DataFrame.
    """
    colunas_faltantes = [col for col in colunas_obrigatorias if col not in df.columns]
    if colunas_faltantes:
        raise ValueError(
            f"O arquivo '{nome_arquivo}' não possui as colunas obrigatórias: {colunas_faltantes}"
        )


def criar_features_temporais(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria colunas derivadas da data de abertura.
    """
    df["data_abertura"] = pd.to_datetime(df["data_abertura"], errors="coerce")
    df["data_fechamento"] = pd.to_datetime(df["data_fechamento"], errors="coerce")

    df["ano_abertura"] = df["data_abertura"].dt.year
    df["mes_abertura"] = df["data_abertura"].dt.month
    df["dia_abertura"] = df["data_abertura"].dt.day
    df["dia_semana_abertura"] = df["data_abertura"].dt.dayofweek

    return df


def tratar_nulos_ids(df: pd.DataFrame, colunas_ids: list[str]) -> pd.DataFrame:
    """
    Preenche IDs ausentes com 0.
    """
    for coluna in colunas_ids:
        if coluna in df.columns:
            df[coluna] = df[coluna].fillna(0)
    return df


def converter_colunas_numericas(df: pd.DataFrame, target: str) -> pd.DataFrame:
    """
    Converte todas as colunas, exceto a target, para numérico.
    """
    for coluna in df.columns:
        if coluna != target:
            df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
    return df


def converter_colunas_para_int(df: pd.DataFrame, target: str) -> pd.DataFrame:
    """
    Converte para inteiro todas as colunas, exceto a variável alvo.
    """
    colunas_int = [col for col in df.columns if col != target]
    df[colunas_int] = df[colunas_int].astype(int)
    return df


def main():
    print("Iniciando preprocessamento...")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    print("Carregando datasets...")
    os_defeito_solucao = carregar_csv(ARQUIVO_OS_DEFEITO_SOLUCAO)
    produtos = carregar_csv(ARQUIVO_PRODUTOS)

    print(f"OS + defeito + solução: {os_defeito_solucao.shape}")
    print(f"Produtos: {produtos.shape}")

    validar_colunas(
        os_defeito_solucao,
        "export_os_defeito_solucao.csv",
        [
            "produto_id",
            "tipo_atendimento_id",
            "data_abertura",
            "data_fechamento",
            "tempo_resolucao_horas",
        ],
    )

    validar_colunas(
        produtos,
        "export_produtos.csv",
        [
            "produto_id",
            "fabrica_id",
            "linha_id",
            "familia_id",
        ],
    )

    print("Realizando merge entre as bases...")
    dados = os_defeito_solucao.merge(produtos, on="produto_id", how="left")
    print(f"Após merge: {dados.shape}")

    print("Criando features temporais...")
    dados = criar_features_temporais(dados)

    print("Removendo colunas desnecessárias...")
    colunas_descartar = [
        "os_id_anonimo",
        "data_abertura",
        "data_fechamento",
        "referencia_anonima",
        "linha_descricao",
        "familia_descricao",
    ]
    dados = dados.drop(columns=colunas_descartar, errors="ignore")

    print("Removendo linhas sem variável alvo...")
    dados = dados.dropna(subset=["tempo_resolucao_horas"])

    print("Tratando nulos em colunas de IDs...")
    colunas_ids = [
        "produto_id",
        "defeito_reclamado_id",
        "defeito_constatado_id",
        "solucao_id",
        "fabrica_id",
        "linha_id",
        "familia_id",
    ]
    dados = tratar_nulos_ids(dados, colunas_ids)

    print("Removendo linhas sem colunas obrigatórias para modelagem...")
    colunas_obrigatorias = [
        "tipo_atendimento_id",
        "ano_abertura",
        "mes_abertura",
        "dia_abertura",
        "dia_semana_abertura",
    ]
    dados = dados.dropna(subset=colunas_obrigatorias)

    print("Convertendo colunas para formato numérico...")
    dados = converter_colunas_numericas(dados, target="tempo_resolucao_horas")

    print("Removendo registros com valores inválidos após conversão...")
    dados = dados.dropna()

    if dados.empty:
        raise ValueError(
            "O dataset ficou vazio após o preprocessamento. Verifique os dados de entrada e as regras aplicadas."
        )

    print("Convertendo colunas de entrada para inteiro...")
    dados = converter_colunas_para_int(dados, target="tempo_resolucao_horas")

    print("Salvando dataset tratado...")
    dados.to_csv(ARQUIVO_SAIDA, index=False)

    print("\nPreprocessamento concluído com sucesso.")
    print(f"Arquivo salvo em: {ARQUIVO_SAIDA}")
    print(f"Shape final: {dados.shape}")
    print("\nColunas finais:")
    print(dados.columns.tolist())
    print("\nValores nulos finais:")
    print(dados.isna().sum())


if __name__ == "__main__":
    main()