"""Funções de limpeza de dados.

Autora: ana-branch
"""


def remover_duplicatas(df):
    """Remove linhas duplicadas do DataFrame."""
    antes = len(df)
    df = df.drop_duplicates()
    depois = len(df)
    print(f"Removidas {antes - depois} duplicatas.")
    return df


def tratar_nulos(df, estrategia='mediana'):
    """Preenche valores ausentes em colunas numéricas."""
    num_cols = df.select_dtypes(include='number').columns
    if estrategia == 'mediana':
        df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    elif estrategia == 'media':
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    return df
