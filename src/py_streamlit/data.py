"""Carga del dataset de ejemplo."""

import pandas as pd


def load_gapminder() -> pd.DataFrame:
    """Lee `data/gapminder.csv` (ejecuta la app desde la raíz del proyecto)."""
    return pd.read_csv("data/gapminder.csv")
