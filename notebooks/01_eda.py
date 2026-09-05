"""Análise Exploratória de Dados.

Autora: ana-branch
Branch: feature/ana-eda
"""
import pandas as pd
import numpy as np
import sys
sys.path.append('../src')
from limpeza_dados import remover_duplicatas, tratar_nulos
from visualizacoes import plotar_distribuicao, plotar_correlacao


def executar_eda(caminho_csv):
    """Pipeline completo de EDA."""
    df = pd.read_csv(caminho_csv)
    print(f"Shape original: {df.shape}")

    df = remover_duplicatas(df)
    df = tratar_nulos(df)

    print(f"Shape após limpeza: {df.shape}")
    print(df.describe())

    print(df) # print mostrando quantas linhas foram processadas.

    return df
