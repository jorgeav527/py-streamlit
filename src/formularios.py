import streamlit as st


def render():
    st.header("🕹️ Formularios con Widgets (interactividad)")

    st.subheader("Entradas de texto y números")
    nombre = st.text_input("Nombre", placeholder="Escribe tu nombre")
    edad = st.number_input("Edad", min_value=18, max_value=100, value=35)
    notas = st.text_area("Notas Aqui", placeholder="Observaciones...")
    st.write(f"Nombre: {nombre} | Edad: {edad} | Notas: {notas}")

    st.subheader("Selección de opciones")
    pais = st.selectbox("País", ["Perú", "México", "España", "Japón"])
    lenguajes = st.multiselect(
        "Lenguajes",
        ["Python", "R", "SQL", "Julia"],
        default=["Python"],
    )
    color = st.radio("Color", ["Rojo", "Verde", "Azul"], horizontal=True)
    nivel = st.pills(
        "Nivel",
        ["Básico", "Intermedio", "Avanzado"],
        default="Intermedio",
    )
    vista = st.segmented_control("Vista", ["Tabla", "Gráfico"], default="Tabla")
    st.json(
        {
            "País": pais,
            "Lenguajes": lenguajes,
            "Color": color,
            "Nivel": nivel,
            "Vista": vista,
        }
    )

    st.subheader("Sliders")
    rango_edad = st.slider("Rango de edad", 18, 100, (25, 45))
    experiencia = st.select_slider(
        "Experiencia",
        ["Novato", "Intermedio", "Avanzado", "Ninja"],
        value="Intermedio",
    )
    st.write(f"Rango: {rango_edad} | Experiencia: {experiencia}")

    st.subheader("Booleanos, fechas y colores")
    c1, c2 = st.columns(2)
    acepto = c1.checkbox("Acepto los términos", value=True)
    activo = c2.toggle("Modo oscuro", value=False)
    c3, c4 = st.columns(2)
    fecha = c3.date_input("Fecha del análisis")
    hora = c4.time_input("Hora de corte")
    color_marca = st.color_picker("Color de la marca", "#4F46E5")
    st.write(
        f"Acepto: {acepto} | Activo: {activo} | Fecha: {fecha} | "
        f"Hora: {hora} | Color: {color_marca}"
    )

    st.subheader("Formularios")
    with st.form("demo_form"):
        f_nombre = st.text_input("Nombre")
        f_edad = st.slider("Edad", 18, 99, 25)
        enviado = st.form_submit_button("Enviar")
    if enviado:
        st.success(f"Registrado: {f_nombre} ({f_edad} años)")

    st.subheader("Botones y descargas")
    if st.button("Saludar"):
        st.write("¡Hola, analista!")
    st.download_button(
        "Descargar CSV",
        data="a,b\n1,2\n",
        file_name="ejemplo.csv",
        mime="text/csv",
    )
