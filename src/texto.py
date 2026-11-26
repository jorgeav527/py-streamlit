import streamlit as st

UNSPLASH_IMG = "https://images.unsplash.com/photo-1518770660439-4636190af475"
AUDIO_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def render():
    st.header("📝 Texto, layout y multimedia")
    st.write(
        "Streamlit convierte Python en una interfaz web. Aquí tienes los "
        "componentes que usarás para **comunicar** resultados de un análisis."
    )

    st.subheader("Títulos y Markdown")
    st.title("Título principal")
    st.header("Encabezado")
    st.subheader("Subencabezado")
    st.markdown("**Negrita**, *cursiva*, `código` y [enlaces](https://streamlit.io)")

    st.subheader("Código y JSON")
    st.code(
        "df = pd.read_csv('data/gapminder.csv')", language="python", line_numbers=True
    )
    st.code(
        """def clean_data(df):
            df.columns = [col.lower().replace(" ", "_") for col in df.columns]
            return df.dropna()

        df = pd.read_csv("data/gapminder.csv")
        df_clean = clean_data(df)""",
        language="python",
        line_numbers=True,
    )
    st.json({"proyecto": "Streamlit Lab", "estado": "Activo", "version": 1.0})

    st.subheader("Fórmulas, etiquetas y HTML")
    st.latex(r"R^2 = 1 - \frac{SS_{res}}{SS_{tot}}")
    st.badge("Nuevo", icon=":material/new_releases:", color="green")
    st.html("<b>HTML</b> para personalizar el diseño.")

    st.subheader("Mensajes y alertas")
    st.info("ℹ️ Información: el dataset tiene 1.704 filas.")
    st.success("✅ Éxito: la limpieza terminó correctamente.")
    st.warning("⚠️ Advertencia: hay valores nulos en 'lifeExp'.")
    st.error("🚨 Error: no se pudo conectar a la base de datos.")

    st.subheader("Métricas (KPIs)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Registros", "1.704", "+12% vs ayer")
    c2.metric("Países", "142", "6 continentes")
    c3.metric("Tiempo de carga", "0.8s", "-0.2s", delta_color="inverse")

    st.subheader("Layout: columnas, contenedores y desplegables")
    with st.container(border=True):
        izq, der = st.columns([2, 1], border=True)
        with izq:
            st.markdown("**Columna ancha (2/3)**")
            st.write("Ocupa el doble de espacio que la derecha.")
        with der:
            st.markdown("**Columna angosta (1/3)**")
            st.write("Ocupa la mitad.")

    with st.expander("Más detalles"):
        st.write("Contenido oculto hasta que lo abras.")

    with st.popover("Abrir popover"):
        st.write("Un menú flotante.")

    st.subheader("Multimedia")
    mc1, mc2 = st.columns(2)
    mc1.image(UNSPLASH_IMG, caption="Análisis de hardware", width="stretch")
    mc2.video(VIDEO_URL)
    st.audio(AUDIO_URL, format="audio/mp3")
