"""Página «Análisis»: carga de datos y gráficos."""

import io

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from ..data import load_gapminder

PAISES_DEFECTO = ["Mexico", "Spain", "Japan"]
COLUMNAS_NECESARIAS = ["country", "year", "pop", "continent", "lifeExp", "gdpPercap"]


def _grafico_matplotlib(data: pd.DataFrame, paises: list[str]) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 5))
    for pais in paises:
        df_pais = data[data["country"] == pais]
        ax.plot(
            df_pais["year"],
            df_pais["lifeExp"],
            marker="o",
            markersize=4,
            linewidth=2,
            label=pais,
        )
    ax.set_title(
        "Evolución de la Esperanza de Vida", fontsize=16, pad=20, fontweight="bold"
    )
    ax.set_xlabel("Año", fontsize=12)
    ax.set_ylabel("Años de Vida", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(title="Países", frameon=False, loc="upper left")
    return fig


def _cargar_datos() -> pd.DataFrame:
    st.subheader("Carga de datos")
    st.caption("Sube tu propio CSV o usa el dataset de ejemplo `data/gapminder.csv`.")
    archivo = st.file_uploader(
        "Sube tu propio dataset (CSV)", type="csv", key="analisis_upload"
    )

    if archivo is not None:
        df = pd.read_csv(archivo)
        faltantes = [c for c in COLUMNAS_NECESARIAS if c not in df.columns]
        if faltantes:
            st.warning(
                f"El archivo no tiene las columnas {faltantes}. "
                "Usando el dataset de ejemplo."
            )
            df = load_gapminder()
        else:
            st.success(f"Usando tu archivo: {archivo.name}")
    else:
        df = load_gapminder()
        st.info("Usando el dataset de ejemplo `data/gapminder.csv`.")

    st.dataframe(df.head(), width="stretch")
    return df


def render() -> None:
    st.header("📊 Análisis de datos")
    st.write(
        "El flujo típico de un analista: **cargar → explorar → graficar**. "
        "Puedes subir tu CSV o trabajar con el dataset de ejemplo."
    )

    df = _cargar_datos()

    st.subheader("Resumen del dataset")
    st.caption("`df.info()` muestra columnas, tipos y valores no nulos.")
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    paises_grafico = [p for p in PAISES_DEFECTO if p in df["country"].unique()]
    if not paises_grafico:
        paises_grafico = list(df["country"].unique())[:3]

    st.subheader("Matplotlib")
    st.caption("Control total del gráfico y publicación con `st.pyplot`.")
    paises = st.multiselect(
        "Selecciona los países a comparar:",
        options=sorted(df["country"].unique()),
        default=paises_grafico,
        key="datos_paises",
    )
    if paises:
        fig = _grafico_matplotlib(df, paises)
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.warning("Selecciona al menos un país.")

    st.subheader("Altair (interactivo)")
    st.caption("Gráficos declarativos con zoom, tooltips y selección.")
    chart = (
        alt.Chart(df[df["year"] == df["year"].max()])
        .mark_circle(size=60)
        .encode(
            x=alt.X("gdpPercap:Q", title="PIB per cápita"),
            y=alt.Y("lifeExp:Q", title="Esperanza de vida"),
            color="continent:N",
            tooltip=["country", "continent", "lifeExp", "gdpPercap"],
        )
        .interactive()
    )
    st.altair_chart(chart, width="stretch")
