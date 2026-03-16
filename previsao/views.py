import joblib
import pandas as pd
from pathlib import Path
from django.shortcuts import render
from .forms import PrevisaoForm

BASE_DIR = Path(__file__).resolve().parent.parent

modelo = joblib.load(BASE_DIR / "models" / "modelo_tempo_os.pkl")
colunas_modelo = joblib.load(BASE_DIR / "models" / "colunas_modelo.pkl")
produtos_df = pd.read_csv(BASE_DIR / "Dataset" / "export_produtos.csv")


def home(request):
    resultado = None
    erro = None

    if request.method == "POST":
        form = PrevisaoForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data
            produto_id = dados["produto_id"]

            produto_info = produtos_df[produtos_df["produto_id"] == produto_id]

            if produto_info.empty:
                erro = "O produto_id informado não foi encontrado na base export_produtos.csv."
            else:
                produto_info = produto_info.iloc[0]
                data_abertura = pd.to_datetime(dados["data_abertura"])

                entrada = {
                    "tipo_atendimento_id": dados["tipo_atendimento_id"],
                    "produto_id": produto_id,
                    "defeito_reclamado_id": dados["defeito_reclamado_id"] or 0,
                    "defeito_constatado_id": dados["defeito_constatado_id"] or 0,
                    "solucao_id": dados["solucao_id"] or 0,
                    "ano_abertura": data_abertura.year,
                    "mes_abertura": data_abertura.month,
                    "dia_abertura": data_abertura.day,
                    "dia_semana_abertura": data_abertura.dayofweek,
                    "fabrica_id": produto_info["fabrica_id"],
                    "linha_id": produto_info["linha_id"],
                    "familia_id": produto_info["familia_id"],
                }

                entrada_final = {col: entrada.get(col, 0) for col in colunas_modelo}
                df_entrada = pd.DataFrame([entrada_final])

                previsao = modelo.predict(df_entrada)[0]
                resultado = round(float(previsao), 2)

    else:
        form = PrevisaoForm()

    return render(request, "home.html", {
        "form": form,
        "resultado": resultado,
        "erro": erro,
    })