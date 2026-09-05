# Projeto DS Colaborativo

Projeto de aprendizado de Git com múltiplos colaboradores.

## Colaboradores
- Prof-Saulo-Santos (líder)
- ana-branch
- joao-branch

## Estrutura
from src.modelos import avaliar_modelos
import pandas as pd

X = pd.read_csv('data/processed/features.csv')
y = pd.read_csv('data/processed/target.csv').squeeze()
resultados = avaliar_modelos(X, y)
eof
