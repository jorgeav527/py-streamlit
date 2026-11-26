import io

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def grafico_matplotlib(data, paises):
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


def grafico_altair(data, year):
    chart = (
        alt.Chart(data[data["year"] == year])
        .mark_circle(size=60)
        .encode(
            x=alt.X("gdpPercap:Q", title="PIB per cápita"),
            y=alt.Y("lifeExp:Q", title="Esperanza de vida"),
            color="continent:N",
            tooltip=["country", "continent", "lifeExp", "gdpPercap"],
        )
        .interactive()
    )
    return chart


def cargar_datos():
    st.subheader("Carga de datos")
    archivo = st.file_uploader("Sube tu propio dataset (CSV)", type="csv")

    if archivo is None:
        df = pd.read_csv("data/gapminder.csv")
        st.info("Usando el dataset de ejemplo `data/gapminder.csv`.")
    else:
        df = pd.read_csv(archivo)
        st.success(f"Usando tu archivo: {archivo.name}")

    st.dataframe(df.sample(5), width="stretch")
    return df


def render():
    st.header("📊 Análisis de datos")
    st.write(
        "El flujo típico de un analista: **cargar → explorar → graficar**. "
        "Puedes subir tu CSV o trabajar con el dataset de ejemplo."
    )

    df = cargar_datos()

    st.subheader("Resumen del dataset")
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.subheader("Grafico (estatico)")
    paises_disponibles = sorted(df["country"].unique())
    paises = st.multiselect(
        "Selecciona los países a comparar:",
        options=paises_disponibles,
        default=paises_disponibles[:4],
    )

    if paises:
        fig = grafico_matplotlib(df, paises)
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.warning("Selecciona al menos un país.")

    st.subheader("Gráfico (interactivo)")
    years = sorted(df["year"].unique())
    year = st.select_slider("Selecciona el año", options=years, value=years[-1])

    if year:
        chart = grafico_altair(df, year)
        st.altair_chart(chart, width="stretch")
    else:
        st.warning("Selecciona al menos el ultimo año.")
