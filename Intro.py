import base64
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Portafolio · Sthefany Diaz", page_icon="🗂️", layout="wide")

# ---------------------------------------------------------------
# ENLACES (si cambias o te falta alguno, edítalo solo aquí)
# ---------------------------------------------------------------
URL_PIZARRA = "https://6b7p75qtfygtgp58m46hbw.streamlit.app"
URL_IDIOMAS = "https://traductorbase-rosmngfudermkme6bicm6h.streamlit.app"
URL_DIARIO = "https://knt2gdcofwtaymfjpmyq6k.streamlit.app/"
URL_CUENTITO = "https://clonaci-nprofe-copy.streamlit.app/"
URL_CUADERNO = "https://answercontext-emdg7ncqwtbabsyeumy5vl.streamlit.app"
URL_CIBER = "https://drive.google.com/file/d/1zEXyzNpjACNDKYW2e1qM9he9B3kOXWRt/view?usp=drivesdk"
URL_SENAS = ""       # <- cuando termines el traductor de señas
URL_CURSO = "https://sites.google.com/view/aplicaciones-con-va"

# ---------------------------------------------------------------
# PROYECTOS
# cats = categorías del curso que cumple cada app
# tabs = en qué carpeta(s) aparece
# ---------------------------------------------------------------
PROYECTOS = [
    {
        "titulo": "Pizarra Tutor",
        "img": "pizarra.png",
        "url": URL_PIZARRA,
        "cats": ["Análisis de imagen", "Reconocimiento", "Generación de texto"],
        "tabs": ["Imagen", "Texto"],
        "texto": (
            "Escribes un ejercicio a mano en la pizarra y la IA lo lee, identifica la materia "
            "y lo explica paso a paso. En Concepto te enseña el tema detrás del ejercicio y en "
            "Práctica te propone uno parecido con su respuesta. Puedes cambiar materia, nivel "
            "de explicación, color y grosor de la tiza."
        ),
    },
    {
        "titulo": "Tutor de idiomas por voz",
        "img": "idiomas.png",
        "url": URL_IDIOMAS,
        "cats": ["Texto a voz", "Voz a texto", "Traducción"],
        "tabs": ["Voz", "Texto"],
        "texto": (
            "Eliges tu idioma y el que quieres practicar, escuchas una frase normal o lenta y la "
            "repites en voz alta. La app transcribe lo que dijiste y te muestra qué palabras te "
            "salieron bien y cuáles no, con un puntaje. Hay frases por nivel y tema, o puedes "
            "dictar la tuya."
        ),
    },
    {
        "titulo": "Mi Diario",
        "img": "diario.png",
        "url": URL_DIARIO,
        "cats": ["Análisis de datos", "Análisis de sentimiento", "RAG"],
        "tabs": ["Datos", "Texto"],
        "texto": (
            "Un diario para escribir cómo te sientes. Cada entrada queda en el historial, la app "
            "detecta el sentimiento y cambia el ánimo de la página, y arma una nube con tus "
            "palabras más usadas. También le puedes preguntar cosas y responde con base en lo "
            "que escribiste."
        ),
    },
    {
        "titulo": "Cuaderno digital",
        "img": "cuaderno.png",
        "url": URL_CUADERNO,
        "cats": ["RAG", "Análisis de imagen", "Generación de texto"],
        "tabs": ["Imagen", "Texto"],
        "texto": (
            "Subes la lectura en PDF y fotos del tablero o de tu cuaderno. La IA transcribe todo, "
            "lo une y con eso arma un resumen que puedes descargar, un quiz para repasar y "
            "responde preguntas sobre el material."
        ),
    },
    {
        "titulo": "Escuchemos un cuentito",
        "img": "cuentito.png",
        "url": URL_CUENTITO,
        "cats": ["Texto a voz", "Estructura en Streamlit"],
        "tabs": ["Voz"],
        "texto": (
            "De las primeras apps. Eliges una fábula o escribes lo que quieras y la app lo "
            "convierte en audio. Aquí aprendí cómo se organiza una app en Streamlit: título, "
            "imagen, columnas y secciones."
        ),
    },
    {
        "titulo": "Termómetro con emociones",
        "img": "ciber.png",
        "url": URL_CIBER,
        "boton": "Ver video",
        "cats": ["Sistema ciberfísico", "IoT con MQTT", "Datos en tiempo real"],
        "tabs": ["Datos"],
        "texto": (
            "Un sensor de temperatura y humedad simulado en Wokwi que envía sus lecturas por "
            "MQTT. La interfaz las recibe en tiempo real y una carita cambia de expresión "
            "según el clima: con frío extremo se pone brava."
        ),
    },
    {
        "titulo": "Traductor de señas",
        "img": "OIG5.jpg",
        "url": URL_SENAS,
        "cats": ["Entrenando modelos", "Visión en tiempo real"],
        "tabs": ["Imagen"],
        "pendiente": True,
        "texto": (
            "En construcción. Un modelo entrenado con fotos de gestos por letra para reconocer "
            "lengua de señas desde la cámara, en tiempo real."
        ),
    },
]

# Categorías del curso (las de la plantilla) y qué app las cubre
CATEGORIAS = [
    ("Texto a voz", ["Tutor de idiomas", "Cuentito"]),
    ("Voz a texto", ["Tutor de idiomas"]),
    ("Transcripción", ["Tutor de idiomas"]),
    ("Análisis de imagen", ["Pizarra Tutor", "Cuaderno digital"]),
    ("Reconocimiento", ["Pizarra Tutor"]),
    ("Generación en contexto (RAG)", ["Cuaderno digital", "Mi Diario"]),
    ("Análisis de datos", ["Mi Diario"]),
    ("Entrenando modelos", ["Traductor de señas (en proceso)"]),
    ("Sistema ciberfísico", ["Termómetro con emociones"]),
]

# ---------------------------------------------------------------
# ESTILO
# ---------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap');

:root{
  --pino:#163430; --pino-2:#0F2622; --salvia:#9CBE99; --salvia-2:#B4CFB0;
  --piedra:#CBC4BD; --papel:#E6E1DA; --menta:#D2EACC; --tinta:#13302A;
}
html, body, .stApp, .stMarkdown, .stMarkdown *, .stTabs [role="tab"] p{font-family:'Inter Tight', system-ui, sans-serif!important;}
.stApp{background:var(--pino);}
header[data-testid="stHeader"]{background:transparent;}
.block-container{max-width:1120px; padding-top:2.5rem; padding-bottom:4rem;}
section[data-testid="stSidebar"]{display:none;}

/* ---------- portada: carpetas apiladas ---------- */
.hero{position:relative; height:340px; margin:0 -1rem; overflow:hidden;}
.hoja{position:absolute; left:0; right:0; bottom:0; border-radius:6px 6px 0 0;}
.pest{position:absolute; top:-46px; height:52px; padding:0 34px; border-radius:16px 16px 0 0;
      display:flex; align-items:center; font-weight:600; font-size:15px; letter-spacing:.06em;
      color:var(--tinta);}
.h1{top:60px;  background:var(--piedra);}  .h1 .pest{right:12%; background:var(--piedra);}
.h2{top:120px; background:var(--salvia);}  .h2 .pest{left:30%;  background:var(--salvia);}
.h3{top:180px; background:var(--piedra);}  .h3 .pest{left:4%;   background:var(--piedra);}
.h4{top:240px; background:var(--salvia-2);}.h4 .pest{left:38%;  background:var(--salvia-2);}
.h5{top:290px; background:var(--pino);}
.h5 .pest{left:4%; background:var(--pino); color:var(--menta);}
.hoja::after{content:""; position:absolute; left:0; right:0; top:22px; height:1px; background:rgba(0,0,0,.08);}

.portada{display:grid; grid-template-columns:1fr auto; gap:2rem; align-items:start; margin-top:2rem;}
.portada .vol{text-align:right; color:#EEF3EC; font-weight:600; font-size:20px; line-height:1.25; letter-spacing:.02em;}
.titulo{font-size:clamp(72px, 13vw, 168px); line-height:.95; font-weight:400; color:var(--menta);
        letter-spacing:-.035em; margin:2.5rem 0 .6rem;}
.titulo em{font-style:italic; font-weight:400;}
.sub{color:#A9C3A6; font-size:18px; max-width:56ch; line-height:1.55; margin-bottom:3rem;}
.sub a{color:var(--menta);}
.sub strong{color:var(--menta); font-weight:600; font-size:22px;}

/* ---------- pestañas de Streamlit como carpetas ---------- */
.stTabs [role="tablist"]{gap:6px; border-bottom:none!important; box-shadow:none!important;
  padding-left:6px; overflow-x:auto; align-items:flex-end;}
.stTabs [role="tablist"]::after, .stTabs [role="tablist"]::before{display:none!important;}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"],
.stTabs .react-aria-SelectionIndicator{display:none!important;}
.stTabs [role="tab"]{
  height:48px; padding:0 26px!important; border-radius:16px 16px 0 0; background:var(--salvia);
  color:var(--tinta)!important; margin:0!important; border:none!important;
  display:flex; align-items:center; flex-shrink:0;
}
.stTabs [role="tab"]:nth-child(even){background:var(--salvia-2);}
.stTabs [role="tab"] p{font-size:15px!important; font-weight:600!important; letter-spacing:.06em; color:var(--tinta)!important;}
.stTabs [role="tab"][aria-selected="true"]{background:var(--piedra); height:56px;}
.stTabs [role="tab"]:focus-visible{outline:2px solid var(--menta); outline-offset:2px;}
.stTabs [role="tabpanel"]{
  background:var(--piedra); border-radius:0 8px 8px 8px; padding:2.2rem 2rem 1.2rem!important; margin-top:0!important;
}

/* ---------- fichas de proyecto ---------- */
.ficha{position:relative; margin:34px 0 26px;}
.ficha .lomo{position:absolute; top:-30px; left:18px; height:32px; padding:0 18px;
  background:var(--papel); border-radius:12px 12px 0 0; display:flex; align-items:center;
  font-size:13px; font-weight:600; letter-spacing:.06em; color:#5A6B62;}
.ficha .cuerpo{background:var(--papel); border-radius:4px 10px 10px 10px; padding:16px 16px 20px;
  box-shadow:0 1px 0 rgba(0,0,0,.06);}
.ficha img{width:100%; aspect-ratio:6/5; object-fit:cover; object-position:top; border-radius:6px; display:block;}
.ficha h3{font-size:26px; font-weight:600; color:var(--tinta); letter-spacing:-.015em; margin:16px 0 6px; padding:0;}
.ficha p{color:#33443D; font-size:15.5px; line-height:1.55; margin:0 0 14px;}
.chips{display:flex; flex-wrap:wrap; gap:6px; margin:4px 0 14px;}
.chip{font-size:12.5px; padding:4px 10px; border-radius:999px; background:var(--salvia-2); color:var(--tinta); font-weight:500;}
.abrir{display:inline-block; background:var(--pino); color:var(--menta)!important; text-decoration:none!important;
  padding:10px 18px; border-radius:999px; font-weight:600; font-size:14.5px;}
.abrir:hover{background:var(--pino-2);}
.abrir:focus-visible{outline:2px solid var(--pino); outline-offset:3px;}
.sinlink{display:inline-block; padding:10px 18px; border-radius:999px; border:1.5px dashed #7F8F86;
  color:#5A6B62; font-size:14.5px; font-weight:500;}
.pendiente .cuerpo{opacity:.82;}
.pendiente img{filter:grayscale(.6);}

/* ---------- índice de categorías ---------- */
.indice{margin-top:3.5rem; color:#E7EEE5;}
.indice h2{color:var(--menta); font-weight:500; font-size:34px; letter-spacing:-.02em; margin-bottom:.4rem;}
.indice .nota{color:#A9C3A6; margin-bottom:1.4rem;}
.fila{display:grid; grid-template-columns:minmax(180px, 1fr) 2fr; gap:1rem; padding:14px 0;
  border-top:1px solid rgba(210,234,204,.18);}
.fila .cat{font-weight:600;}
.fila .apps{color:#C5D8C1;}
.fila .vacio{color:#7E9A8E; font-style:italic;}
.pie{margin-top:3rem; color:#7E9A8E; font-size:14px;}

@media (max-width: 700px){
  .hero{height:260px;} .pest{font-size:12px; padding:0 16px; height:40px; top:-36px;}
  .h1{top:50px} .h2{top:95px} .h3{top:140px} .h4{top:185px} .h5{top:225px}
  .portada{grid-template-columns:1fr;} .portada .vol{text-align:left;}
  .stTabs [data-baseweb="tab-panel"]{padding:1.6rem 1rem 1rem;}
  .fila{grid-template-columns:1fr; gap:.2rem;}
}
</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------
# AYUDANTES
# ---------------------------------------------------------------
@st.cache_data
def img_b64(nombre):
    ruta = Path(__file__).parent / nombre
    if not ruta.exists():
        return ""
    tipo = "jpeg" if ruta.suffix.lower() in (".jpg", ".jpeg") else "png"
    return f"data:image/{tipo};base64," + base64.b64encode(ruta.read_bytes()).decode()


def ficha(p):
    src = img_b64(p["img"])
    img = f'<img src="{src}" alt="Captura de {p["titulo"]}">' if src else ""
    chips = "".join(f'<span class="chip">{c}</span>' for c in p["cats"])
    if p.get("pendiente"):
        lomo, boton = "( EN PROCESO )", '<span class="sinlink">Próximamente</span>'
    elif p["url"]:
        lomo = "( 2026 )"
        boton = f'<a class="abrir" href="{p["url"]}" target="_blank" rel="noopener">{p.get("boton", "Abrir la app")}</a>'
    else:
        lomo, boton = "( 2026 )", '<span class="sinlink">Enlace pendiente</span>'
    clase = "ficha pendiente" if p.get("pendiente") else "ficha"
    # sin sangrías: Markdown las convertiría en bloque de código
    return (
        f'<div class="{clase}"><div class="lomo">{lomo}</div><div class="cuerpo">'
        f"{img}<h3>{p['titulo']}</h3><div class=\"chips\">{chips}</div>"
        f"<p>{p['texto']}</p>{boton}</div></div>"
    )


def carpeta(lista):
    cols = st.columns(2, gap="large")
    for i, p in enumerate(lista):
        with cols[i % 2]:
            st.markdown(ficha(p), unsafe_allow_html=True)


# ---------------------------------------------------------------
# PORTADA
# ---------------------------------------------------------------
st.markdown(
    '<div class="hero">'
    '<div class="hoja h1"><div class="pest">( IMAGEN )</div></div>'
    '<div class="hoja h2"><div class="pest">( VOZ )</div></div>'
    '<div class="hoja h3"><div class="pest">( TEXTO )</div></div>'
    '<div class="hoja h4"><div class="pest">( DATOS )</div></div>'
    '<div class="hoja h5"><div class="pest">( 2026 )</div></div>'
    "</div>"
    '<div class="portada">'
    '<svg width="96" height="96" viewBox="-50 -50 100 100" aria-hidden="true">'
    + "".join(
        f'<ellipse cx="0" cy="-27" rx="10" ry="20" fill="#D2EACC" transform="rotate({a})"/>'
        for a in range(0, 360, 60)
    )
    + "</svg>"
    '<div class="vol">INTERFACES<br>MULTIMODALES<br>VOL. 1</div>'
    "</div>"
    '<div class="titulo">Porta<em>folio</em></div>'
    '<div class="sub"><strong>Sthefany Diaz</strong><br>Interfaces Multimodales, profe Carlos Correa.<br><br>'
    "Apps de inteligencia artificial hechas en Streamlit que mezclan imagen, voz, texto, datos "
    "y sensores. Abre una carpeta para ver los trabajos de esa categoría. "
    f'<a href="{URL_CURSO}" target="_blank" rel="noopener">Página del curso</a>.</div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# CARPETAS
# ---------------------------------------------------------------
nombres = ["Todos", "Imagen", "Voz", "Texto", "Datos"]
tabs = st.tabs([f"( {n.upper()} )" for n in nombres])

for tab, nombre in zip(tabs, nombres):
    with tab:
        lista = PROYECTOS if nombre == "Todos" else [p for p in PROYECTOS if nombre in p["tabs"]]
        carpeta(lista)

# ---------------------------------------------------------------
# ÍNDICE: qué categoría del curso cubre cada app
# ---------------------------------------------------------------
filas = "".join(
    f'<div class="fila"><div class="cat">{cat}</div>'
    + (
        f'<div class="apps">{", ".join(apps)}</div>'
        if apps
        else '<div class="apps vacio">Pendiente</div>'
    )
    + "</div>"
    for cat, apps in CATEGORIAS
)
st.markdown(
    '<div class="indice"><h2>Índice de categorías</h2>'
    '<div class="nota">Varias apps cumplen más de una categoría porque mezclan temas.</div>'
    f"{filas}</div>"
    '<div class="pie">Hecho con Python y Streamlit, 2026</div>',
    unsafe_allow_html=True,
)