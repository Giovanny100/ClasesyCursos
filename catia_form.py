import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ===============================
# CONFIGURACIÓN GENERAL
# ===============================
st.set_page_config(
    page_title="CLASES: CUESTIONARIO", 
    page_icon="🎓", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ===============================
# ESTILOS CSS PREMIUM
# ===============================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    /* Variables de color de marca */
    :root {
        --aqua: #00D9C0;
        --pink: #FFB3D9;
        --dark: #1A1A1A;
        --light: #FFFFFF;
        --gray: #F5F5F5;
    }
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Fondo principal oscuro elegante */
    .stApp {
        background: linear-gradient(135deg, #1A1A1A 0%, #2D2D2D 100%);
    }
    
    /* Contenedor principal con glassmorphism */
    .main .block-container {
        padding: 3rem 2rem;
        background: rgba(255, 255, 255, 0.98);
        border-radius: 30px;
        box-shadow: 
            0 20px 60px rgba(0, 217, 192, 0.15),
            0 0 100px rgba(255, 179, 217, 0.1);
        max-width: 900px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 217, 192, 0.1);
    }
    
    /* Hero section con gradiente de marca */
    .hero-section {
        background: linear-gradient(135deg, #00D9C0 0%, #FFB3D9 100%);
        padding: 3rem 2rem;
        border-radius: 25px;
        text-align: center;
        margin: -3rem -2rem 3rem -2rem;
        box-shadow: 0 15px 40px rgba(0, 217, 192, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    /* Logo container */
    .logo-container {
        margin-bottom: 1.5rem;
        filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.2));
    }
    
    /* Títulos con estilo premium */
    h1 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        text-align: center;
        font-size: 3rem !important;
        margin: 0 !important;
        text-shadow: 2px 2px 20px rgba(0, 0, 0, 0.2);
        letter-spacing: -1px;
    }
    
    h2 {
        color: #1A1A1A !important;
        font-weight: 700 !important;
        margin: 3rem 0 1.5rem 0 !important;
        font-size: 1.8rem !important;
        display: flex;
        align-items: center;
        padding-bottom: 1rem;
        border-bottom: 3px solid transparent;
        background: linear-gradient(90deg, #00D9C0, #FFB3D9) bottom / 100% 3px no-repeat;
    }
    
    h2::before {
        content: '';
        width: 50px;
        height: 50px;
        margin-right: 15px;
        background: linear-gradient(135deg, #00D9C0, #FFB3D9);
        border-radius: 12px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 5px 15px rgba(0, 217, 192, 0.3);
    }
    
    /* Tarjeta de descripción premium */
    .description-card {
        background: linear-gradient(135deg, rgba(0, 217, 192, 0.1), rgba(255, 179, 217, 0.1));
        padding: 2rem;
        border-radius: 20px;
        border-left: 5px solid #00D9C0;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        backdrop-filter: blur(10px);
    }
    
    .description-card p {
        margin: 0;
        line-height: 1.8;
        color: #2D2D2D;
    }
    
    /* Labels mejorados */
    .stRadio > label, .stMultiSelect > label {
        font-weight: 600 !important;
        color: #1A1A1A !important;
        font-size: 1.05rem !important;
        margin-bottom: 0.8rem !important;
        display: block;
    }
    
    /* Radio buttons con estilo de marca */
    .stRadio > div {
        background: #F5F5F5;
        padding: 1.2rem;
        border-radius: 15px;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stRadio > div:hover {
        border-color: #00D9C0;
        background: rgba(0, 217, 192, 0.05);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 217, 192, 0.15);
    }
    
    /* Multiselect styling */
    .stMultiSelect > div > div {
        background: #F5F5F5;
        border-radius: 15px;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stMultiSelect > div > div:focus-within {
        border-color: #00D9C0;
        box-shadow: 0 0 0 3px rgba(0, 217, 192, 0.1);
    }
    
    /* Tags seleccionados */
    span[data-baseweb="tag"] {
        background: linear-gradient(135deg, #00D9C0, #FFB3D9) !important;
        color: white !important;
        border-radius: 20px !important;
        padding: 5px 12px !important;
        font-weight: 500 !important;
    }
    
    /* Botón principal premium */
    .stButton > button {
        background: linear-gradient(135deg, #00D9C0 0%, #FFB3D9 100%) !important;
        color: #1A1A1A !important;
        font-weight: 700 !important;
        font-size: 1.3rem !important;
        padding: 1rem 3rem !important;
        border-radius: 50px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 
            0 15px 35px rgba(0, 217, 192, 0.3),
            0 5px 15px rgba(255, 179, 217, 0.2) !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 2rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 
            0 20px 50px rgba(0, 217, 192, 0.4),
            0 10px 25px rgba(255, 179, 217, 0.3) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98) !important;
    }
    
    /* Success message mejorado */
    .success-card {
        background: linear-gradient(135deg, rgba(0, 217, 192, 0.15), rgba(255, 179, 217, 0.15));
        padding: 3rem 2rem;
        border-radius: 25px;
        text-align: center;
        margin-top: 3rem;
        border: 2px solid #00D9C0;
        box-shadow: 0 15px 40px rgba(0, 217, 192, 0.2);
    }
    
    .success-card h3 {
        color: #1A1A1A;
        font-size: 2rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    /* Animación para los iconos de sección */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    h2::before {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Progress indicator */
    .progress-container {
        background: #F5F5F5;
        height: 6px;
        border-radius: 10px;
        margin: 2rem 0;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #00D9C0, #FFB3D9);
        width: 0%;
        transition: width 0.5s ease;
        box-shadow: 0 0 10px rgba(0, 217, 192, 0.5);
    }
    
    /* Divider elegante */
    hr {
        margin: 3rem 0;
        border: none;
        height: 3px;
        background: linear-gradient(to right, transparent, #00D9C0, #FFB3D9, transparent);
        opacity: 0.3;
    }
    
    /* Columnas responsive */
    [data-testid="column"] {
        padding: 0 1rem;
    }
    
    /* Tooltip style */
    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 2px dotted #00D9C0;
        cursor: help;
    }
    
    /* Footer branding */
    .footer-brand {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 2px solid rgba(0, 217, 192, 0.1);
        color: #666;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ===============================
# HERO SECTION CON LOGO
# ===============================
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <div class="logo-container">
""", unsafe_allow_html=True)

# LOGO - Elige UNA de estas opciones y comenta las demás:

# Opción 1: Imagen local en la misma carpeta
# st.image("logo.png", width=200)

# Opción 2: Imagen en carpeta assets
# st.image("assets/logo.png", width=200)

# Opción 3: URL de internet
# st.image("https://tu-url.com/logo.png", width=200)

# Opción 4: Placeholder temporal (emoji grande)
st.markdown("<div style='font-size: 5rem; margin: 0;'>🎓</div>", unsafe_allow_html=True)

st.markdown("""
        </div>
        <h1>CUESTIONARIO EDUCATIVO</h1>
        <p style='color: white; font-size: 1.2rem; margin-top: 1rem; font-weight: 300;'>
            Tu opinión importa • Anónimo • 3 minutos
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ===============================
# TARJETA DE DESCRIPCIÓN
# ===============================
st.markdown("""
<div class="description-card">
    <p style='font-size: 1.15rem; font-weight: 600; margin-bottom: 1rem; color: #1A1A1A;'>
        📊 ¿Por qué tu opinión es importante?
    </p>
    <p style='font-size: 1rem; color: #2D2D2D;'>
        Estamos diseñando <strong>servicios educativos innovadores</strong> basados en lo que realmente necesitas. 
        Este cuestionario es <strong>100% anónimo</strong> y tus respuestas nos ayudarán a crear 
        <strong>cursos más útiles, divertidos y efectivos</strong>.
    </p>
    <p style='margin-top: 1.5rem; padding: 1rem; background: rgba(0, 217, 192, 0.1); border-radius: 10px; color: #00D9C0; font-weight: 600;'>
        🎯 Objetivo: Crear experiencias educativas que realmente te ayuden a aprender y disfrutar el proceso
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# DICCIONARIOS PARA CODIFICACIÓN
# ===============================
CODIGOS = {
    "semestre": {"1°": 1, "2°": 2, "3°": 3, "4°": 4, "5°": 5, "6°": 6},
    "genero": {"Hombre": 1, "Mujer": 2, "Prefiero no decirlo": 3},
    "turno": {"Matutino": 1, "Vespertino": 2},
    "preferencia_pasar": {
        "Estudiar mucho": 1,
        "Pagar un curso extra": 2,
        "Que resuelvan el examen por mí": 3,
        "Ninguna de las anteriores": 4
    },
    "pagarias_rubrica": {"Sí": 1, "No": 2, "Depende del precio": 3},
    "tipo_profesor": {
        "Hombre": 1,
        "Mujer": 2,
        "Un personaje animado en videos": 3,
        "Me da lo mismo mientras aprenda": 4
    },
    "pago_justo": {
        "Menos de $200": 1,
        "$200–$400": 2,
        "$400–$600": 3,
        "Más de $600": 4
    },
    "red_social": {
        "TikTok": 1,
        "Instagram": 2,
        "WhatsApp": 3,
        "YouTube": 4,
        "Facebook": 5
    }
}

MATERIAS_OPC = ["Matemáticas / Física", "Química / Biología", "Historia / Sociales", "Artísticas", "Otro"]
RAZONES_OPC = ["Los profes no explican bien", "Son aburridas las clases", "Los alumnos no estudian", "La escuela no importa"]
CURSOS_OPC = ["Programación de videojuegos", "Trucos y secretos de la IA", "Diseño y Marketing", "Inversiones y manejo de dinero", "Otra"]
CONFIANZA_OPC = ["Recomendaciones de amigos", "Ver resultados o reseñas", "Que tenga un personaje animado que explique", "Que ofrezcan prueba gratuita"]

# ===============================
# FORMULARIO PREMIUM
# ===============================
with st.form("catia_form"):
    
    # SECCIÓN 1: Datos Generales
    st.markdown("<h2>🧠 Datos Generales</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        semestre = st.radio(
            "¿En qué semestre estás?", 
            ["1°", "2°", "3°", "4°", "5°", "6°"],
            help="Selecciona tu semestre actual"
        )
        turno = st.radio(
            "¿En qué turno estudias?", 
            ["Matutino", "Vespertino"],
            help="¿Estudias por la mañana o por la tarde?"
        )
    
    with col2:
        genero = st.radio(
            "¿Cuál es tu sexo?", 
            ["Hombre", "Mujer", "Prefiero no decirlo"],
            help="Esta información es confidencial"
        )
    
    # SECCIÓN 2: Dificultades Académicas
    st.markdown("<h2>📚 Dificultades Académicas</h2>", unsafe_allow_html=True)
    
    materias = st.multiselect(
        "¿Qué materias se te dificultan más?",
        MATERIAS_OPC,
        help="Puedes seleccionar varias opciones"
    )
    
    razones = st.multiselect(
        "¿Por qué razones crees que tú o algún amig@ reprueban las materias?",
        RAZONES_OPC,
        help="Selecciona todas las que consideres relevantes"
    )
    
    # SECCIÓN 3: Comportamiento y Preferencias
    st.markdown("<h2>💡 Comportamiento y Preferencias</h2>", unsafe_allow_html=True)
    
    pasar = st.radio(
        "¿Para pasar una materia cuál de las siguientes opciones prefieres?",
        ["Estudiar mucho", "Pagar un curso extra", "Que resuelvan el examen por mí", "Ninguna de las anteriores"],
    )
    
    col3, col4 = st.columns([1.5, 1])
    with col3:
        pagarias = st.radio(
            "¿Pagarías por que te hagan un examen o rúbrica para pasar una materia aburrida?",
            ["Sí", "No", "Depende del precio"],
        )
    
    curso = st.multiselect(
        "¿De cuál de los siguientes temas tomarías un curso?",
        CURSOS_OPC,
        help="Selecciona los temas que te interesan"
    )
    
    col5, col6 = st.columns(2)
    with col5:
        profesor = st.radio(
            "Prefieres que te dé clases:",
            ["Hombre", "Mujer", "Un personaje animado en videos", "Me da lo mismo mientras aprenda"],
        )
    
    with col6:
        pago = st.radio(
            "¿Cuánto te parece justo pagar por ayuda para pasar una materia difícil?",
            ["Menos de $200", "$200–$400", "$400–$600", "Más de $600"],
        )
    
    # SECCIÓN 4: Marketing y Redes
    st.markdown("<h2>🎯 Marketing y Confianza</h2>", unsafe_allow_html=True)
    
    confianza = st.multiselect(
        "¿Qué te haría confiar en una escuela o persona que ofrece ese tipo de ayuda?",
        CONFIANZA_OPC,
        help="Selecciona los factores más importantes para ti"
    )
    
    red = st.radio(
        "¿En qué red social pasas más tiempo?",
        ["TikTok", "Instagram", "WhatsApp", "YouTube", "Facebook"],
        help="Esto nos ayuda a saber dónde comunicarnos mejor"
    )
    
    # BOTÓN DE ENVÍO
    enviado = st.form_submit_button("🚀 Enviar Respuestas")

# ===============================
# GUARDADO Y CONFIRMACIÓN
# ===============================
if enviado:
    def codificar_multiselect(selecciones, opciones):
        return ", ".join([str(opciones.index(item) + 1) for item in selecciones])
    
    filename = "respuestas.csv"
    existe = os.path.isfile(filename)
    
    data = {
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "semestre": [CODIGOS["semestre"][semestre]],
        "genero": [CODIGOS["genero"][genero]],
        "turno": [CODIGOS["turno"][turno]],
        "materias_dificiles": [codificar_multiselect(materias, MATERIAS_OPC)],
        "razones_reprobacion": [codificar_multiselect(razones, RAZONES_OPC)],
        "preferencia_pasar": [CODIGOS["preferencia_pasar"][pasar]],
        "pagarias_rubrica": [CODIGOS["pagarias_rubrica"][pagarias]],
        "curso_interes": [codificar_multiselect(curso, CURSOS_OPC)],
        "tipo_profesor": [CODIGOS["tipo_profesor"][profesor]],
        "pago_justo": [CODIGOS["pago_justo"][pago]],
        "confianza_en_ayuda": [codificar_multiselect(confianza, CONFIANZA_OPC)],
        "red_social": [CODIGOS["red_social"][red]],
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, mode="a", header=not existe, index=False, encoding="utf-8-sig")
    
    # ANIMACIÓN Y MENSAJE DE ÉXITO
    st.balloons()
    st.markdown("""
    <div class="success-card">
        <h3>🎉 ¡Gracias por tu participación!</h3>
        <p style='font-size: 1.2rem; color: #2D2D2D; margin: 1.5rem 0;'>
            Tu opinión es <strong>invaluable</strong> para crear mejores experiencias educativas.
        </p>
        <p style='font-size: 1rem; color: #666;'>
            ✓ Respuestas registradas exitosamente<br>
            ✓ Información procesada de forma anónima<br>
            ✓ Contribuyendo a mejorar la educación
        </p>
        <div style='margin-top: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #00D9C0, #FFB3D9); border-radius: 15px;'>
            <p style='color: white; font-weight: 600; margin: 0; font-size: 1.1rem;'>
                💚 Comparte este cuestionario con tus amigos 💕
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer-brand">
    <p>Hecho con 💚 y 💕 • Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)