from functools import lru_cache
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"
DATASET_INFO_DIR = DATASET_DIR / "DatasetInfo"


def _read_csv_safe(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    last_error = None
    for encoding in ("utf-8-sig", "utf-8", "latin-1", "cp1252"):
        try:
            return pd.read_csv(path, encoding=encoding, on_bad_lines="skip")
        except Exception as exc:
            last_error = exc

    raise last_error


def _normalize_text(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip()

    if text.upper() == "NULL":
        return ""

    text = " ".join(text.split())

    if text in {"-", "--", "---"}:
        return ""

    return text


def _safe_int(value):
    if pd.isna(value):
        return None

    try:
        return int(float(value))
    except Exception:
        return None


def _build_choices(df: pd.DataFrame, id_col: str, desc_col: str, prefix: str = "ID"):
    choices_map = {}

    if id_col not in df.columns:
        return [("", "---------")]

    for _, row in df.iterrows():
        item_id = _safe_int(row.get(id_col))
        if item_id is None or item_id in choices_map:
            continue

        desc = _normalize_text(row.get(desc_col, ""))
        label = f"{item_id} - {desc}" if desc else f"{prefix} {item_id}"
        choices_map[item_id] = label

    ordered = sorted(choices_map.items(), key=lambda item: item[1].lower())
    return [("", "---------")] + ordered


@lru_cache(maxsize=1)
def get_form_choices():
    tipos_df = _read_csv_safe(DATASET_INFO_DIR / "export_tipos_atendimento.csv")
    solucoes_df = _read_csv_safe(DATASET_INFO_DIR / "export_solucoes.csv")
    defeitos_reclamados_df = _read_csv_safe(DATASET_INFO_DIR / "export_defeitos_reclamados.csv")
    defeitos_constatados_df = _read_csv_safe(DATASET_INFO_DIR / "export_defeitos_constatados.csv")

    return {
        "tipos_atendimento": _build_choices(
            tipos_df,
            "tipo_atendimento_id",
            "descricao",
            "Tipo"
        ),
        "solucoes": _build_choices(
            solucoes_df,
            "solucao_id",
            "descricao",
            "Solução"
        ),
        "defeitos_reclamados": _build_choices(
            defeitos_reclamados_df,
            "defeito_reclamado_id",
            "descricao",
            "Defeito reclamado"
        ),
        "defeitos_constatados": _build_choices(
            defeitos_constatados_df,
            "defeito_constatado_id",
            "descricao",
            "Defeito constatado"
        ),
    }


@lru_cache(maxsize=1)
def get_produtos_df():
    df = _read_csv_safe(DATASET_DIR / "export_produtos.csv").copy()

    for col in ["produto_id", "fabrica_id", "linha_id", "familia_id"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df