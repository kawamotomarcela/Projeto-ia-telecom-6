import joblib
import pandas as pd

modelo = joblib.load("models/modelo_tempo_os.pkl")
colunas = joblib.load("models/colunas_modelo.pkl")

# exemplo
entrada = {col: 0 for col in colunas}

df = pd.DataFrame([entrada])

previsao = modelo.predict(df)

print("Tempo previsto:", previsao[0])