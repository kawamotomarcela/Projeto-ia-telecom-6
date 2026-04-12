import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

import gdown

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATASET_DIR = BASE_DIR / "Dataset"
DATASET_INFO_DIR = DATASET_DIR / "DatasetInfo"
PROCESSED_DIR = DATASET_DIR / "processed"

DRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1YG2V6OksrwnAIEa1Aui2HqZWfh_SfzQ5"

ARQUIVOS_OBRIGATORIOS = {
    "export_os_defeito_solucao.csv": DATASET_DIR / "export_os_defeito_solucao.csv",
    "export_produtos.csv": DATASET_DIR / "export_produtos.csv",
    "export_tipos_atendimento.csv": DATASET_INFO_DIR / "export_tipos_atendimento.csv",
    "export_solucoes.csv": DATASET_INFO_DIR / "export_solucoes.csv",
    "export_defeitos_reclamados.csv": DATASET_INFO_DIR / "export_defeitos_reclamados.csv",
    "export_defeitos_constatados.csv": DATASET_INFO_DIR / "export_defeitos_constatados.csv",
}


def preparar_pastas() -> None:
    DATASET_DIR.mkdir(parents=True, exist_ok=True)
    DATASET_INFO_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def baixar_pasta_drive(destino_temporario: Path) -> list[str]:
    print("Baixando datasets do Google Drive...")
    arquivos_baixados = gdown.download_folder(
        url=DRIVE_FOLDER_URL,
        output=str(destino_temporario),
        quiet=False,
        use_cookies=False,
    )

    if not arquivos_baixados:
        raise RuntimeError(
            "Nenhum arquivo foi baixado. Verifique se a pasta do Google Drive está pública."
        )

    return arquivos_baixados


def indexar_arquivos(base: Path) -> dict[str, Path]:
    encontrados = {}

    for arquivo in base.rglob("*"):
        if arquivo.is_file():
            encontrados[arquivo.name] = arquivo

    return encontrados


def copiar_arquivos_necessarios(arquivos_encontrados: dict[str, Path]) -> None:
    faltantes = []

    for nome_arquivo, destino_final in ARQUIVOS_OBRIGATORIOS.items():
        origem = arquivos_encontrados.get(nome_arquivo)

        if origem is None:
            faltantes.append(nome_arquivo)
            continue

        destino_final.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origem, destino_final)
        print(f"Arquivo copiado: {destino_final}")

    if faltantes:
        raise FileNotFoundError(
            "Os seguintes arquivos obrigatórios não foram encontrados na pasta baixada:\n"
            + "\n".join(f"- {nome}" for nome in faltantes)
        )


def main():
    print("Iniciando download dos datasets...")

    preparar_pastas()

    with TemporaryDirectory() as pasta_temp:
        pasta_temp_path = Path(pasta_temp)

        baixar_pasta_drive(pasta_temp_path)
        arquivos_encontrados = indexar_arquivos(pasta_temp_path)
        copiar_arquivos_necessarios(arquivos_encontrados)

    print("\nDownload e organização concluídos com sucesso.")
    print(f"Datasets disponíveis em: {DATASET_DIR}")


if __name__ == "__main__":
    main()