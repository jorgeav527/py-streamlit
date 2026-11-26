# Streamlit para Data Analytics — Cibertec

Laboratorio interactivo para aprender Streamlit desde cero, pensado para
estudiantes de analítica de datos. La app es **multipágina** y cada sección
muestra componentes de Streamlit **en vivo**, con código Python sencillo.

## ¿Qué vas a aprender?

- Crear interfaces web con Python puro.
- Capturar datos con formularios y widgets.
- Mostrar tablas, métricas y gráficos (Matplotlib y Altair).
- Usar estado de sesión, caché, cámara/audio, diálogos y chat.
- Organizar una app real en varias páginas.

## Requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Instalación

```bash
uv sync
```

## Cómo ejecutar

```bash
uv run streamlit run src/py_streamlit/main.py
```

> Ejecuta siempre desde la **raíz del proyecto**. El dataset se lee con la ruta
> relativa `data/gapminder.csv`.

Streamlit abrirá la app en `http://localhost:8501`.

## Estructura del proyecto

```
py-streamlit/
├── pyproject.toml
├── README.md
├── .streamlit/config.toml          # tema y preferencias
├── data/
│   └── gapminder.csv               # dataset de ejemplo
└── src/py_streamlit/
    ├── main.py                     # punto de entrada (st.navigation)
    ├── data.py                     # load_gapminder()
    └── sections/
        ├── inicio.py               # página Inicio (2 tabs)
        ├── texto.py                # tab Básicas y métricas
        ├── widgets.py              # tab Formularios
        ├── avanzado.py             # página Avanzado
        └── analisis.py             # página Análisis
```

## Recorrido por la app

### 🏠 Inicio

Tiene dos pestañas:

- **🧱 Básicas y métricas**: títulos, Markdown, `st.code`, `st.json`, LaTeX,
  insignias, alertas (`info`, `success`, `warning`, `error`), KPIs con
  `st.metric`, columnas, contenedores, desplegables y multimedia.
- **🧾 Formularios**: `text_input`, `number_input`, `selectbox`, `multiselect`,
  `radio`, `pills`, `segmented_control`, `slider`, `select_slider`, `checkbox`,
  `toggle`, `date_input`, `time_input`, `color_picker`, `st.form`, botones,
  descargas y enlaces.

### ✨ Avanzado

- `st.camera_input` y `st.audio_input`: captura de foto y voz.
- `st.session_state`: estado que sobrevive a los reruns.
- `@st.cache_data`: reutilizar cálculos costosos.
- Feedback: `st.spinner`, `st.progress`, `st.status`, `st.skeleton`, `st.toast`.
- `@st.fragment(run_every=...)`: actualizar solo una parte de la página.
- `@st.dialog`: ventanas modales.
- `st.chat_message` + `st.chat_input`: interfaces de chat.
- `st.query_params`: guardar estado en la URL.
- `st.mermaid_chart`, `st.echarts_chart`: diagramas y gráficos extra.

### 📊 Análisis

Flujo típico de análisis:

1. `st.file_uploader` para subir tu propio CSV (o usar `data/gapminder.csv`).
2. Revisar el resumen del dataset con `df.info()`. Como `df.info()` imprime en
   consola, se captura con `io.StringIO` y se muestra con `st.text`.
3. Graficar con Matplotlib (`st.pyplot`) para la evolución de la esperanza de
   vida y con Altair (`st.altair_chart`) para el gráfico interactivo.

## Cheatsheet rápido

| Necesito… | Componente |
|---|---|
| Escribir texto | `st.write`, `st.markdown`, `st.title`, `st.caption` |
| Mostrar código / datos | `st.code`, `st.json`, `st.dataframe`, `st.table` |
| Alertas | `st.info`, `st.success`, `st.warning`, `st.error` |
| KPIs | `st.metric` |
| Ordenar el layout | `st.columns`, `st.container`, `st.expander`, `st.tabs`, `st.sidebar` |
| Pedir datos | `st.text_input`, `st.number_input`, `st.selectbox`, `st.slider`, `st.file_uploader` |
| Agrupar un formulario | `st.form` + `st.form_submit_button` |
| Graficar | `st.pyplot`, `st.altair_chart`, `st.line_chart`, `st.bar_chart` |
| Mostrar progreso | `st.spinner`, `st.progress`, `st.status` |
| Guardar estado | `st.session_state` |
| Acelerar cargas | `@st.cache_data` |
| Navegar entre páginas | `st.navigation`, `st.Page`, `st.switch_page` |

## Cómo agregar tu propio componente

1. Abre la sección/página que corresponda en `src/py_streamlit/sections/`.
2. Agrega el título, la descripción y el componente con Streamlit directo:

```python
st.subheader("Mi componente")
st.caption("Explicación breve de qué hace.")
st.write("¡Hola desde mi componente!")
```

## Nota sobre recursos externos

La sección de multimedia (dentro de Inicio) usa imágenes, audio y video de
internet (Unsplash, SoundHelix y YouTube). Necesitas conexión para verlos; el
resto de la app funciona sin internet.

## Solución de problemas

- **`FileNotFoundError: data/gapminder.csv`** → ejecuta la app desde la raíz del
  proyecto.
- **`ModuleNotFoundError: py_streamlit`** → ejecuta `uv sync` y usa
  `uv run streamlit run ...`.
- **La app no se actualiza** → revisa que no haya un error en la consola; guarda
  el archivo y Streamlit recargará.
- **Los datos cambiaron solos** → `@st.cache_data` guarda resultados; usa el
  menú «Clear cache» o cambia los argumentos de la función.
- **Aviso de `use_container_width` deprecado** → usa `width="stretch"`.

## Recursos

- Documentación: <https://docs.streamlit.io>
- Cheatsheet: <https://docs.streamlit.io/develop/quick-reference/cheat-sheet>
- Galería de apps: <https://streamlit.io/gallery>
