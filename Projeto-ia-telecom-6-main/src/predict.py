import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
ARQUIVO_MODELO = MODELS_DIR / "modelo_tempo_os.pkl"
ARQUIVO_COLUNAS = MODELS_DIR / "colunas_modelo.pkl"


def carregar_artefatos():
    """
    Carrega o modelo treinado e a lista de colunas usadas no treinamento.
    """
    if not ARQUIVO_MODELO.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado em: {ARQUIVO_MODELO}\n"
            f"Execute primeiro o train.py."
        )

    if not ARQUIVO_COLUNAS.exists():
        raise FileNotFoundError(
            f"Arquivo de colunas não encontrado em: {ARQUIVO_COLUNAS}\n"
            f"Execute primeiro o train.py."
        )

    modelo = joblib.load(ARQUIVO_MODELO)
    colunas = joblib.load(ARQUIVO_COLUNAS)

    return modelo, colunas


def montar_entrada_padrao(colunas: list[str]) -> pd.DataFrame:
    """
    Monta uma entrada de exemplo preenchendo todas as colunas com zero.
    """
    entrada = {coluna: 0 for coluna in colunas}
    return pd.DataFrame([entrada])


def main():
    print("Carregando modelo e colunas...")
    modelo, colunas = carregar_artefatos()

    print("Montando entrada de teste...")
    df_entrada = montar_entrada_padrao(colunas)

    print("Realizando previsão...")
    previsao = modelo.predict(df_entrada)[0]

    print(f"Tempo previsto: {previsao}")


if __name__ == "__main__":
    main()