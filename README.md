# Streamlit para Data Analytics — Cibertec

Laboratorio interactivo para aprender **Streamlit** desde cero, pensado para
estudiantes de analítica de datos. La app es **multipágina** y cada sección
muestra componentes de Streamlit **en vivo**, con código Python sencillo y
directo (sin helpers ni `__init__.py`).

## ¿Qué incluye?

- **Home** con dos pestañas: componentes básicos/métricas y formularios.
- **Análisis**: subir un CSV, revisar el dataset y graficar con Matplotlib y
  Altair.
- **Extra**: cámara, audio, estado de sesión, caché, feedback, modales,
  diagramas y chat.

## Requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Instalación y ejecución

```bash
uv sync
uv run streamlit run src/main.py
```

> Ejecuta siempre desde la **raíz del proyecto**: el dataset se lee con la ruta
> relativa `data/gapminder.csv`.

Streamlit abrirá la app en `http://localhost:8501`.

## Estructura del proyecto

```
py-streamlit/
├── .streamlit/
│   └── config.toml        # tema y telemetría
├── data/
│   └── gapminder.csv      # dataset de ejemplo
├── src/
│   ├── main.py            # entrada: st.navigation + st.Page
│   ├── home_page.py       # página Home (2 tabs)
│   ├── texto.py           # tab Básicas y métricas
│   ├── formularios.py     # tab Formularios
│   ├── analisis_page.py   # página Análisis (datos + gráficos)
│   └── extra_page.py      # página Extra (funciones avanzadas)
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

Cada módulo de página o sección (`home_page`, `texto`, `formularios`,
`analisis_page`, `extra_page`) es un archivo independiente que expone una
función `render()`. No hay paquetes ni `__init__.py`: `main.py` importa los
archivos directamente (`import home_page`, `import analisis_page`,
`import extra_page`).

## Cómo funciona la navegación

`src/main.py` configura la página y registra las páginas con `st.Page`:

```python
import streamlit as st

def app():
    st.set_page_config(page_title="Cibertec - Streamlit Lab", page_icon="📊", layout="wide")

    import analisis_page
    import extra_page
    import home_page

    paginas = [
        st.Page(home_page.render, title="Home", icon="🏠", url_path="home", default=True),
        st.Page(analisis_page.render, title="Análisis", icon="📊", url_path="analisis"),
        st.Page(extra_page.render, title="Extra", icon="✨", url_path="extra"),
    ]
    st.navigation(paginas).run()

if __name__ == "__main__":
    app()
```

## Recorrido por la app

### 🏠 Home (`home_page.py`)

Página de bienvenida con enlaces a la documentación y al cheatsheet. Tiene dos
pestañas:

#### 🧱 Básicas y métricas (`texto.py`)

- Títulos y Markdown (`st.title`, `st.header`, `st.subheader`, `st.markdown`).
- Código (`st.code`) y JSON (`st.json`), incluida una función de limpieza
  `clean_data`.
- LaTeX, insignias (`st.badge`) y HTML (`st.html`).
- Alertas: `st.info`, `st.success`, `st.warning`, `st.error`.
- KPIs con `st.metric` en columnas.
- Layout: `st.container(border=True)`, `st.columns(..., border=True)` con
  `with` para ver el ancho 2/3 vs 1/3, `st.expander` y `st.popover`.
- Multimedia: `st.image`, `st.video` y `st.audio`.

#### 🧾 Formularios (`formularios.py`)

- Entradas: `st.text_input`, `st.number_input`, `st.text_area`.
- Selección: `st.selectbox`, `st.multiselect`, `st.radio`, `st.pills`,
  `st.segmented_control`; el resultado se muestra con `st.json`.
- Valores: `st.slider`, `st.select_slider`.
- Booleanos, fechas y colores: `st.checkbox`, `st.toggle`, `st.date_input`,
  `st.time_input`, `st.color_picker`.
- Formularios: `st.form` + `st.form_submit_button`.
- Acciones: `st.button` y `st.download_button`.

### 📊 Análisis (`analisis_page.py`)

Flujo típico de un analista: **cargar → explorar → graficar**.

1. **Carga de datos** (`cargar_datos`): `st.file_uploader` para subir un CSV; si
   no se sube nada, usa `data/gapminder.csv`. Muestra 5 filas con `st.dataframe`.
2. **Resumen del dataset**: `df.info()` se captura con `io.StringIO` y se muestra
   con `st.text` (porque `df.info()` imprime en consola, no en la página).
3. **Gráfico estático** (`grafico_matplotlib`): un `st.multiselect` elige los
   países (por defecto los 4 primeros) y se dibuja la evolución de la esperanza
   de vida con Matplotlib (`st.pyplot`).
4. **Gráfico interactivo** (`grafico_altair`): un `st.select_slider` elige el año
   y se muestra un scatter de PIB per cápita vs esperanza de vida para **todos
   los países** de ese año, coloreado por continente y con tooltips
   (`st.altair_chart`).

Columnas esperadas del CSV:

```
country, year, pop, continent, lifeExp, gdpPercap
```

### ✨ Extra (`extra_page.py`)

- **Captura de medios**: `st.camera_input` y `st.audio_input`; la foto grabada se
  muestra con `st.image` y el audio con `st.audio`.
- **Estado de sesión**: contador con `st.session_state`.
- **Caché**: `@st.cache_data` sobre un cálculo costoso simulado.
- **Feedback**: `st.spinner`, `st.progress`, `st.status`, `st.toast` y
  `st.skeleton`.
- **Diálogos**: `@st.dialog` para abrir una ventana modal.
- **Diagramas**: `st.mermaid_chart`.
- **Chat**: `st.chat_message` + `st.chat_input`, guardando el historial en
  `st.session_state` y usando `st.rerun()` para repintar.

## Dataset de ejemplo

`data/gapminder.csv`:

- **1704 filas**, **6 columnas**.
- **142 países**, **5 continentes**.
- Años **1952–2007** (12 cortes cada 5 años).
- Columnas: `country`, `year`, `pop`, `continent`, `lifeExp`, `gdpPercap`.

Es el dataset clásico de Gapminder: población, continente, esperanza de vida y
PIB per cápita por país y año.

## Cheatsheet rápido

| Necesito… | Componente | Dónde se ve |
|---|---|---|
| Texto y títulos | `st.title`, `st.header`, `st.markdown`, `st.caption` | Home › Básicas |
| Código / JSON | `st.code`, `st.json` | Home › Básicas |
| Alertas | `st.info`, `st.success`, `st.warning`, `st.error` | Home › Básicas |
| KPIs | `st.metric` | Home › Básicas / Extra |
| Layout | `st.columns`, `st.container`, `st.tabs`, `st.expander`, `st.popover` | Home |
| Imagen / audio / video | `st.image`, `st.audio`, `st.video` | Home › Básicas |
| Pedir texto/números | `st.text_input`, `st.number_input`, `st.text_area` | Home › Formularios |
| Elegir opciones | `st.selectbox`, `st.multiselect`, `st.radio`, `st.pills`, `st.segmented_control` | Home › Formularios |
| Sliders | `st.slider`, `st.select_slider` | Home › Formularios |
| Booleanos / fechas / colores | `st.checkbox`, `st.toggle`, `st.date_input`, `st.time_input`, `st.color_picker` | Home › Formularios |
| Agrupar un formulario | `st.form` + `st.form_submit_button` | Home › Formularios |
| Botones / descargas | `st.button`, `st.download_button` | Home › Formularios |
| Subir un CSV | `st.file_uploader` | Análisis |
| Tablas | `st.dataframe` | Análisis |
| Gráfico estático | Matplotlib + `st.pyplot` | Análisis |
| Gráfico interactivo | Altair + `st.altair_chart` | Análisis |
| Cámara / micrófono | `st.camera_input`, `st.audio_input` | Extra |
| Guardar estado | `st.session_state` | Extra |
| Acelerar cálculos | `@st.cache_data` | Extra |
| Progreso / avisos | `st.spinner`, `st.progress`, `st.status`, `st.toast`, `st.skeleton` | Extra |
| Modales | `@st.dialog` | Extra |
| Diagramas | `st.mermaid_chart` | Extra |
| Chat | `st.chat_message`, `st.chat_input` | Extra |
| Navegación | `st.navigation`, `st.Page` | `main.py` |

## Cómo agregar tu propio componente

1. Abre el archivo que corresponda en `src/` (`texto.py`, `formularios.py`,
   `analisis_page.py`, `extra_page.py`).
2. Agrega el título, la descripción y el componente con Streamlit directo:

```python
st.subheader("Mi componente")
st.caption("Explicación breve de qué hace.")
st.write("¡Hola desde mi componente!")
```

### Agregar una página nueva

1. Crea `src/mi_page.py` con una función `render()`:

```python
import streamlit as st

def render():
    st.header("Mi página")
    st.write("Contenido de mi página.")
```

2. Regístrala en `src/main.py`:

```python
import mi_page

paginas = [
    # ...
    st.Page(mi_page.render, title="Mi página", icon="📄", url_path="mi-page"),
]
```

## Notas y limitaciones

- La ruta `data/gapminder.csv` es **relativa**: ejecuta desde la raíz.
- El CSV que subas debe tener las mismas columnas que Gapminder
  (`country`, `year`, `pop`, `continent`, `lifeExp`, `gdpPercap`). No hay
  validación: si faltan columnas, los gráficos fallarán con `KeyError`.
- `df.sample(5)` muestra filas distintas en cada rerun (útil para explorar, pero
  cambia al interactuar).
- La sección de multimedia usa imágenes, audio y video de internet (Unsplash,
  SoundHelix y YouTube); necesitas conexión para verlos.
- No hay pruebas automatizadas; la verificación es manual abriendo la app.

## Solución de problemas

- **`FileNotFoundError: data/gapminder.csv`** → ejecuta la app desde la raíz del
  proyecto.
- **`ModuleNotFoundError: streamlit`** (o falta Matplotlib/Altair) → ejecuta
  `uv sync`.
- **`KeyError: 'country'` (o similar)** → el CSV subido no tiene el esquema de
  Gapminder.
- **La app no se actualiza** → revisa la consola; guarda el archivo y Streamlit
  recargará.
- **Aviso de `use_container_width` deprecado** → usa `width="stretch"`.

## Recursos

- Documentación: <https://docs.streamlit.io>
- Cheatsheet: <https://docs.streamlit.io/develop/quick-reference/cheat-sheet>
- Galería de apps: <https://streamlit.io/gallery>
- Dataset Gapminder: <https://www.gapminder.org/data/>
