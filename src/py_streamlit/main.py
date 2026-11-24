"""Punto de entrada del laboratorio de Streamlit (Cibertec).

Se ejecuta con:

    uv run streamlit run src/py_streamlit/main.py

Ejecuta siempre desde la raíz del proyecto: `data/gapminder.csv` se lee con
una ruta relativa.
"""

import streamlit as st


def app() -> None:
    """Construye la app multipágina. La llama `streamlit run`."""
    st.set_page_config(
        page_title="Cibertec-208 · Streamlit Lab",
        page_icon="📊",
        layout="wide",
    )

    # Importamos aquí para que el paquete no ejecute UI al importarse.
    from py_streamlit.sections import analisis, avanzado, inicio

    paginas = [
        st.Page(
            inicio.render,
            title="Inicio",
            icon="🏠",
            url_path="inicio",
            default=True,
        ),
        st.Page(avanzado.render, title="Avanzado", icon="✨", url_path="avanzado"),
        st.Page(analisis.render, title="Análisis", icon="📊", url_path="analisis"),
    ]
    st.navigation(paginas).run()


if __name__ == "__main__":
    app()
