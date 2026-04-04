import math
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "Dataset"
PROCESSED_DIR = DATASET_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"

ARQUIVO_DADOS_TRATADOS = PROCESSED_DIR / "dados_tratados.csv"
ARQUIVO_MODELO = MODELS_DIR / "modelo_tempo_os.pkl"
ARQUIVO_COLUNAS = MODELS_DIR / "colunas_modelo.pkl"

TARGET = "tempo_resolucao_horas"


def carregar_dataset(caminho: Path) -> pd.DataFrame:
    """
    Carrega o dataset tratado.
    """
    if not caminho.exists():
        raise FileNotFoundError(
            f"O arquivo de dados tratados não foi encontrado em: {caminho}\n"
            f"Execute primeiro o preprocess.py."
        )

    df = pd.read_csv(caminho)

    if df.empty:
        raise ValueError(
            "O dataset tratado está vazio. Verifique se o preprocess.py foi executado corretamente."
        )

    if TARGET not in df.columns:
        raise ValueError(
            f"A coluna alvo '{TARGET}' não foi encontrada no dataset tratado."
        )

    return df


def avaliar_modelo(y_true, y_pred) -> dict:
    """
    Calcula métricas de avaliação do modelo.
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
    }


def main():
    print("Iniciando treinamento do modelo...")

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    print("Carregando dataset tratado...")
    df = carregar_dataset(ARQUIVO_DADOS_TRATADOS)

    print(f"Dataset carregado: {df.shape}")

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    print(f"Quantidade de amostras: {len(df)}")
    print("Features utilizadas:")
    print(X.columns.tolist())

    print("\nSeparando dados de treino e teste...")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    print("Treinando modelo RandomForestRegressor...")
    modelo = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1,
    )

    modelo.fit(X_train, y_train)

    print("Realizando predições no conjunto de teste...")
    y_pred = modelo.predict(X_test)

    metricas = avaliar_modelo(y_test, y_pred)

    print("\nTreinamento concluído.")
    print(f"MAE: {metricas['MAE']:.4f}")
    print(f"RMSE: {metricas['RMSE']:.4f}")
    print(f"R²: {metricas['R2']:.4f}")

    print("\nSalvando artefatos do modelo...")
    joblib.dump(modelo, ARQUIVO_MODELO)
    joblib.dump(list(X.columns), ARQUIVO_COLUNAS)

    print("Modelo salvo com sucesso em:")
    print(ARQUIVO_MODELO)
    print(ARQUIVO_COLUNAS)


if __name__ == "__main__":
    main()