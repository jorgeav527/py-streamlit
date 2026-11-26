import time

import streamlit as st


@st.cache_data(show_spinner=False)
def operacion_costosa(n):
    """Simula un cálculo pesado (1 segundo) para demostrar la caché."""
    time.sleep(1)
    return sum(i * i for i in range(n))


@st.dialog("📄 Detalles del curso")
def modal():
    st.write("**Streamlit para Data Analytics** — Cibertec")
    st.write("Duración: 4 módulos · Nivel: básico-intermedio")
    st.write("Puedes cerrar esta ventana con la tecla `Esc` o el botón de abajo.")
    if st.button("Cerrar"):
        st.rerun()


def render():
    st.header("✨ Extra")
    st.write(
        "Aquí están las piezas que convierten una demo en una **app real**: "
        "captura de medios, estado, caché, feedback, diálogos y chat."
    )

    st.subheader("Captura de medios")
    c1, c2 = st.columns(2)
    foto = c1.camera_input("Toma una foto")
    audio = c2.audio_input("Graba una nota de voz")
    if foto is not None:
        st.image(foto, caption="Foto capturada", width=240)
    if audio is not None:
        st.audio(audio)

    st.subheader("Estado de sesión")
    if "contador_demo" not in st.session_state:
        st.session_state.contador_demo = 0
    c1, c2, c3 = st.columns([1, 1, 2])
    if c1.button("➕ Sumar"):
        st.session_state.contador_demo += 1
    if c2.button("➖ Restar"):
        st.session_state.contador_demo -= 1
    c3.metric("Contador", st.session_state.contador_demo)

    st.subheader("Caché de cálculos")
    if st.button("Ejecutar cálculo (5 millones)", key="btn_cache"):
        inicio = time.perf_counter()
        resultado = operacion_costosa(5_000_000)
        st.success(f"Resultado: {resultado:,}")
        st.write(f"⏱️ Tiempo: {time.perf_counter() - inicio:.3f}s")

    st.subheader("Feedback: spinner, progreso y estado")
    if st.button("Iniciar animación", key="btn_feedback"):
        with st.spinner("Calculando..."):
            time.sleep(0.5)
        barra = st.progress(0, text="Procesando filas...")
        for i in range(100):
            barra.progress(i + 1, text=f"Procesando... {i + 1}%")
            time.sleep(0.01)
        with st.status("Paso a paso", expanded=True) as estado:
            st.write("Leyendo datos...")
            time.sleep(0.4)
            st.write("Limpiando datos...")
            time.sleep(0.4)
            estado.update(label="¡Listo!", state="complete")
        st.toast("✅ Proceso finalizado", icon="🎉")
    with st.skeleton(height=60):
        time.sleep(0.4)

    st.subheader("Diálogos (modales)")
    if st.button("Abrir diálogo", key="btn_dialog"):
        modal()

    st.subheader("Otros gráficos: Mermaid y ECharts")
    st.caption("Diagramas de flujo y gráficos de ECharts sin librerías extra.")
    st.mermaid_chart(
        "flowchart LR\n"
        "  A[Datos] --> B[Limpieza]\n"
        "  B --> C[Análisis]\n"
        "  C --> D[Visualización]"
    )

    st.subheader("Chat")
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

    for m in st.session_state.mensajes:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if prompt := st.chat_input("Escribe un mensaje..."):
        st.session_state.mensajes.append({"role": "user", "content": prompt})
        st.session_state.mensajes.append(
            {"role": "assistant", "content": f"Recibí: {prompt}"}
        )
        st.rerun()
