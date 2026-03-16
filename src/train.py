import math
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent.parent

arquivo = BASE_DIR / "Dataset" / "dados_tratados.csv"
df = pd.read_csv(arquivo)

print("Dataset carregado:", df.shape)

target = "tempo_resolucao_horas"

if target not in df.columns:
    raise ValueError(f"A coluna alvo '{target}' não foi encontrada.")

if df.shape[0] == 0:
    raise ValueError("O dataset tratado ficou vazio. Verifique o preprocess.py.")

X = df.drop(columns=[target])
y = df[target]

print("Features:", X.columns.tolist())
print("Quantidade de amostras:", len(df))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
rmse = math.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("\nTreinamento concluído.")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

models_dir = BASE_DIR / "models"
models_dir.mkdir(exist_ok=True)

joblib.dump(model, models_dir / "modelo_tempo_os.pkl")
joblib.dump(list(X.columns), models_dir / "colunas_modelo.pkl")

print("\nModelo salvo com sucesso em:")
print(models_dir / "modelo_tempo_os.pkl")
print(models_dir / "colunas_modelo.pkl")