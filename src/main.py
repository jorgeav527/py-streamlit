import streamlit as st


def app():
    st.set_page_config(
        page_title="Cibertec - Streamlit Lab",
        page_icon="📊",
        layout="wide",
    )

    import analisis_page
    import extra_page
    import home_page

    paginas = [
        st.Page(
            home_page.render,
            title="Home",
            icon="🏠",
            url_path="home",
            default=True,
        ),
        st.Page(analisis_page.render, title="Análisis", icon="📊", url_path="analisis"),
        st.Page(extra_page.render, title="Extra", icon="✨", url_path="extra"),
    ]
    st.navigation(paginas).run()


if __name__ == "__main__":
    app()
