"""Página de inicio: una app multipágina con dos pestañas."""

import streamlit as st

from . import texto, widgets

DOCS_URL = "https://docs.streamlit.io"
CHEATSHEET_URL = "https://docs.streamlit.io/develop/quick-reference/cheat-sheet"


def render() -> None:
    st.title("🚀 Streamlit para Data Analytics")
    st.caption("Cibertec · Laboratorio interactivo de componentes")

    c1, c2, c3 = st.columns([1, 1, 2])
    c1.link_button("📚 Documentación", DOCS_URL, width="stretch")
    c2.link_button("🧪 Cheatsheet", CHEATSHEET_URL, width="stretch")
    c3.caption(
        "Usa el menú de la izquierda para cambiar de página. Cada sección "
        "muestra componentes de Streamlit en vivo."
    )

    st.divider()

    tab_basicas, tab_formularios = st.tabs(
        ["🧱 Básicas y métricas", "🧾 Formularios"]
    )

    with tab_basicas:
        texto.render()
    with tab_formularios:
        widgets.render()
