import os
import json
import joblib
import pandas as pd
from datetime import datetime

PASTA_MODELS = "models"
ARQUIVO_SAIDA = "resultado_pkls.txt"


def escrever(linha=""):
    print(linha)
    with open(ARQUIVO_SAIDA, "a", encoding="utf-8") as f:
        f.write(str(linha) + "\n")


def separar(titulo):
    escrever("\n" + "=" * 80)
    escrever(titulo)
    escrever("=" * 80)


def mostrar_objeto(nome_arquivo, objeto):
    escrever(f"Arquivo: {nome_arquivo}")
    escrever(f"Tipo do objeto: {type(objeto)}")

    if isinstance(objeto, (list, tuple, pd.Index)):
        escrever(f"Quantidade de itens: {len(objeto)}")
        escrever("\nConteúdo:")

        for i, item in enumerate(objeto, start=1):
            escrever(f"{i}. {item}")

    elif isinstance(objeto, dict):
        escrever(f"Quantidade de chaves: {len(objeto)}")
        escrever("\nConteúdo:")

        for chave, valor in objeto.items():
            escrever(f"{chave}: {valor}")

    elif isinstance(objeto, pd.DataFrame):
        escrever(f"Formato: {objeto.shape}")
        escrever("\nColunas:")

        for i, coluna in enumerate(objeto.columns, start=1):
            escrever(f"{i}. {coluna}")

        escrever("\nPrimeiras linhas:")
        escrever(objeto.head().to_string())

    else:
        escrever("\nRepresentação do objeto:")
        escrever(objeto)

        if hasattr(objeto, "get_params"):
            escrever("\nParâmetros do modelo:")
            for chave, valor in objeto.get_params().items():
                escrever(f"{chave}: {valor}")

        if hasattr(objeto, "feature_names_in_"):
            escrever("\nFeatures detectadas dentro do modelo:")
            for i, coluna in enumerate(objeto.feature_names_in_, start=1):
                escrever(f"{i}. {coluna}")

        if hasattr(objeto, "n_features_in_"):
            escrever(f"\nQuantidade de features esperadas pelo modelo: {objeto.n_features_in_}")

        if hasattr(objeto, "classes_"):
            escrever("\nClasses do modelo:")
            escrever(objeto.classes_)


def main():
    # Limpa o arquivo antigo antes de começar
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DOS ARQUIVOS PKL/JSON\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 80 + "\n")

    if not os.path.exists(PASTA_MODELS):
        escrever(f"Erro: pasta '{PASTA_MODELS}' não encontrada.")
        escrever("Execute este script dentro da pasta Explicação-geral.")
        return

    arquivos = os.listdir(PASTA_MODELS)

    escrever(f"Pasta analisada: {PASTA_MODELS}")
    escrever(f"Arquivo de saída criado: {ARQUIVO_SAIDA}")
    escrever(f"Quantidade de arquivos encontrados: {len(arquivos)}")

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_MODELS, arquivo)

        if arquivo.endswith(".pkl"):
            separar(f"INSPECIONANDO PKL: {arquivo}")

            try:
                objeto = joblib.load(caminho)
                mostrar_objeto(arquivo, objeto)

            except Exception as erro:
                escrever(f"Erro ao abrir {arquivo}: {erro}")

        elif arquivo.endswith(".json"):
            separar(f"INSPECIONANDO JSON: {arquivo}")

            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    dados = json.load(f)

                escrever(json.dumps(dados, indent=4, ensure_ascii=False))

            except Exception as erro:
                escrever(f"Erro ao abrir {arquivo}: {erro}")

    separar("PROCESSO FINALIZADO")
    escrever(f"O relatório foi salvo em: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()