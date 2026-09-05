"""Funções de modelagem ML.

Autor: joao-branch
Branch: feature/joao-modelos
"""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np


def criar_pipeline_lr():
    """Cria pipeline com Logistic Regression."""
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model',  LogisticRegression(max_iter=1000, random_state=42))
    ])


def criar_pipeline_rf():
    """Cria pipeline com Random Forest."""
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model',  RandomForestClassifier(n_estimators=100, random_state=42))
    ])


def avaliar_modelos(X, y):
    """Compara LR e RF com cross-validation."""
    modelos = {
        'Logistic Regression': criar_pipeline_lr(),
        'Random Forest':       criar_pipeline_rf(),
    }
    resultados = {}
    for nome, pipe in modelos.items():
        scores = cross_val_score(pipe, X, y, cv=5, scoring='f1')
        resultados[nome] = {'media': scores.mean(), 'std': scores.std()}
        print(f"{nome}: {scores.mean():.4f} ± {scores.std():.4f}")
    return resultados
