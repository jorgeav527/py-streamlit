"""Página «Avanzado»: captura de medios y funciones avanzadas."""

import time
from datetime import datetime

import streamlit as st


@st.cache_data(show_spinner=False)
def _operacion_costosa(n: int) -> int:
    """Simula un cálculo pesado (1 segundo) para demostrar la caché."""
    time.sleep(1)
    return sum(i * i for i in range(n))


@st.fragment(run_every=1)
def _reloj() -> None:
    """Fragmento que se actualiza solo cada segundo."""
    st.metric("Hora actual", datetime.now().strftime("%H:%M:%S"))


@st.dialog("📄 Detalles del curso")
def _dialogo() -> None:
    st.write("**Streamlit para Data Analytics** — Cibertec")
    st.write("Duración: 4 módulos · Nivel: básico-intermedio")
    st.write("Puedes cerrar esta ventana con la tecla `Esc` o el botón de abajo.")
    if st.button("Cerrar", key="cerrar_dialogo"):
        st.rerun()


def render() -> None:
    st.header("✨ Funciones avanzadas")
    st.write(
        "Aquí están las piezas que convierten una demo en una **app real**: "
        "captura de medios, estado, caché, feedback, diálogos y chat."
    )

    st.subheader("Captura de medios")
    st.caption("Toma una foto o graba audio directamente desde el navegador.")
    c1, c2 = st.columns(2)
    foto = c1.camera_input("Toma una foto", key="adv_camara")
    audio = c2.audio_input("Graba una nota de voz", key="adv_audio")
    if foto is not None:
        st.image(foto, caption="Foto capturada", width=240)
    if audio is not None:
        st.audio(audio)

    st.subheader("Estado de sesión")
    st.caption("`st.session_state` conserva valores entre reruns (por usuario).")
    if "contador_demo" not in st.session_state:
        st.session_state.contador_demo = 0
    c1, c2, c3 = st.columns([1, 1, 2])
    if c1.button("➕ Sumar", key="btn_sumar"):
        st.session_state.contador_demo += 1
    if c2.button("➖ Restar", key="btn_restar"):
        st.session_state.contador_demo -= 1
    c3.metric("Contador", st.session_state.contador_demo)

    st.subheader("Caché de cálculos")
    st.caption("La primera ejecución tarda; las siguientes usan el resultado guardado.")
    if st.button("Ejecutar cálculo (5 millones)", key="btn_cache"):
        inicio = time.perf_counter()
        resultado = _operacion_costosa(5_000_000)
        st.success(f"Resultado: {resultado:,}")
        st.write(f"⏱️ Tiempo: {time.perf_counter() - inicio:.3f}s")
    st.caption("Ejecútalo dos veces: la segunda será casi instantánea.")

    st.subheader("Feedback: spinner, progreso y estado")
    st.caption("Comunica qué está pasando cuando una tarea tarda.")
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

    st.subheader("Efectos festivos")
    st.caption("`st.balloons` y `st.snow` para celebrar hitos.")
    c1, c2 = st.columns(2)
    c1.button("🎈 Globos", on_click=st.balloons, key="btn_balloons")
    c2.button("❄️ Nieve", on_click=st.snow, key="btn_snow")

    st.subheader("Fragmentos y auto-refresh")
    st.caption("`@st.fragment(run_every=...)` actualiza solo una parte de la página.")
    _reloj()

    st.subheader("Diálogos (modales)")
    st.caption("`@st.dialog` muestra una ventana emergente con contenido propio.")
    if st.button("Abrir diálogo", key="btn_dialog"):
        _dialogo()

    st.subheader("Chat")
    st.caption("`st.chat_message` + `st.chat_input` para interfaces conversacionales.")
    if "mensajes_demo" not in st.session_state:
        st.session_state.mensajes_demo = []
    for m in st.session_state.mensajes_demo:
        with st.chat_message(m["role"]):
            st.write(m["content"])
    if prompt := st.chat_input("Escribe un mensaje...", key="chat_demo"):
        respuesta = f"Recibí: {prompt}"
        st.session_state.mensajes_demo.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.mensajes_demo.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)

    st.subheader("Parámetros de URL")
    st.caption("`st.query_params` guarda estado en la URL (útil para compartir vistas).")
    st.write("Parámetros actuales:", dict(st.query_params))
    nombre = st.text_input("Nombre para la URL", key="qp_nombre")
    if st.button("Guardar en URL", key="btn_qp"):
        st.query_params["nombre"] = nombre

    st.subheader("Otros gráficos: Mermaid y ECharts")
    st.caption("Diagramas de flujo y gráficos de ECharts sin librerías extra.")
    st.mermaid_chart(
        "flowchart LR\n"
        "  A[Datos] --> B[Limpieza]\n"
        "  B --> C[Análisis]\n"
        "  C --> D[Visualización]"
    )
    st.echarts_chart(
        {
            "xAxis": {"type": "category", "data": ["Ene", "Feb", "Mar"]},
            "yAxis": {"type": "value"},
            "series": [{"type": "bar", "data": [120, 200, 150]}],
        }
    )

    st.divider()
    st.caption(
        "ℹ️ `st.rerun()` vuelve a ejecutar la app desde el inicio y `st.stop()` "
        "detiene la ejecución en ese punto. Se usan para controlar el flujo."
    )
