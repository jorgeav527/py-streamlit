"""Página 1, pestaña «Formularios»: widgets e interactividad."""

import streamlit as st


def render() -> None:
    st.header("🕹️ Widgets e interactividad")
    st.write(
        "Cada widget devuelve un valor de Python. Cuando el usuario interactúa, "
        "Streamlit **vuelve a ejecutar** el script con el nuevo valor."
    )

    st.subheader("Entradas de texto y números")
    st.caption("Captura datos del usuario y muéstralos al instante.")
    nombre = st.text_input("Nombre", placeholder="Escribe tu nombre", key="w_nombre")
    edad = st.number_input("Edad", min_value=18, max_value=100, value=31, key="w_edad")
    notas = st.text_area("Notas", placeholder="Observaciones...", key="w_notas")
    st.write(f"Nombre: {nombre} | Edad: {edad} | Notas: {notas!r}")

    st.subheader("Selección de opciones")
    st.caption("`selectbox`, `multiselect`, `radio`, `pills` y `segmented_control`.")
    pais = st.selectbox("País", ["Perú", "México", "España", "Japón"], key="w_pais")
    lenguajes = st.multiselect(
        "Lenguajes",
        ["Python", "R", "SQL", "Julia"],
        default=["Python"],
        key="w_lenguajes",
    )
    color = st.radio("Color", ["Rojo", "Verde", "Azul"], horizontal=True, key="w_color")
    nivel = st.pills(
        "Nivel",
        ["Básico", "Intermedio", "Avanzado"],
        default="Intermedio",
        key="w_nivel",
    )
    vista = st.segmented_control(
        "Vista", ["Tabla", "Gráfico"], default="Tabla", key="w_vista"
    )
    st.write(
        f"País: {pais} | Lenguajes: {lenguajes} | Color: {color} | "
        f"Nivel: {nivel} | Vista: {vista}"
    )

    st.subheader("Sliders")
    st.caption("Valores numéricos y de rango con `slider` y `select_slider`.")
    rango_edad = st.slider("Rango de edad", 18, 100, (25, 45), key="w_rango")
    experiencia = st.select_slider(
        "Experiencia",
        ["Novato", "Intermedio", "Avanzado", "Ninja"],
        value="Intermedio",
        key="w_exp",
    )
    st.write(f"Rango: {rango_edad} | Experiencia: {experiencia}")

    st.subheader("Booleanos, fechas y colores")
    st.caption("`checkbox`, `toggle`, `date_input`, `time_input` y `color_picker`.")
    c1, c2 = st.columns(2)
    acepto = c1.checkbox("Acepto los términos", value=True, key="w_acepto")
    activo = c2.toggle("Modo oscuro", value=False, key="w_activo")
    c3, c4 = st.columns(2)
    fecha = c3.date_input("Fecha del análisis", key="w_fecha")
    hora = c4.time_input("Hora de corte", key="w_hora")
    color_marca = st.color_picker("Color de la marca", "#4F46E5", key="w_color_pick")
    st.write(
        f"Acepto: {acepto} | Activo: {activo} | Fecha: {fecha} | "
        f"Hora: {hora} | Color: {color_marca}"
    )

    st.subheader("Formularios")
    st.caption("Agrupa varios widgets y envía todo junto con un solo botón.")
    with st.form("demo_form"):
        f_nombre = st.text_input("Nombre", key="w_f_nombre")
        f_edad = st.slider("Edad", 18, 99, 25, key="w_f_edad")
        enviado = st.form_submit_button("Enviar")
    if enviado:
        st.success(f"Registrado: {f_nombre} ({f_edad} años)")

    st.subheader("Botones y descargas")
    st.caption("`button`, `download_button` y `link_button`.")
    if st.button("Saludar", key="w_btn_saludar"):
        st.write("¡Hola, analista!")
    st.download_button(
        "Descargar CSV",
        data="a,b\n1,2\n",
        file_name="ejemplo.csv",
        mime="text/csv",
        key="w_dl",
    )
    st.link_button("Documentación de Streamlit", "https://docs.streamlit.io")
