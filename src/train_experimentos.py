import math
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

try:
    from xgboost import XGBRegressor
    XGBOOST_DISPONIVEL = True
except Exception:
    XGBOOST_DISPONIVEL = False


BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "Dataset"
PROCESSED_DIR = DATASET_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"

ARQUIVO_DADOS_TRATADOS = PROCESSED_DIR / "dados_tratados.csv"
ARQUIVO_RESULTADOS = MODELS_DIR / "resultados_experimentos.json"

TARGET = "tempo_resolucao_horas"


def carregar_dataset(caminho: Path) -> pd.DataFrame:
    if not caminho.exists():
        raise FileNotFoundError(
            f"O arquivo de dados tratados não foi encontrado em: {caminho}\n"
            f"Execute primeiro o preprocess.py."
        )

    df = pd.read_csv(caminho)

    if df.empty:
        raise ValueError("O dataset tratado está vazio.")

    if TARGET not in df.columns:
        raise ValueError(f"A coluna alvo '{TARGET}' não foi encontrada.")

    return df


def avaliar_modelo(y_true, y_pred) -> dict:
    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": round(float(mae), 4),
        "RMSE": round(float(rmse), 4),
        "R2": round(float(r2), 4),
    }


def salvar_json(dados: dict, caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def obter_modelos():
    modelos = {
        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1,
        ),
        "NN_MLPRegressor": Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                (
                    "mlp",
                    MLPRegressor(
                        hidden_layer_sizes=(64, 32),
                        activation="relu",
                        solver="adam",
                        alpha=0.0001,
                        learning_rate="adaptive",
                        learning_rate_init=0.001,
                        max_iter=100,
                        early_stopping=True,
                        validation_fraction=0.1,
                        n_iter_no_change=10,
                        random_state=42,
                        verbose=True,
                    ),
                ),
            ]
        ),
    }

    if XGBOOST_DISPONIVEL:
        modelos["XGBoost"] = XGBRegressor(
            objective="reg:squarederror",
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            n_jobs=-1,
        )

    return modelos


def main():
    print("Iniciando comparação de modelos...")

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    df = carregar_dataset(ARQUIVO_DADOS_TRATADOS)

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    print(f"Dataset carregado: {df.shape}")
    print(f"Quantidade de amostras: {len(df)}")
    print("Features utilizadas:")
    print(X.columns.tolist())

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    # Amostra reduzida para modelos mais pesados, como a rede neural
    amostra_max = 100_000

    if len(X_train) > amostra_max:
        X_train_exp = X_train.sample(n=amostra_max, random_state=42)
        y_train_exp = y_train.loc[X_train_exp.index]
    else:
        X_train_exp = X_train
        y_train_exp = y_train

    print(f"\nBase completa de treino: {X_train.shape}")
    print(f"Base reduzida para experimentos pesados: {X_train_exp.shape}")

    resultados = {}
    modelos = obter_modelos()

    for nome, modelo in modelos.items():
        print(f"\nTreinando modelo: {nome}")

        if nome == "NN_MLPRegressor":
            print("Usando base reduzida para a rede neural...")
            modelo.fit(X_train_exp, y_train_exp)
        else:
            modelo.fit(X_train, y_train)

        print(f"Realizando predições com: {nome}")
        pred = modelo.predict(X_test)

        metricas = avaliar_modelo(y_test, pred)
        resultados[nome] = metricas

        print(f"Resultados {nome}:")
        print(f"MAE: {metricas['MAE']}")
        print(f"RMSE: {metricas['RMSE']}")
        print(f"R²: {metricas['R2']}")

        nome_arquivo_modelo = f"modelo_{nome.lower().replace(' ', '_')}_teste.pkl"
        caminho_modelo = MODELS_DIR / nome_arquivo_modelo
        joblib.dump(modelo, caminho_modelo)
        print(f"Modelo de teste salvo em: {caminho_modelo}")

    melhor_modelo = min(resultados, key=lambda nome: resultados[nome]["RMSE"])

    resumo = {
        "target": TARGET,
        "quantidade_amostras": int(len(df)),
        "quantidade_features": int(X.shape[1]),
        "melhor_modelo_experimentos": melhor_modelo,
        "resultados": resultados,
        "observacao": (
            "Os experimentos não substituem automaticamente o modelo oficial do projeto. "
            "Servem apenas para comparação de desempenho."
        ),
    }

    salvar_json(resumo, ARQUIVO_RESULTADOS)

    print("\nResumo final dos experimentos:")
    for nome, metricas in resultados.items():
        print(f"{nome}: {metricas}")

    print(f"\nMelhor modelo nos experimentos: {melhor_modelo}")
    print(f"Resultados salvos em: {ARQUIVO_RESULTADOS}")


if __name__ == "__main__":
    main()