import json
from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd
from django.shortcuts import render

from .forms import PrevisaoForm
from .models import HistoricoPrevisao
from .utils import get_produtos_df

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
MODELO_PATH = MODELS_DIR / "modelo_tempo_os.pkl"
COLUNAS_PATH = MODELS_DIR / "colunas_modelo.pkl"
METADATA_PATH = MODELS_DIR / "metadata_modelo.json"


@lru_cache(maxsize=1)
def carregar_artefatos_modelo():
    if not MODELO_PATH.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado em: {MODELO_PATH}\n"
            f"Execute primeiro o train.py."
        )

    if not COLUNAS_PATH.exists():
        raise FileNotFoundError(
            f"Arquivo de colunas não encontrado em: {COLUNAS_PATH}\n"
            f"Execute primeiro o train.py."
        )

    modelo = joblib.load(MODELO_PATH)
    colunas_modelo = joblib.load(COLUNAS_PATH)

    metadata = {}
    if METADATA_PATH.exists():
        with open(METADATA_PATH, "r", encoding="utf-8") as arquivo:
            metadata = json.load(arquivo)

    return modelo, colunas_modelo, metadata


def to_int_or_zero(value):
    if value in ("", None):
        return 0

    try:
        if pd.isna(value):
            return 0
    except Exception:
        pass

    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0


def zero_to_none(value):
    value = to_int_or_zero(value)
    return None if value == 0 else value


def home(request):
    resultado = None
    erro = None
    modelo_utilizado = "RandomForest"

    form = PrevisaoForm(request.POST or None)

    try:
        modelo, colunas_modelo, metadata = carregar_artefatos_modelo()
        modelo_utilizado = metadata.get("melhor_modelo", "RandomForest")
    except Exception as exc:
        modelo = None
        colunas_modelo = []
        erro = f"Erro ao carregar o modelo: {exc}"

    if request.method == "POST" and form.is_valid() and modelo is not None:
        try:
            dados = form.cleaned_data

            tipo_atendimento_id = to_int_or_zero(dados.get("tipo_atendimento_id"))
            produto_id = to_int_or_zero(dados.get("produto_id"))
            defeito_reclamado_id = to_int_or_zero(dados.get("defeito_reclamado_id"))
            defeito_constatado_id = to_int_or_zero(dados.get("defeito_constatado_id"))
            solucao_id = to_int_or_zero(dados.get("solucao_id"))
            data_abertura = pd.to_datetime(dados.get("data_abertura"))

            produtos_df = get_produtos_df()
            produto_info = produtos_df[produtos_df["produto_id"] == produto_id]

            if produto_info.empty:
                erro = "O produto_id informado não foi encontrado na base export_produtos.csv."
            else:
                produto_info = produto_info.iloc[0]

                entrada = {
                    "tipo_atendimento_id": tipo_atendimento_id,
                    "produto_id": produto_id,
                    "defeito_reclamado_id": defeito_reclamado_id,
                    "defeito_constatado_id": defeito_constatado_id,
                    "solucao_id": solucao_id,
                    "ano_abertura": int(data_abertura.year),
                    "mes_abertura": int(data_abertura.month),
                    "dia_abertura": int(data_abertura.day),
                    "dia_semana_abertura": int(data_abertura.dayofweek),
                    "fabrica_id": to_int_or_zero(produto_info.get("fabrica_id")),
                    "linha_id": to_int_or_zero(produto_info.get("linha_id")),
                    "familia_id": to_int_or_zero(produto_info.get("familia_id")),
                }

                entrada_final = {
                    coluna: to_int_or_zero(entrada.get(coluna, 0))
                    for coluna in colunas_modelo
                }

                df_entrada = pd.DataFrame([entrada_final])

                previsao = modelo.predict(df_entrada)[0]
                resultado = round(float(previsao), 2)

                HistoricoPrevisao.objects.create(
                    tipo_atendimento_id=tipo_atendimento_id,
                    produto_id=produto_id,
                    defeito_reclamado_id=zero_to_none(defeito_reclamado_id),
                    defeito_constatado_id=zero_to_none(defeito_constatado_id),
                    solucao_id=zero_to_none(solucao_id),
                    data_abertura=dados.get("data_abertura"),
                    fabrica_id=to_int_or_zero(produto_info.get("fabrica_id")),
                    linha_id=to_int_or_zero(produto_info.get("linha_id")),
                    familia_id=to_int_or_zero(produto_info.get("familia_id")),
                    resultado_horas=resultado,
                )

        except Exception as exc:
            erro = f"Ocorreu um erro ao gerar a previsão: {exc}"

    return render(
        request,
        "home.html",
        {
            "form": form,
            "resultado": resultado,
            "erro": erro,
            "modelo_utilizado": modelo_utilizado,
        },
    )