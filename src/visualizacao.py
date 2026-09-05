
"""Funções de visualização de dados.

Autor: joao-branch
"""
import matplotlib.pyplot as plt
import seaborn as sns


def plotar_distribuicao(df, coluna, titulo=None):
    """Plota histograma com KDE para uma coluna numérica."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[coluna], kde=True, ax=ax, color='steelblue')
    ax.set_title(titulo or f'Distribuição de {coluna}')
    plt.tight_layout()
    return fig


def plotar_correlacao(df):
    """Plota heatmap de correlação entre colunas numéricas."""
    corr = df.select_dtypes(include='number').corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    ax.set_title('Matriz de Correlação')
    plt.tight_layout()
    return fig
